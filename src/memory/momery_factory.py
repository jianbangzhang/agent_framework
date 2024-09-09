# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : momery_factory.py
# Time       ：2024/8/26 08:54
# Author     ：jianbang
# version    ：python 3.10
# company    : IFLYTEK Co.,Ltd.
# emil       : whdx072018@foxmail.com
# Description：
"""
from .graph_memory import GraphMemory
from .text_memory import TextMemory


class MemoryFactory(object):
    def __init__(self,*args,**kwargs):
        self.args=args
        self.kwargs=kwargs

    def build_memory(self,memory_type,memory_size,retrieval_technique,n_shot,*args,**kwargs):
        """
        :param memory_type:
        :param args:
        :param kwargs:
        :return:
        """
        if memory_type=="graph":
            self.memory=GraphMemory(memory_type,memory_size,retrieval_technique,n_shot,*args,**kwargs)
        else:
            self.memory=TextMemory(memory_type,memory_size,retrieval_technique,n_shot,*args,**kwargs)

    def save(self, content, *args, **kwargs):
        """
        :param content:
        :param args:
        :param kwargs:
        :return:
        """
        return self.memory.save(content, *args, **kwargs)

    def query(self, question, rewrite_query=None, *args, **kwargs):
        """
        :param question:
        :param args:
        :param kwargs:
        :return:
        """
        return self.memory.query(question, rewrite_query=rewrite_query, *args, **kwargs)

