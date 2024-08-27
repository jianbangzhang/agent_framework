# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test_env_config.py
# Time       ：2024/8/25 09:15
# Author     ：jianbang
# version    ：python 3.10
# company    : IFLYTEK Co.,Ltd.
# emil       : whdx072018@foxmail.com
# Description：
"""
import os
from config import EnvironmentConfig



print(EnvironmentConfig.info)
print(os.getenv("api_key"))
print(os.getenv("is_multi_turns"))