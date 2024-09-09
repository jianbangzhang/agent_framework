# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : get_observation.py
# Time       ：2024/9/2 19:14
# Author     ：jianbang
# version    ：python 3.10
# company    : IFLYTEK Co.,Ltd.
# emil       : whdx072018@foxmail.com
# Description：
"""
import pandas as pd
from .tool import BaseTool
from utils import retry
from typing import Tuple
import os
import jieba
import random
from rouge_chinese import Rouge



class RetrieveTool(BaseTool):
    name = "retrieve_api"
    is_remote=True
    description="这是一个observation检索工具"

    def __call__(self,api=None,user_question=None,param=None,*args, **kwargs)->Tuple:
        """
        :param user_question:
        :param rewrite_question:
        :param args:
        :param kwargs:
        :return:
        """
        project_path = os.getenv("project_path")
        path= os.path.join(project_path,"dataset/tool_result/tool_based.xlsx")
        self.df=pd.read_excel(path)
        get_observation=kwargs.get("observation",True)

        if get_observation:
            date,code=self._call_observation_from_dataset(api,param=param)
        else:
            date, code = self._call_tools_from_dataset(user_question=user_question)
        return date,code

    @retry(max_retry=1, delay=0)
    def _call_observation_from_dataset(self,api,param):
        """
        :param user_question:
        :param api:
        :param param:
        :param args:
        :param kwargs:
        :return:
        """
        df=self.df
        tool_name=df["tool_name"].to_list()
        observation_lst=df["return"].to_list()
        for tool,observation in zip(tool_name,observation_lst):
            try:
                if not isinstance(tool,str) and not isinstance(observation,str):
                    continue
                if api.lower()==tool.lower():
                    if isinstance(observation,str):
                        observation=eval(observation)
                        for key in param:
                            observation[key]=param[key]
                    else:
                        observation=observation
                    return str(observation)
                else:
                    continue
            except:
                continue
        observation="未查询到相关的内容"
        return observation

    @retry(max_retry=1, delay=0)
    def _call_tools_from_dataset(self,user_question):
        df=self.df
        tool_descriptions = df["tool_description"].to_list()
        query_lst=df["query"].to_list()
        tool_lst=[]
        scores=[]
        for tool,query in zip(tool_descriptions,query_lst):
            try:
                if not isinstance(tool,str) and not isinstance(query,str):
                    continue
                score = self._calculate_similarity(user_question, query)
                scores.append(score)
                tool_lst.append(tool)
            except:
                continue

        tool_lst_best=self._get_top_k(scores,tool_lst)
        return tool_lst_best


    def _get_top_k(self,scores,tool_lst,k=3):
        """
        :param scores:
        :param tool_lst:
        :param k:
        :return:
        """
        self.idxs=[index for index, value in sorted(enumerate(scores), key=lambda x: x[1], reverse=True)[:1]]
        self.idxs+=[index for index, value in sorted(enumerate(scores), key=lambda x: x[1], reverse=False)[:k-1]]
        tools=[tool_lst[id] for id in self.idxs]
        return tools


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










