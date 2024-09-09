# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : model_factory.py
# Time       ：2024/9/7 16:29
# Author     ：jianbang
# version    ：python 3.10
# company    : IFLYTEK Co.,Ltd.
# emil       : whdx072018@foxmail.com
# Description：
"""
from .qwen import QWen2Model
from .gpt import ChatGPT




class ModelFactory(object):
    def __init__(self,model_type,is_remote_llm,model_config,*args,**kwargs):
        """
        :param model_type:
        :param is_remote_llm:
        :param model_config:
        :param args:
        :param kwargs:
        """
        self._class_map ={
                "qwen": QWen2Model,
                "chatgpt": ChatGPT
        }
        self.model_type=model_type
        self.is_remote_llm=is_remote_llm
        self.model_config=model_config

    def _create_instance(self, class_name,*args,**kwargs):
        if class_name in self._class_map:
            child_model=self._class_map[class_name](self.model_type,self.is_remote_llm,self.model_config,*args,**kwargs)
            return child_model
        else:
            raise ValueError(f"Unknown class type: {class_name}")

    def generate(self,model_type,model_name, prompt,max_token,*args,**kwargs):
        """
        :param model_type:
        :param model_name:
        :param prompt:
        :param max_token:
        :param args:
        :param kwargs:
        :return:
        """

        submodel=self._create_instance(model_type)
        result=submodel.generate(model_name, prompt,max_token,*args,**kwargs)
        return result


