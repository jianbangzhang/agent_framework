# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : executor_agent.py
# Time       ：2024/8/25 17:48
# Author     ：jianbang
# version    ：python 3.10
# company    : IFLYTEK Co.,Ltd.
# emil       : whdx072018@foxmail.com
# Description：
"""
from src.agents.meta.base_agent import BaseAgent



class ExecutorAgent(BaseAgent):
    def __init__(self,
                 agent_name,
                 base_llm,
                 stream_chat,
                 **kwargs):
        super(ExecutorAgent,self).__init__(agent_name,base_llm,stream_chat,**kwargs)
        self.agent_name="executor"







