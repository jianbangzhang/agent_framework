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




class BasePrompt(ABC):
    prompt_type="base class for prompt subclasses"
    prompt_description="This structure of prompt"

    def __init__(self,language,n_shot_prompt,enable_rewrite,*args,**kwargs):
        """
        :param args:
        :param kwargs:
        """
        self.prompt_language=language
        self.n_shot_examples=n_shot_prompt
        self.enable_rewrite=enable_rewrite

    @abstractmethod
    def set_lang(self, language: str):
        """
        :param language:
        :return:
        """
        raise NotImplementedError

    @abstractmethod
    def set_example_number(self, value: int):
        """
        :param value:
        :return:
        """
        raise NotImplementedError


    @classmethod
    def __repr__(cls):
        function_info=str(cls.prompt_type)+"\n"+str(cls.prompt_description)
        return function_info
