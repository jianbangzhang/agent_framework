# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : text_memory.py
# Time       ：2024/9/7 11:03
# Author     ：jianbang
# version    ：python 3.10
# company    : IFLYTEK Co.,Ltd.
# emil       : whdx072018@foxmail.com
# Description：
"""
import os
import json
import re
import jieba
from rouge_chinese import Rouge
from .meta import MetaMemory


class TextMemory(MetaMemory):
    def __init__(self,memory_type,memory_size,retrieval_technique,n_shot,*args,**kwargs):
        """
        :param memory_type:
        :param memory_size:
        :param retrieval_technique:
        :param n_shot:
        :param args:
        :param kwargs:
        """
        super(TextMemory,self).__init__(memory_type,memory_size,retrieval_technique,n_shot,*args,**kwargs)
        self.memory_type=memory_type
        self.database_type="natural"
        project_path = os.environ.get("project_path")
        self.file_path = os.path.join(project_path, "dataset/momery/text_based_reflection.json")

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

    def save(self,question,content, *args, **kwargs):
        """
        :param question:
        :param content:
        :param args:
        :param kwargs:
        :return:
        """
        content=self._transform_data(question,content)
        with open(self.file_path, 'a', encoding='utf-8') as f:
            json_record = json.dumps(content,ensure_ascii=False)
            f.write(json_record + '\n')

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
            scores.append(score)
            matchs.append(data_dict)
        max_score_id=scores.index(max(scores))
        best_data=matchs[max_score_id]
        return best_data

    def _transform_data(self,question,content):
        """
        :param content:
        positive_reflection:
        - {"问题": "用户询问有哪些手机可以推荐。", "规划过程": "调用hm_product_recommend API，传入关键词字典{'商品类目': '手机'}。", "回复": "您好，我们有以下几款手机供您选择：1.小米11 Ultra 5G手机 256GB：价格为5999元，拥有120Hz高刷新率和骁龙888处理器，还配备了高品质相机系统；2. vivo X60 Pro 5G手机 256GB：售价为4498元，搭载Exynos 1080处理器与ZEISS联合调校的相机系统，拍照实力十足。这些手机都具有不同的特点和功能，您可以根据自己的需求进行选择。如果您有其他问题或需求，请随时告诉我。"}
        negative_reflection:
        - {"tools_using": "API相似度高：系统中可能存在其他用于推荐商品的API，如hm_product_marketing或hm_product_info，这些API名称和功能与hm_product_recommend非常接近，容易造成误调用。", "parameters_passing": "参数拼写错误：如果keywords_dict参数中的值被拼写错误（如'商品类目'被拼写成'商品类别'），API可能无法识别该参数，导致查询失败。不完整或错误的参数设置：有些API可能需要多个参数共同传递，但如果遗漏了必需的参数或者误传了无关的参数，也可能导致API无法返回正确结果。"}
        :return:
        """
        content_lst=[line.strip() for line in content.split("\n") if line.strip()]
        i=0
        size=len(content_lst)
        total_dict=dict()
        while i<size:
            if i+1>=size:
                break
            cur_line = content_lst[i]
            next_line=content_lst[i+1]
            if "positive_reflection" in cur_line:
                key="positive_reflection"
                total_dict[key] = re.sub("-", "", next_line, count=1).strip()
            elif "negative_reflection" in cur_line:
                key="negative_reflection"
                total_dict[key] = re.sub("-", "", next_line, count=1).strip()
            else:
                pass

            i += 2
        return total_dict








