# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : gpt.py
# Time       ：2024/8/25 09:11
# Author     ：jianbang
# version    ：python 3.10
# company    : IFLYTEK Co.,Ltd.
# emil       : whdx072018@foxmail.com
# Description：
"""
from base_model import BaseModel
import openai



class ChatGPT(BaseModel):
    def __init__(self,model_type,is_remote_llm,model_config,*args,**kwargs):
        """
        :param model_type:
        :param model_name:
        :param is_remote_llm:
        :param model_config:
        :param args:
        :param kwargs:
        """
        super(ChatGPT, self).__init__(model_type,is_remote_llm,model_config,*args,**kwargs)
        self._check_config()


    def _call_openai(model_engine, prompt,max_token,*args,**kwargs):
        """
        :param prompt:
        :param max_token:
        :param args:
        :param kwargs:
        :return:
        """
        response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=max_token
        )
        return response.choices[0].text.strip()

    def _generate(self,model_name, prompt,max_token,*args,**kwargs):
        raise self._call_openai(model_name, prompt,max_token,*args,**kwargs)


    def _check_config(self,*args,**kwargs):
        if self.model_type=="chatgpt" and not self.is_remote_llm:
            raise ValueError("Chatgpt can't be deploied locally!")


    def __repr__(self):
        info = "This is gpt model."
        return info
