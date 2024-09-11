# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : meta.py
# Time       ：2024/8/25 22:16
# Author     ：jianbang
# version    ：python 3.10
# company    : IFLYTEK Co.,Ltd.
# emil       : whdx072018@foxmail.com
# Description：
"""
from abc import ABC,abstractmethod

class MetaMemory(ABC):
    def __init__(self,memory_type,memory_size,retrieval_technique,n_shot,*args,**kwargs):
        """
        :param memory_type:
        :param memory_size:
        :param retrieval_technique:
        :param n_shot:
        :param args:
        :param kwargs:
        """
        self.memory_type=memory_type
        self.memory_size=memory_size
        self.retrieval_technique=retrieval_technique
        self.n_shot=n_shot

    @abstractmethod
    def save(self,user_question,content,*args,**kwargs):
        raise NotImplementedError


    @abstractmethod
    def query(self,question,rewrite_query,*args,**kwargs):
        raise NotImplementedError










