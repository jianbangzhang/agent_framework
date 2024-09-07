# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : retrieve_memory.py
# Time       ：2024/9/1 12:56
# Author     ：jianbang
# version    ：python 3.10
# company    : IFLYTEK Co.,Ltd.
# emil       : whdx072018@foxmail.com
# Description：
"""

from .tool import BaseTool
from utils import retry
from typing import Dict,Tuple,Union



class RetrieveTool(BaseTool):
    name = "retrieve_memory_api"
    is_remote=True
    description="这是一个memory检索工具"

    def __call__(self,user_question, rewrite_question,*args, **kwargs)->Tuple:
        """
        :param user_question:
        :param rewrite_question:
        :param args:
        :param kwargs:
        :return:
        """
        memory_obj=kwargs.get("memory",None)
        if memory_obj is None:
            raise ValueError

        date_dict,code=self._call_api(memory_obj,user_question, rewrite_question,*args, **kwargs)
        return date_dict,code

    @retry(max_retry=1, delay=0)
    def _call_api(self,memory_obj,user_question, rewrite_question,*args, **kwargs)->Union[Dict,None]:
        """
        :param memory_obj:
        :param user_question:
        :param rewrite_question:
        :param args:
        :param kwargs:
        :return:
        """
        n_example=memory_obj.query(user_question,
                rewrite_question=rewrite_question,*args, **kwargs)

        return {"result": n_example}
