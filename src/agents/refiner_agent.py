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
    def __init__(self,
                 agent_type,
                 llm,
                 stream_chat,
                 **kwargs):
        super(RefinerAgent,self).__init__(agent_type,llm,stream_chat,**kwargs)
        self.agent_name = "refiner"

    def save2memory(self,user_question,content,memory):
        """
        :param content:
        :param memory:
        :param kwargs:
        :return:
        """
        if memory is None:
            raise ValueError
        memory.save(user_question,content)

