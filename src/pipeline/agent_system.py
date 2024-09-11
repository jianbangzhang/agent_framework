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
from src.agents import AgentFactory
from src.prompt import PromptFactory
from src.memory import MemoryFactory
from src.tools import BaseTool
from src.action import Action
from src.models import ModelFactory
from utils import retry
from .base import Pipeline



class AgentPipeline(Pipeline):
    def __init__(self,config,*args,**kwargs):
        """
        :param config:
        :param args:
        :param kwargs:
        """
        super(AgentPipeline,self).__init__(*args,**kwargs)
        self.system_type= config.system_type
        self.enable_multi_turns=config.enable_multi_turns
        self.has_memory = config.has_memory
        self.memory_type = config.memory_type
        self.memory_size = config.memory_size
        self.retrieval_technique = config.retrieval_technique
        self.n_shot_prompt = config.n_shot_prompt
        self.language = config.language
        self.enable_rewrite= config.enable_rewrite
        detailed_config= config.detailed_config
        self.agent_type=detailed_config.agent_type
        self.num_agents=detailed_config.num_agents
        self.is_stream=detailed_config.is_stream
        self.is_remote_llm=detailed_config.is_remote_llm
        self.llm_model_type=detailed_config.llm_model_type
        self.llm_model_path_or_name=detailed_config.llm_model_path_or_name
        self.top_p=detailed_config.top_p
        self.temperature=detailed_config.temperature
        self.max_token = detailed_config.max_token
        self.is_remote_call=detailed_config.is_remote_call
        self.enable_call_tool_for_check=detailed_config.enable_call_tool_for_check


    def _init(self, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        :return:
        """
        self._setup_llm_model(*args, **kwargs)
        self._setup_agents(*args, **kwargs)
        self._setup_prompt_generator(*args,**kwargs)
        self._setup_tool_and_action(*args,**kwargs)
        self._setup_momery(*args,**kwargs)

    def _setup_llm_model(self,*args,**kwargs):
        """
        :param args:
        :param kwargs:
        :return:
        """
        self.msg = "[build model instance]:"+self.splitter
        model_config={"top_p":self.top_p,
                      "temperature":self.temperature}
        self.llm_model=ModelFactory(self.llm_model_type,self.is_remote_llm,model_config)


    def _setup_agents(self, *args, **kwargs):
        agent_factory=AgentFactory()
        self.msg="[build agent instance]:"+self.splitter
        for i,(agent_name,model_path_or_name,model_type,stream_chat) in enumerate(zip(self.agent_type,self.llm_model_path_or_name,self.llm_model_type,self.is_stream)):
            info=f"build {agent_name} agent."
            self.msg+=info+self.splitter
            print(info)
            agent_obj=agent_factory.build_agent(agent_name,self.llm_model,stream_chat)
            self.agent_container[agent_name]=agent_obj

    def _setup_prompt_generator(self, *args, **kwargs):
        self.msg+="[build prompt generator instance]:"+self.splitter
        self.prompt_generator_obj=PromptFactory(self.memory_type,self.language,self.n_shot_prompt,self.enable_rewrite,*args,**kwargs)

    def _setup_tool_and_action(self, *args, **kwargs):
        self.msg += "[build tool and action instance]:"+self.splitter
        self.tool_obj=BaseTool()
        self.action_obj=Action(*args,**kwargs)


    def _setup_momery(self, *args, **kwargs):
        self.msg += "[build prompt generator instance]:"+self.splitter
        self.memory_obj=MemoryFactory(*args,**kwargs)
        self.memory_obj.build_memory(self.memory_type,self.memory_size,self.retrieval_technique,self.n_shot_prompt)


    def run(self,user_question,*args, **kwargs):
        """
        :param user_question:
        :param args:
        :param kwargs:
        :return:
        """
        result=self._process(user_question,*args, **kwargs)
        return result


    def _process(self,user_question,*args, **kwargs):
        """
        :param user_question:
        :param args:
        :param kwargs:
        :return:
        """
        self._init(*args, **kwargs)
        self.msg+="all object is successfully instance!"+self.splitter
        self.msg += f"[Processing {self.system_type}]"+self.splitter

        if self.system_type=="multi_agents":
            assert len(self.agent_container)==3,"Multi-agent system must has 3 agents."
            result=self._process_multi_agents(user_question,*args, **kwargs)

        elif self.system_type=="single_agent":
            assert len(self.agent_container) == 1, "Single-agent system must has 1 agent."
            result=self._process_single_agent(user_question,*args, **kwargs)
        else:
            raise NotImplementedError

        return result


    def _agent_output(self,agent_obj,prompt,model_type,model_name):
        """
        :param agent_obj:
        :param prompt_generator_obj:
        :param llm_input:
        :param model_name:
        :param max_token:
        :return: prompt_generator,input_prompt=input_prompt,memory=memory
        """
        output=agent_obj.run(prompt,model_type,model_name,self.max_token)
        return output

    @retry(max_retry=1, delay=0)
    def _get_examples(self,user_question,searcher_agent,searcher_base_model,model_name,*args, **kwargs):
        """
        :param user_question:
        :param searcher_agent:
        :param searcher_base_model:
        :param model_name:
        :param args:
        :param kwargs:
        :return:
        """
        def get_answer(input_text):
            if "Observation" in input_text or "Finish" not in input_text:
                answer=""
                code=-1
            elif "Thought" in input_text and "Finish" in input_text:
                answer_lst=[line.replace("Finish:","").strip() for line in input_text.split("\n") if "Finish:" in line]
                answer=answer_lst[0]
                code=0
                if "reflection" not in answer:
                    code=-1
            else:
                answer=input_text
                code=0
            return answer,code
        try:
            history=[]
            init_prompt = self.prompt_generator_obj.generate_prompt(searcher_agent.agent_name, user_question,memory=self.memory_obj)
            search_agent_output=self._agent_output(searcher_agent,init_prompt,searcher_base_model,model_name)
            history.append(init_prompt)
            history.append(search_agent_output)

            api, param = self.action_obj.parse(search_agent_output, *args, **kwargs)
            observation_value,code = self.tool_obj.execute(api, **param,memory=self.memory_obj)
            observation = f"Observation: {observation_value}"
            history.append(observation)

            search_agent_input="\n".join(history)
            search_agent_finish=self._agent_output(searcher_agent,search_agent_input,searcher_base_model,model_name)
            answer,code=get_answer(search_agent_finish)
            answer=answer if code==0 else observation_value
            self.msg+=f"{self.splitter}{self.splitter}[Search Agent]:{self.splitter}"+self.splitter.join(history)+f"\n{answer}"
        except:
            answer = self.tool_obj.execute("retrieve_memory_api", user_question=user_question, memory=self.memory_obj)
        return answer


    def _process_multi_agents(self,user_question,tool_lst=None,*args, **kwargs):
        """
        :param user_question:
        :param tool_lst:
        :param args:
        :param kwargs:
        :return:
        """
        agent_names=["executor","refiner","searcher"]
        model_types=self.llm_model_type
        model_names=self.llm_model_path_or_name

        executor_agent=self.agent_container[agent_names[0]]
        executor_base_llm=model_types[0]
        executor_model_name=model_names[0]
        refiner_agent=self.agent_container[agent_names[1]]
        refiner_base_model=model_types[1]
        refiner_model_name=model_names[1]
        searcher_agent=self.agent_container[agent_names[2]]
        searcher_base_model=model_types[2]
        searcher_model_name=model_names[2]

        history=[]
        is_finish=False
        tool_lst,code = self.tool_obj.execute("retrieve_api", user_question=user_question,observation=False) if tool_lst is None else tool_lst
        tool_text = self.splitter.join([f"{i + 1}.{tool}" for i, tool in enumerate(tool_lst)])
        n_shot_examples,code = self._get_examples(user_question,searcher_agent,searcher_base_model,searcher_model_name,*args, **kwargs)
        self.msg += f"{self.splitter}{self.splitter}[Retrieve]:{self.splitter}{n_shot_examples}"+self.splitter
        print(n_shot_examples)

        init_prompt=self.prompt_generator_obj.generate_prompt(executor_agent.agent_name,user_question,tool=tool_text,retrieve_content=n_shot_examples)
        llm_input=init_prompt
        history.append(init_prompt)
        max_rounds=2
        cur_rounds=0
        call_tools=[]

        while not is_finish and cur_rounds<=max_rounds:
            cur_rounds+=1
            llm_out=self._agent_output(executor_agent,llm_input,executor_base_llm,executor_model_name)
            history.append(llm_out)
            print(llm_out)

            api,param=self.action_obj.parse(llm_out,*args,**kwargs)
            if api is None and param is None:
                is_finish=True
            else:
                is_finish=False
                observation_value,code=self._get_observation(api, param)
                call_tools.append(api)
                observation=f"Observation: {observation_value}"
                print(observation)
                history.append(observation)
                llm_input = self.splitter.join(history)

        self.msg += f"{self.splitter}{self.splitter}[Executor Agent]:{self.splitter}" + self.splitter.join(history)
        history_text="## 对话：\nQuestion: "+user_question+"\n"+"\n".join(history[1:])
        call_tool_text="\n".join([api_tool for api in list(set(call_tools)) for api_tool in tool_lst if str(api) in str(api_tool)])
        refiner_prompt=f"## 工具:\n{call_tool_text}\n\n"+history_text
        refiner_llm_input = self.prompt_generator_obj.generate_prompt(refiner_agent.agent_name, refiner_prompt)
        reflexion=self._agent_output(refiner_agent,refiner_llm_input,refiner_base_model,refiner_model_name)
        refiner_agent.save2memory(user_question,reflexion,self.memory_obj)
        self.msg+=f"{self.splitter}{self.splitter}[Refine Agent]:{self.splitter}"+f"{refiner_llm_input}{self.splitter}{reflexion}"
        print(reflexion)
        return self.splitter.join(history)


    def _process_single_agent(self,user_question,tool_lst=None,*args, **kwargs):
        """
        :param user_question:
        :param tool_lst:
        :param args:
        :param kwargs:
        :return:
        """
        agent_names = ["executor"]
        prompt_type="single"
        executor_agent = self.agent_container[agent_names[0]]
        executor_base_llm=self.llm_model_path_or_name[0]
        model_type=self.llm_model_type[0]

        history = []
        is_finish = False
        tool_lst,_=self.tool_obj.execute("retrieve_api",user_question=user_question,observation=False) if tool_lst is None else tool_lst
        tool_text=self.splitter.join([f"{i+1}.{tool}" for i,tool in enumerate(tool_lst)])
        init_prompt = self.prompt_generator_obj.generate_prompt(prompt_type,user_question,tool=tool_text)
        llm_input=init_prompt
        history.append(init_prompt)
        max_rounds = 2
        cur_rounds = 0

        while not is_finish and cur_rounds <= max_rounds:
            cur_rounds += 1
            llm_out = self._agent_output(executor_agent,llm_input,model_type,executor_base_llm)
            self.msg += f"[agent output]:{self.splitter}{llm_out}"
            history.append(llm_out)
            print(llm_out)

            api, param = self.action_obj.parse(llm_out, *args, **kwargs)
            if api is None and param is None:
                is_finish = True
            else:
                is_finish = False
                observation_value,code = self._get_observation(api,param)
                observation = f"Observation: {observation_value}"
                print(observation)
                history.append(observation)
                llm_input = self.splitter.join(history)

        self.msg += f"{self.splitter}{self.splitter}[Single Agent]:{self.splitter}{self.splitter.join(history)}"
        return self.splitter.join(history)

    def _get_observation(self,api,param):
        if api in self.get_apis:
            res=self.tool_obj.execute(api, **param)
        else:
            res=self.tool_obj.execute("retrieve_api",api=api,param=param,observation=True)
        return res


    def __repr__(self):
        return self.msg







