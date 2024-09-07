# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : env_config.py
# Time       ：2024/8/25 09:02
# Author     ：jianbang
# version    ：python 3.10
# company    : IFLYTEK Co.,Ltd.
# emil       : whdx072018@foxmail.com
# Description：
"""
import os


current_file_path = os.path.abspath(__file__)
root_folder_path = os.path.dirname(os.path.dirname(current_file_path))


class EnvironmentConfig:
    api_key="XXXX"
    is_multi_turns="true"
    info=f"Set environment varibles:\n\tAPI_KEY:{api_key}\n\tEnableMultiTurns:{is_multi_turns}\n\tProjectPath:{root_folder_path}\n"
    os.environ["api_key"]=api_key
    os.environ["enable_multi_turns"]='true'
    os.environ["project_path"]=root_folder_path


