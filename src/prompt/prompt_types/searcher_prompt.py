# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : searcher_prompt.py
# Time       ：2024/8/31 21:39
# Author     ：jianbang
# version    ：python 3.10
# company    : IFLYTEK Co.,Ltd.
# emil       : whdx072018@foxmail.com
# Description：
"""
from src.prompt.meta.llm_prompt import LLMPrompt
from src.prompt.meta.constants import (SEARCHER_SYSTEM_TEMPLATES,
                                       SEARCHER_SYSTEM_TEMPLATES_WIHT_REWRITE,
                                       SEARCHER_REQUIREMENTS)


class SearcherPrompt(LLMPrompt):
    def __init__(self,language,n_shot_prompt,enable_rewrite,*args,**kwargs):
        """
        :param language:
        :param n_shot_prompt:
        :param args:
        :param kwargs:
        """
        super(SearcherPrompt, self).__init__(language,n_shot_prompt,enable_rewrite,*args,**kwargs)
        memory_type = kwargs.get("memory", None)
        if memory_type is None:
            raise ValueError("memory should not be None type.")
        self.system_template=SEARCHER_SYSTEM_TEMPLATES_WIHT_REWRITE if enable_rewrite else SEARCHER_SYSTEM_TEMPLATES
        self._check_config()

    def build_prompt(self, input, *args, **kwargs):
        """
        :param input:
        :param args:
        :param kwargs:
        :return:
        """
        self._set_requirements()
        self.prompt = self.system_template+"\n\n"
        self.prompt += self.requirements+"\n\n"
        self.prompt += f"禁止输出无关内容，现在开始:\n输入问题:{input}\n输出:\n"
        return self.prompt

    def _set_requirements(self):
        self.requirements=SEARCHER_REQUIREMENTS

    def _check_config(self):
        """
        :return:
        """
        if self.prompt_language == "en":
            raise NotImplementedError



    def set_lang(self,language:str):
        self.prompt_language=language