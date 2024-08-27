# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : base_prompt.py
# Time       ：2024/8/25 17:36
# Author     ：jianbang
# version    ：python 3.10
# company    : IFLYTEK Co.,Ltd.
# emil       : whdx072018@foxmail.com
# Description：
"""
from abc import ABC
from abc import abstractmethod
from typing import NoReturn

class BasePrompt(ABC):
    prompt_type="base class for prompt subclasses"
    prompt_description="This structure of prompt"

    def __init__(self,*args,**kwargs):
        """
        :param args:
        :param kwargs:
        """
        self.prompt_language=None

    @abstractmethod
    def build_prompt(self,*args,**kwargs)->NoReturn:
        """
        :param args:
        :param kwargs:
        :return:
        """
        raise NotImplementedError

    @abstractmethod
    def init_prompt(self,*args,**kwargs)->NoReturn:
        """
        :param args:
        :param kwargs:
        :return:
        """
        raise NotImplementedError

    @classmethod
    def __repr__(cls):
        function_info=str(cls.prompt_type)+"\n"+str(cls.prompt_description)
        return function_info
