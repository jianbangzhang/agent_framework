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
    model_name="searcher"
    def __init__(self,
                 agent_type,
                 llm,
                 stream_chat,
                 **kwargs):
        super(SearchAgent,self).__init__(agent_type,llm,stream_chat,**kwargs)
        self.memory=kwargs.get("memory",None)
        if self.memory is None:
            raise ModuleNotFoundError

    def run(self, prompt_generator, *args, **kwargs):
        return self._run(prompt_generator, *args, **kwargs)

    def _run(self, prompt_generator, *args, **kwargs):
        input_question = kwargs.get("user_question",None)
        if input_question is None:
            raise ValueError
        output = self.memory.query(input_question,*args, **kwargs)
        return output

    def retrieve_from_memory(self, input_question,*args, **kwargs):
        n_shot=self.memory.query(input_question)
        return n_shot

