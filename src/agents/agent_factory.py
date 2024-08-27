# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : agent_factory.py
# Time       ：2024/8/25 20:35
# Author     ：jianbang
# version    ：python 3.10
# company    : IFLYTEK Co.,Ltd.
# emil       : whdx072018@foxmail.com
# Description：
"""
from .executor_agent import ExecutorAgent
from .refiner_agent import RefinerAgent
from .searcher_agent import SearchAgent


class AgentFactory(object):
    def __init__(self):
        pass

    def build_agent(self,agent_name,base_llm,stream_chat):
        if agent_name=="executor":
            agent=ExecutorAgent(agent_name,
                                 base_llm,
                                 stream_chat)
        elif agent_name=="refiner":
            agent=RefinerAgent(agent_name,
                                 base_llm,
                                 stream_chat)
        elif agent_name=="searcher":
            agent=SearchAgent(agent_name,
                                 base_llm,
                                 stream_chat)
        else:
            raise NotImplementedError
        return agent

