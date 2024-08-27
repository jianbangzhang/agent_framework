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
        self.memory_type="graph"
        self.database_type="neo4j"

    def save(self, content, *args, **kwargs):
        pass

    def query(self, question, *args, **kwargs):
        pass

    def reorder(self, *args, **kwargs):
        pass

    def update(self, *args, **kwargs):
        pass
