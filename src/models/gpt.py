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
from .base_model import BaseModel
import openai
import os



class ChatGPT(BaseModel):
    def __init__(self, model_type, is_remote_llm, model_config, *args, **kwargs):
        """
        :param model_type:
        :param model_name:
        :param is_remote_llm:
        :param model_config:
        :param args:
        :param kwargs:
        """
        super(ChatGPT, self).__init__(model_type, is_remote_llm, model_config, *args, **kwargs)
        openai.api_key = os.environ.get("api_key")
        self._check_config()

    def _call_openai(self, model_engine, prompt, max_token, *args, **kwargs):
        """
        :param prompt:
        :param max_token:
        :param args:
        :param kwargs:
        :return:
        """
        temperature = self.model_config["temperature"]
        top_p = self.model_config["top_p"]

        response = openai.ChatCompletion.create(
            model=model_engine,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_token,
            temperature=temperature,
            top_p=top_p
        )

        answer = response.choices[0].message['content'].strip()
        return answer

    def _generate(self, model_name, prompt, max_token, *args, **kwargs):
        return self._call_openai(model_name, prompt, max_token, *args, **kwargs)

    def _check_config(self, *args, **kwargs):
        if self.model_type == "chatgpt" and not self.is_remote_llm:
            raise ValueError("Chatgpt can't be deployed locally!")

    def __repr__(self):
        info = "This is gpt model."
        return info