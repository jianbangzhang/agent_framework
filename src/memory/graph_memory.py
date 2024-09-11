# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : graph_memory.py
# Time       ：2024/8/26 08:45
# Author     ：jianbang
# version    ：python 3.10
# company    : IFLYTEK Co.,Ltd.
# emil       : whdx072018@foxmail.com
# Description：
"""
import jieba
from rouge_chinese import Rouge
import json
import os
import re
from .meta import MetaMemory


class GraphMemory(MetaMemory):
    def __init__(self,memory_type,memory_size,retrieval_technique,n_shot,*args,**kwargs):
        """
        :param memory_type: 
        :param memory_size: 
        :param retrieval_technique: 
        :param n_shot: 
        :param args: 
        :param kwargs: 
        """
        super(GraphMemory,self).__init__(memory_type,memory_size,retrieval_technique,n_shot,*args,**kwargs)
        self.memory_type=memory_type
        self.database_type="triplets"
        project_path=os.environ.get("project_path")
        self.file_path=os.path.join(project_path,"dataset/momery/triplets_based_reflection.jsonl")

    def _read_jsonl(self,file_path):
        """
        :param file_path:
        :return:
        """
        data = []
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                data.append(json.loads(line))
        return data

    def _calculate_similarity(self,sentence1, sentence2):
        """
        :param sentence1:
        :param sentence2:
        :return:
        """
        evaluator = Rouge()
        predictions = ' '.join(jieba.cut(sentence1))
        gold_labels = ' '.join(jieba.cut(sentence2))
        scores = evaluator.get_scores(predictions, gold_labels)
        rouge_l_f_score = scores[0]['rouge-l']['f']
        return rouge_l_f_score

    def save(self, user_question,content, *args, **kwargs):
        """
        :param user_question:
        :param content:
        :param args:
        :param kwargs:
        :return:
        """
        total_data = self._read_jsonl(self.file_path)
        question_lst=[d["question"] for d in total_data]
        if not user_question in question_lst:
            content=self._transform_data(user_question,content)
            with open(self.file_path, 'a', encoding='utf-8') as f:
                json_record = json.dumps(content,ensure_ascii=False)
                f.write(json_record + '\n')
        else:
            pass

    def query(self, question,rewrite_query=None, *args, **kwargs):
        """
        :param question:
        :param args:
        :param kwargs:
        :return:
        """
        scores=[]
        matchs=[]
        total_data=self._read_jsonl(self.file_path)
        for data_dict in total_data:
            query=data_dict["question"]
            score=self._calculate_similarity(question,query)
            if rewrite_query is not None:
                score += self._calculate_similarity(rewrite_query, query)
            scores.append(score)
            matchs.append(data_dict)
        max_score_id=scores.index(max(scores))
        best_data=matchs[max_score_id]
        return best_data

    def _transform_data(self,question,content):
        """
        :param content:
        positive_reflection:
        - React: hm_product_recommend[param:keywords_dict]-after-我们有以下几款手机供您选择：1.小米11 Ultra 5G手机 256GB：价格为5999元，拥有120Hz高刷新率和骁龙888处理器，还配备了高品质相机系统；2. vivo X60 Pro 5G手机 256GB：售价为4498元，搭载Exynos 1080处理器与ZEISS联合调校的相机系统，拍照实力十足；3. 华为畅享 20 Pro 5G手机 128GB：价格亲民，只需2699元即可拥有优秀的相机和4000mAh的电池容量。
        negative_reflection:
        - positive reacting: hm_product_recommend[param: {'keywords_dict': {'商品类目': '手机'}}]-after-我们有以下几款手机供您选择：1.小米11 Ultra 5G手机 256GB：价格为5999元，拥有120Hz高刷新率和骁龙888处理器，还配备了高品质相机系统；2. vivo X60 Pro 5G手机 256GB：售价为4498元，搭载Exynos 1080处理器与ZEISS联合调校的相机系统，拍照实力十足。
        - negative reacting: hm_product_recommend[param: {'keywords_dict': '手机'}]-after-参数传递错误。", "negative reacting: hm_product_recommend[param: {'sku_code_list': ['手机']}]-after-参数传递错误。
        :return:
        """
        content_lst = [line.strip() for line in content.split("\n") if line.strip()]
        total_dict = {"question":question,"positive_reflection": None, "negative_reflection": []}
        i = 0
        size = len(content_lst)
        while i < size:
            if i + 1 >= size:
                break
            cur_line = content_lst[i]
            next_line = content_lst[i + 1]
            if "positive_reflection" in cur_line:
                key = "positive_reflection"
                total_dict[key] = re.sub("-", "", next_line, count=1).strip()
            elif "negative_reflection" in cur_line:
                key = "negative_reflection"
                total_dict[key].append(re.sub("-", "", next_line, count=1).strip())
            else:
                pass
            i += 2

        last_line = content_lst[-1]
        total_dict["negative_reflection"].append(re.sub("-", "", last_line, count=1).strip())
        return total_dict

