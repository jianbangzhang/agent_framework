# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : llm_prompt.py
# Time       ：2024/8/25 17:36
# Author     ：jianbang
# version    ：python 3.10
# company    : IFLYTEK Co.,Ltd.
# emil       : whdx072018@foxmail.com
# Description：
"""
from abc import abstractmethod
from src.prompt.meta.base_prompt import BasePrompt


class LLMPrompt(BasePrompt):
    def __init__(self,language,n_shot_prompt,enable_rewrite,*args,**kwargs):
        super(LLMPrompt,self).__init__(language,n_shot_prompt,enable_rewrite,*args,**kwargs)
        self.system_template=None
        self.requirements=None
        self.examples=None
        self.prompt=None
        self.enable_rewrite=enable_rewrite

    def set_lang(self,language:str):
        """
        :param language:
        :return:
        """
        self.prompt_language=language

    def set_example_number(self,value:int):
        """
        :param value:
        :return:
        """
        self.n_shot_examples=value

    @abstractmethod
    def build_prompt(self,input,*args, **kwargs):
        """
        :param args:
        :param kwargs:
        :return:
        """
        raise NotImplementedError


    @abstractmethod
    def _check_config(self):
        raise NotImplementedError

    @classmethod
    def __repr__(cls):
        function_info = str(cls.prompt_type) + "\n" + str(cls.prompt_description)
        return function_info



