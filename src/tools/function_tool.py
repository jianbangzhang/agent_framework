# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : function_tool.py
# Time       ：2024/8/25 22:13
# Author     ：jianbang
# version    ：python 3.10
# company    : IFLYTEK Co.,Ltd.
# emil       : whdx072018@foxmail.com
# Description：
"""

from .tool import BaseTool
from utils import retry
import requests
from typing import Dict,Tuple,Union
import os


class CinemaFindTool(BaseTool):
    name = "cinema_find_api"
    is_remote=True
    description="这是一个电影院搜索工具"

    def __call__(self,place, *args, **kwargs)->Tuple:
        date_dict,code=self._call_actual_api(place)
        return date_dict,code

    @retry(max_retry=1, delay=0)
    def _call_actual_api(self,place)->Union[Dict,None]:
        authCode = os.environ.get("authCode")
        post_url = "http://172.31.205.27:32157/online-agent-tool/open/agent/multimedia/cinema"
        data = {
            "sdkAppKey": "zgydApp",
            "authCode": authCode,
            "place":place
        }

        response = requests.post(post_url, json=data)

        if response.status_code == 200:
            result = response.json()['data']
            if not result:
                return {"result": "非常抱歉，未查到电影院搜索相关内容"}
            return result
        else:
            return {"result": "非常抱歉，网络异常，电影院搜索暂时无法查询"}