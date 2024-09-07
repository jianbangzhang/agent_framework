# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : momery_factory.py
# Time       ：2024/9/1 09:38
# Author     ：jianbang
# version    ：python 3.10
# company    : IFLYTEK Co.,Ltd.
# emil       : whdx072018@foxmail.com
# Description：
"""

from .prompt_types import (ExecuatorPrompt,
                           RefinerPrompt,
                           SearcherPrompt,
                           SinglePrompt)


class PromptFactory(object):
    def __init__(self,memory_obj,language,n_shot_prompt,enable_rewrite,*args,**kwargs):
        self.memory_obj=memory_obj
        self.language=language
        self.n_shot_prompt=n_shot_prompt
        self.enable_rewrite=enable_rewrite
        self.prompt=None

    def generate_prompt(self,agent_name,input,retrieve_content=None,*args,**kwargs):
        """
        :param agent_name:
        :param input:
        :return:
        """
        if agent_name=="executor" and retrieve_content is None:
            raise ValueError

        if agent_name=="refiner" and self.memory_obj is None:
            raise ValueError

        self.build_prompt(agent_name,input,retrieve_content,*args,**kwargs)
        return self.prompt


    def build_prompt(self,agent_name,input,retrieve_content=None,*args,**kwargs):
        """
        :param agent_name:
        :return:
        """
        if agent_name == "executor":
            agent_obj=ExecuatorPrompt(self.language,self.n_shot_prompt,self.enable_rewrite,*args,**kwargs)
            self.prompt=agent_obj.build_prompt(input,retrieve_content=retrieve_content)
        elif agent_name == "searcher":
            agent_obj=SearcherPrompt(self.language,self.n_shot_prompt,self.enable_rewrite,*args,**kwargs)
            self.prompt = agent_obj.build_prompt(input)
        elif agent_name == "refiner":
            agent_obj=RefinerPrompt(self.language,self.n_shot_prompt,self.enable_rewrite,*args,**kwargs)
            self.prompt = agent_obj.build_prompt(input,memory=self.memory_obj)
        elif agent_name == "single":
            agent_obj=SinglePrompt(self.language,self.n_shot_prompt,self.enable_rewrite,*args,**kwargs)
            self.prompt = agent_obj.build_prompt(input)
        else:
            raise NotImplementedError

    def set_lang(self,language):
        """
        :param language:
        :return:
        """
        self.prompt.set_lang(language)



