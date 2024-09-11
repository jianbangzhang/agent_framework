# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : base.py
# Time       ：2024/9/9 18:47
# Author     ：jianbang
# version    ：python 3.10
# company    : IFLYTEK Co.,Ltd.
# emil       : whdx072018@foxmail.com
# Description：
"""
from abc import ABC,abstractmethod
from config.tool_config import ToolConfig


class Pipeline(ABC):
    def __init__(self,*args,**kwargs):
        self.agent_container=dict()
        self.tool_config=ToolConfig()
        self.splitter="\n"
        self.msg="[Running Info]:"+self.splitter

    @property
    def get_apis(self):
        return [data_dict["api"] for data_dict in self.tool_config.tool_list]

    @abstractmethod
    def _init(self,*args,**kwargs):
        raise NotImplementedError

    @abstractmethod
    def _setup_llm_model(self,*args,**kwargs):
        raise NotImplementedError

    @abstractmethod
    def _setup_agents(self,*args,**kwargs):
        raise NotImplementedError

    @abstractmethod
    def _setup_prompt_generator(self,*args,**kwargs):
        raise NotImplementedError

    @abstractmethod
    def _setup_tool_and_action(self,*args,**kwargs):
        raise NotImplementedError

    @abstractmethod
    def _setup_momery(self,*args,**kwargs):
        raise NotImplementedError

    def run(self,*args,**kwargs):
        return self._process(*args,**kwargs)

    @abstractmethod
    def _process(self,*args,**kwargs):
        raise NotImplementedError

    @abstractmethod
    def __repr__(self):
        raise NotImplementedError