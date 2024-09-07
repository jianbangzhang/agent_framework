# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : agents_config.py
# Time       ：2024/8/25 08:55
# Author     ：jianbang
# version    ：python 3.10
# company    : IFLYTEK Co.,Ltd.
# emil       : whdx072018@foxmail.com
# Description：
"""

class AgentSystemConfig:
    def __init__(self,system_type="single_agents",
                 enable_multi_turns=True,
                 has_memory=True,
                 memory_type="graph",
                 language="en",
                 n_shot=1):
        """
        :param system_type:
        :param enable_multi_turns:
        :param has_memory:
        :param memory_type: only when there is memory block,you can choose one element of list:["graph","natural"]
        :param language: you can choose Chinese(zh in brief) and English(en in brief)
        :param n_shot: when n_shot=0,prompt is zero-shot,otherwise few-shot prompt,this n is noted

        """
        self.system_type=system_type
        self.enable_multi_turns=enable_multi_turns
        self.detailed_config=MultiAgentSysConfig() if system_type=="multi_agents" else SingleAgentConfig()
        self.has_memory=has_memory
        self.memory_type=memory_type if has_memory else None
        self.n_shot_prompt=n_shot
        self.language=language
        # Todo
        self.enable_rewrite=False
        self.retrieval_technique=None



class MultiAgentSysConfig:
    def __init__(self):
        # agent config
        self.agent_type=["executor","refiner","searcher"]
        self.num_agents=3
        self.is_stream=[False,False,False]
        self.is_remote_llm=[True,True,True]

        # model config
        self.llm_model_type=["chatgpt","chatgpt","chatgpt"] #["qwen2","qwen2","qwen2"]
        self.llm_model_path_or_name=["gpt-3.5-turbo","gpt-3.5-turbo","gpt-3.5-turbo"] #["Qwen/Qwen2-7B-Instruct","Qwen/Qwen2-7B-Instruct","Qwen/Qwen2-7B-Instruct"]
        self.top_p=0
        self.top_k=1
        self.temperature=0
        self.max_token=4096

        # tool config
        self.is_remote_call=True

        # action config
        self.enable_call_tool_for_check=True




class SingleAgentConfig:
    def __init__(self):
        self.agent_type=["executor"]
        self.num_agents=1
        self.is_stream = [False]
        self.is_remote_llm = [True]

        # model config
        self.llm_based = [True]
        self.llm_model_type = ["chatgpt"]
        self.llm_model_path = ["gpt-3.5-turbo"]
        self.top_k = 1
        self.temperature = 0
        self.max_token = 4096

        # tool config
        self.is_remote_call = True

        # action config
        self.enable_call_tool_for_check = True













