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
import json
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
        self.memory_type="text"
        self.database_type="natural"
        self.file_path="/Users/whu/Downloads/agent-framework/dataset/momery/text_based_reflection.jsonl"

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
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.metrics.pairwise import cosine_similarity

        tfidf_vectorizer = TfidfVectorizer()
        tfidf_matrix = tfidf_vectorizer.fit_transform([sentence1, sentence2])
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
        return similarity[0][0]

    def save(self, content, *args, **kwargs):
        """
        :param content:
        :param args:
        :param kwargs:
        :return:
        """
        with open(self.file_path, 'a', encoding='utf-8') as f:
            json_record = json.dumps(content)
            f.write(json_record + '\n')

    def query(self, question, *args, **kwargs):
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


