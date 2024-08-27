# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : base_model.py
# Time       ：2024/8/25 17:51
# Author     ：jianbang
# version    ：python 3.10
# company    : IFLYTEK Co.,Ltd.
# emil       : whdx072018@foxmail.com
# Description：
"""
from abc import ABC,abstractmethod



class BaseModel(ABC):
    def __init__(self,model_type,model_name,is_remote_llm,**kwargs):
        """
        :param model_type:
        :param model_name:
        :param is_remote_llm:
        :param kwargs:
        """
        self.model_type=model_type
        self.model_name=model_name
        self.is_remote_llm=is_remote_llm
        self.kwargs=kwargs


    def generate(self,*args,**kwargs):
        return self._generate(*args,**kwargs)


    @abstractmethod
    def _generate(self,*args,**kwargs):
        raise NotImplementedError


    def __repr__(self):
        info="This is meta class for model classes"
        return info

