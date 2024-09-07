# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : executor_prompt.py
# Time       ：2024/9/1 09:16
# Author     ：jianbang
# version    ：python 3.10
# company    : IFLYTEK Co.,Ltd.
# emil       : whdx072018@foxmail.com
# Description：
"""
from src.prompt.meta.llm_prompt import LLMPrompt
from src.prompt.meta.constants import (EXECUATOR_SYSTEM_TEMPLATES,
                                       EXECUATOR_EXAMPLES,
                                       EXECUATOR_REQUIREMENTS)


class ExecuatorPrompt(LLMPrompt):
    def __init__(self,language,n_shot_prompt,enable_rewrite,*args,**kwargs):
        """
        :param language:
        :param n_shot_prompt:
        :param args:
        :param kwargs:
        """
        super(ExecuatorPrompt, self).__init__(language,n_shot_prompt,enable_rewrite,*args,**kwargs)
        self.system_template=EXECUATOR_SYSTEM_TEMPLATES
        self._check_config()

    def build_prompt(self,input, *args, **kwargs):
        """
        :param agent_name:
        :param input:
        :param args:
        :param kwargs:
        :return:
        """
        content=kwargs.get("retrieve_content")
        self._set_requirements()
        self._set_examples(content)
        self.prompt=self.system_template+"\n"
        self.prompt+=self.requirements+"\n"
        self.prompt+=self.examples+"\n"
        self.prompt+=f"现在开始：\n输入用户问题：{input}\n输出：\n"


    def _set_requirements(self):
        """
        :return:
        """
        self.requirements=EXECUATOR_REQUIREMENTS

    def _set_examples(self,content):
        """
        :param content:
        :return:
        """
        if content is None:
            self.examples = EXECUATOR_EXAMPLES
        else:
            self.examples=EXECUATOR_EXAMPLES+"\n"+content


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