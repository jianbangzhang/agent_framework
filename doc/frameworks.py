# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : frameworks.py
# Time       ：2024/8/25 08:51
# Author     ：jianbang
# version    ：python 3.10
# company    : IFLYTEK Co.,Ltd.
# emil       : whdx072018@foxmail.com
# Description：
"""

class BaseAgent:
    def __init__(self):
        pass
    def chat(self):
        pass

    def generate_with_stream(self):
        # overwrite
        pass

    def generate_with_no_stream(self):
        # overwrite
        pass


class BaseModel:
    def __init__(self):
        pass



class BaseTool:
    def __init__(self):
        pass

