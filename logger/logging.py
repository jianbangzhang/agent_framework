# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : logging.py
# Time       ：2024/8/25 19:10
# Author     ：jianbang
# version    ：python 3.10
# company    : IFLYTEK Co.,Ltd.
# emil       : whdx072018@foxmail.com
# Description：
"""
import os
import datetime




class AutoLevelLogger:
    def __init__(self, file_name="run.log"):
        project_path=os.getenv("project_path")
        self.file_name = os.path.join(project_path,file_name)
        self.file = open(self.file_name, 'a')

    def log(self, message):
        level = self._determine_level(message)
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"{timestamp} - {level} - {message}\n"
        self.file.write(log_entry)
        self.file.flush()

    def _determine_level(self, message):
        patterns = {
            'DEBUG': ['debug', 'verbose'],
            'INFO': ['info', 'notice'],
            'WARNING': ['warning', 'warn'],
            'ERROR': ['error', 'exception', 'fail'],
            'CRITICAL': ['critical', 'fatal']
        }
        for level, keywords in patterns.items():
            if any(keyword in message.lower() for keyword in keywords):
                return level
        return 'INFO'

    def close(self):
        self.file.close()