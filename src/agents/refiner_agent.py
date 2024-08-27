# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : refiner_agent.py
# Time       ：2024/8/25 20:39
# Author     ：jianbang
# version    ：python 3.10
# company    : IFLYTEK Co.,Ltd.
# emil       : whdx072018@foxmail.com
# Description：
"""

from src.agents.meta.base_agent import BaseAgent



class RefinerAgent(BaseAgent):
    model_name="refiner"
    def __init__(self,
                 agent_type,
                 llm,
                 stream_chat,
                 **kwargs):
        super(RefinerAgent,self).__init__(agent_type,llm,stream_chat,**kwargs)


    def save2memory(self,content,**kwargs):
        memory=kwargs.get("memory",None)
        if memory is None:
            raise ValueError
        memory.update(content)