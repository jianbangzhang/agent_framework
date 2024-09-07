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
from typing import Dict,Tuple,Union



class RetrieveObservation(BaseTool):
    name = "retrieve_observation_api"
    is_remote=True
    description="这是一个observation检索工具"

    def __call__(self,user_question,api,param,*args, **kwargs)->Tuple:
        """
        :param user_question:
        :param rewrite_question:
        :param args:
        :param kwargs:
        :return:
        """
        self.path= "/dataset/tool_result/tool_based.xlsx"
        memory_obj=kwargs.get("memory",None)
        if memory_obj is None:
            raise ValueError

        date_dict,code=self._call_api(user_question,api,param,*args, **kwargs)
        return date_dict,code

    @retry(max_retry=1, delay=0)
    def _call_api(self,user_question,api,param,*args, **kwargs)->Union[Dict,None]:
        """
        :param user_question:
        :param api:
        :param param:
        :param args:
        :param kwargs:
        :return:
        """
        df=pd.read_excel(self.path)
        tool_name=df["tool_name"].to_list()
        observation_lst=df["return"].to_list()
        for tool,observation in zip(tool_name,observation_lst):
            if api==tool:
                return observation
            else:
                continue
        observation="未查询到相关的内容"
        return observation





