# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : refiner_prompt.py
# Time       ：2024/8/28 11:02
# Author     ：jianbang
# version    ：python 3.10
# company    : IFLYTEK Co.,Ltd.
# emil       : whdx072018@foxmail.com
# Description：
"""
from src.prompt.meta.llm_prompt import LLMPrompt
from src.prompt.meta.constants import (REFINER_SYSTEM_TEMPLATES,
                                       REFINER_REQUIREMENTS_TRIPLETS,
                                       REFINER_REQUIREMENTS_NATURAL,
                                       REFINER_EXAMPLES_TRIPLETS,
                                       REFINER_EXAMPLES_NATURAL)


class RefinerPrompt(LLMPrompt):
    def __init__(self,language,n_shot_prompt,enable_rewrite,*args,**kwargs):
        """
        :param language:
        :param n_shot_prompt:
        :param args:
        :param kwargs:
        """
        super(RefinerPrompt, self).__init__(language,n_shot_prompt,enable_rewrite,*args,**kwargs)
        self.system_template=REFINER_SYSTEM_TEMPLATES
        self._check_config()

    def build_prompt(self,input, *args, **kwargs):
        memory_type=kwargs.get("memory",None)
        if memory_type is None:
            raise ValueError("memory should not be None type.")

        self._set_requirements(memory_type)
        self._set_examples(memory_type)
        self.prompt=self.system_template+"\n\n"
        self.prompt+=self.requirements+"\n\n"
        self.prompt+=self.examples+"\n\n"
        self.prompt+=f"现在开始：\n输入：{input}\n输出：\n"
        return self.prompt


    def _set_requirements(self,memory_type):
        if memory_type=="graph":
            self.requirements=REFINER_REQUIREMENTS_TRIPLETS
        else:
            self.requirements=REFINER_REQUIREMENTS_NATURAL

    def _set_examples(self,memory_type):
        if memory_type=="graph":
            self.examples=REFINER_EXAMPLES_TRIPLETS
        else:
            self.examples=REFINER_EXAMPLES_NATURAL

    def _check_config(self):
        """
        :return:
        """
        if self.prompt_language=="en":
            raise NotImplementedError
        if self.n_shot_examples!=1:
            raise ValueError

    def set_lang(self,language:str):
        self.prompt_language=language