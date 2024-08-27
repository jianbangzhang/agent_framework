# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : meta_agent.py
# Time       ：2024/8/25 16:23
# Author     ：jianbang
# version    ：python 3.10
# company    : IFLYTEK Co.,Ltd.
# emil       : whdx072018@foxmail.com
# Description：
"""
from abc import ABC, abstractmethod
from typing import Iterator, Union



class MetaAgent(ABC):
    agent_name="MetaAgent"
    def __init__(self,
                 agent_name,
                 base_llm,
                 stream_chat,
                 **kwargs):
        """
        :param agent_name:
        :param base_llm:
        :param stream_chat:
        :param prompt_generator:
        :param kwargs:
        """
        self.agent_type=agent_name
        self.base_llm=base_llm
        self.stream_chat=stream_chat
        self.kwargs=kwargs

    def run(self,*args,**kwargs):
        return self._run(*args,**kwargs)


    @abstractmethod
    def _run(self, *args, **kwargs) -> Union[str, Iterator[str]]:
        raise NotImplementedError


    @abstractmethod
    def __repr__(self):
        raise NotImplementedError
