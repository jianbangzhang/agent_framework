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
from .llm_prompt import LLMPrompt
from .constants import REFINER_SYSTEM_TEMPLATES


class RefinerPrompt(LLMPrompt):
    def __init__(self,*args,**kwargs):
        super(RefinerPrompt, self).__init__(*args,**kwargs)
        self.system_template=REFINER_SYSTEM_TEMPLATES


    def build_prompt(self,agent_name,input, *args, **kwargs):
        pass