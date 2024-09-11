# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : tool_config.py
# Time       ：2024/8/25 11:45
# Author     ：jianbang
# version    ：python 3.10
# company    : IFLYTEK Co.,Ltd.
# emil       : whdx072018@foxmail.com
# Description：
"""

from utils import singleton

@singleton
class ToolConfig:
    def __init__(self):
        self.tool_list=[
    {
        "api": "weather_info_api",
        "is_remote": True,
        "url": "http://XXXXX",
        "method": "post",
        "is_available": True
    }
]
