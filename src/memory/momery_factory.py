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
        pass

    def build_memory(self,memory_type,*args,**kwargs):
        """
        :param memory_type:
        :param args:
        :param kwargs:
        :return:
        """
        if memory_type=="graph":
            self.memory=GraphMemory(*args,**kwargs)
        else:
            self.memory=TextMemory(*args,**kwargs)

