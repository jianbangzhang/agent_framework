# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : agent_system.py
# Time       ：2024/8/25 12:22
# Author     ：jianbang
# version    ：python 3.10
# company    : IFLYTEK Co.,Ltd.
# emil       : whdx072018@foxmail.com
# Description：
"""

from abc import ABC,abstractmethod
from src.agents import AgentFactory
from src.prompt import LLM_Prompt
from src.memory import MemoryFactory
from src.tools import BaseTool
from src.action import Action


class Pipeline(ABC):
    def __init__(self,*args,**kwargs):
        self.agent_container=dict()
        self.result=None
        self.msg="[Running Info]:\n"

    @abstractmethod
    def _init(self,*args,**kwargs):
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



class AgentPipeline(Pipeline):
    def __init__(self,config,*args,**kwargs):
        """
        :param config:
        :param args:
        :param kwargs:
        """
        super(AgentPipeline,self).__init__(*args,**kwargs)
        self.system_type=config.system_type
        self.enable_multi_turns=config.enable_multi_turns
        self.has_memory = config.has_memory
        self.memory_type = config.memory_type
        self.n_shot_prompt = config.n_shot_prompt
        self.language = config.language
        self.retrieval_technique = config.retrieval_technique
        detailed_config=config.detailed_config
        self.agent_type=detailed_config.agent_type
        self.num_agents=detailed_config.num_agents
        self.is_stream=detailed_config.is_stream
        self.is_remote_llm=detailed_config.is_remote_llm
        self.llm_based=detailed_config.llm_based
        self.llm_model_type=detailed_config.llm_model_type
        self.llm_model_path_or_name=detailed_config.llm_model_path_or_name
        self.top_p=detailed_config.top_p
        self.top_k=detailed_config.top_k
        self.temperature=detailed_config.temperature
        self.is_remote_call=detailed_config.is_remote_call
        self.enable_call_tool_for_check=detailed_config.enable_call_tool_for_check


    def _init(self, *args, **kwargs):
        self._setup_agents(*args, **kwargs)
        self._setup_prompt_generator(*args,**kwargs)
        self._setup_tool_and_action(*args,**kwargs)
        self._setup_momery(*args,**kwargs)


    def _setup_agents(self, *args, **kwargs):
        agent_factory=AgentFactory()
        self.msg=f"[build agent]:"
        for i,(agent_name,base_llm,stream_chat) in enumerate(zip(self.agent_type,self.llm_model_type,self.is_stream)):
            info=f"build {agent_name} agent."
            self.msg+="\n\t"+info
            print(info)
            agent_obj=agent_factory.build_agent(agent_name,base_llm,stream_chat)
            self.agent_container[agent_name]=agent_obj

    def _setup_prompt_generator(self, *args, **kwargs):
        self.prompt_generator_obj=LLM_Prompt(*args,**kwargs)

    def _setup_tool_and_action(self, *args, **kwargs):
        self.tool_obj=BaseTool()
        self.action_obj=Action(*args,**kwargs)


    def _setup_momery(self, *args, **kwargs):
        self.memory_obj=MemoryFactory(*args,**kwargs)


    def run(self,user_question,*args, **kwargs):
        self._process(user_question,*args, **kwargs)
        return self.result


    def _process(self,user_question,*args, **kwargs):
        self._init(*args, **kwargs)
        if self.system_type=="multi_agents":
            assert len(self.agent_container)==3,"Multi-agent system must has 3 agents."
            self.result=self._process_multi_agents(user_question,*args, **kwargs)

        elif self.system_type=="single_agent":
            assert len(self.agent_container) == 1, "Single-agent system must has 1 agent."
            self.result=self._process_single_agent(user_question,*args, **kwargs)
        else:
            raise NotImplementedError


    def _process_multi_agents(self,user_question,*args, **kwargs):
        agent_names=["executor","refiner","searcher"]
        executor_agent=self.agent_container[agent_names[0]]
        refiner_agent=self.agent_container[agent_names[1]]
        searcher_agent=self.agent_container[agent_names[2]]

        history=[]
        is_finish=False
        n_shot_examples=searcher_agent.retrieve_from_memory(user_question,*args,**kwargs)
        init_prompt=self.prompt_generator_obj.init_prompt(n_shot_examples)
        history.append(init_prompt)
        while not is_finish:
            llm_out=executor_agent.run(init_prompt)
            history.append(llm_out)

            api,param=self.action_obj.parse(llm_out,*args,**kwargs)
            if param is None:
                is_finish=True
            else:
                is_finish=False

        reflexion=refiner_agent.run(history)
        refiner_agent.save(reflexion)
        return "\n".join(history)




    def _process_single_agent(self,*args, **kwargs):
        agent_names = ["executor"]
        executor_agent = self.agent_container[agent_names[0]]

        history = []
        is_finish = False
        init_prompt = self.prompt_generator_obj.init_prompt()
        history.append(init_prompt)
        while not is_finish:
            llm_out = executor_agent.run(init_prompt)
            history.append(llm_out)

            api, param = self.action_obj.parse(llm_out, *args, **kwargs)
            if param is None:
                is_finish = True
            else:
                is_finish = False

        return "\n".join(history)


    def __repr__(self):
        return self.msg







