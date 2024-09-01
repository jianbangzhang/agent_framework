# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : searcher_agent.py
# Time       ：2024/8/25 20:40
# Author     ：jianbang
# version    ：python 3.10
# company    : IFLYTEK Co.,Ltd.
# emil       : whdx072018@foxmail.com
# Description：
"""

from src.agents.meta.base_agent import BaseAgent



class SearchAgent(BaseAgent):
    def __init__(self,
                 agent_type,
                 llm,
                 stream_chat,
                 **kwargs):
        super(SearchAgent,self).__init__(agent_type,llm,stream_chat,**kwargs)
        self.agent_name="searcher"


