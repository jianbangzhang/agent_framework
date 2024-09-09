# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : single_prompt.py
# Time       ：2024/9/1 09:30
# Author     ：jianbang
# version    ：python 3.10
# company    : IFLYTEK Co.,Ltd.
# emil       : whdx072018@foxmail.com
# Description：
"""

from src.prompt.meta.llm_prompt import LLMPrompt
from src.prompt.meta.constants import (SINGLE_SYSTEM_TEMPLATES,
                                       SINGLE_REQUIREMENTS)


class SinglePrompt(LLMPrompt):
    def __init__(self, language, n_shot_prompt, enable_rewrite, *args, **kwargs):
        """
        :param language:
        :param n_shot_prompt:
        :param args:
        :param kwargs:
        """
        super(SinglePrompt, self).__init__(language, n_shot_prompt, enable_rewrite, *args, **kwargs)
        self.system_template = SINGLE_SYSTEM_TEMPLATES
        self.tool_text = kwargs.get("tool")
        self._check_config()

    def build_prompt(self, inputs, *args, **kwargs):
        """
        :param agent_name:
        :param inputs:
        :param args:
        :param kwargs:
        :return:
        """
        self._set_requirements()
        self.prompt = self.system_template + "\n\n"
        self.prompt += self.tool_text + "\n\n"
        self.prompt += self.requirements + "\n\n"
        self.prompt += self.examples + "\n\n" if self.examples is not None else ""
        self.prompt += f"禁止输出无关内容，现在开始：\n输入用户问题：{inputs}\n输出：\n"
        return self.prompt

    def _set_requirements(self):
        self.requirements = SINGLE_REQUIREMENTS


    def _check_config(self):
        """
        :return:
        """
        if self.prompt_language == "en":
            raise NotImplementedError
        if self.n_shot_examples != 1:
            raise ValueError

    def set_lang(self,language:str):
        self.prompt_language=language