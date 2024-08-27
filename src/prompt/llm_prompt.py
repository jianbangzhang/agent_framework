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
from .base_prompt import BasePrompt


class LLM_Prompt(BasePrompt):
    def __init__(self,*args,**kwargs):
        super(LLM_Prompt,self).__init__(*args,**kwargs)

    def set_lang(self,language:str):
        self.prompt_language=language

    def build_prompt(self,agent_name, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        :return:
        """
        memory_obj = kwargs.get("memory",None)
        if agent_name=="executor":
            pass
        elif agent_name=="searcher":
            if memory_obj is None:
                raise ModuleNotFoundError
            # todo
        elif agent_name=="refiner":
            pass
        else:
            raise NotImplementedError

    def init_prompt(self, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        :return:
        """
        raise NotImplementedError

    @classmethod
    def __repr__(cls):
        function_info = str(cls.prompt_type) + "\n" + str(cls.prompt_description)
        return function_info



