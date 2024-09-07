# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : app.py
# Time       ：2024/8/25 08:48
# Author     ：jianbang
# version    ：python 3.10
# company    : IFLYTEK Co.,Ltd.
# emil       : whdx072018@foxmail.com
# Description：
"""
import os

from config import EnvironmentConfig
from config import AgentSystemConfig
from src.pipeline import AgentPipeline
from logger import AutoLevelLogger
from utils import print_args,print_env






def run_agent(user_question):
    """
    :param user_question:
    :return:
    """
    env_config_info=EnvironmentConfig.info
    logger = AutoLevelLogger()

    env_info=print_env(env_config_info)
    logger.log(env_info)

    enable_multi_turns=os.getenv("enable_multi_turns")
    config=AgentSystemConfig(enable_multi_turns=enable_multi_turns)
    config_info=print_args(config)
    logger.log(config_info)

    agent_pipeline=AgentPipeline(config)
    final_answer=agent_pipeline.run(user_question)
    running_info=agent_pipeline.__repr__()
    logger.log(running_info)
    return final_answer










if __name__ == '__main__':
    api_key = "XXXXXXXX"
    os.environ['api_key'] = api_key
    user_question="武汉的天气"
    answer=run_agent(user_question)
    print(answer)