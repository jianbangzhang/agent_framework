# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : base_agent.py
# Time       ：2024/8/25 16:49
# Author     ：jianbang
# version    ：python 3.10
# company    : IFLYTEK Co.,Ltd.
# emil       : whdx072018@foxmail.com
# Description：
"""

from src.agents.meta.meta_agent import MetaAgent


class BaseAgent(MetaAgent):
    agent_name = "BaseAgent"
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
        super(BaseAgent,self).__init__(agent_name,base_llm,stream_chat,**kwargs)
        self.agent_name=agent_name
        self.llm_model=base_llm
        self.stream_chat=stream_chat
        self.kwargs=kwargs

    def run(self,prompt_generator,*args,**kwargs):
        return self._run(prompt_generator,*args,**kwargs)


    def _run(self, prompt_generator,*args, **kwargs):
        language=kwargs.get("language","zh")
        if language=="zh" or language=="en":
            prompt_generator.set_lang(language)
        else:
            raise ValueError

        input_prompt=prompt_generator.build_prompt(self.agent_name,*args,**kwargs)
        output=self.llm_model.generate(input_prompt)
        return output

    def __repr__(self,*args, **kwargs):
        language = kwargs.get("language", "zh")
        info=f"LLM_Based:{self.llm_model.model_type}"
        info+=f"Prompt_language:{language}"
        return info

