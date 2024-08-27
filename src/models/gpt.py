# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : gpt.py
# Time       ：2024/8/25 09:11
# Author     ：jianbang
# version    ：python 3.10
# company    : IFLYTEK Co.,Ltd.
# emil       : whdx072018@foxmail.com
# Description：
"""
import openai


def call_openai(model_engine, prompt):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=4096
    )
    return response.choices[0].text.strip()