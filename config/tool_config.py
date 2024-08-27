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
        "api": "get_weather_info_api",
        "is_remote": True,
        "url": "http://172.31.205.27:32157/online-agent-demo/open/agent/query/weather",
        "method": "post",
        "is_available": True
    },
    {
        "api": "calendar_api",
        "is_remote": True,
        "url": "http://172.31.128.131:5000/api",
        "method": "post",
        "is_available": True
    },
    {
        "api": "get_bill_cost_in_month_api",
        "is_remote":True,
        "url":"http://172.31.205.27:32157/online-agent-demo/open/agent/getBillCostInMonthApi",
        "method":"post",
        "is_available": True
    },
    {
        "api": "get_subscribe_service_api",
        "is_remote":True,
        "url":"http://172.31.205.27:32157/online-agent-demo/open/agent/getSubscribeServiceApi",
        "method":"post",
        "is_available": True
    },
    {
        "api": "get_flow_info_api",
        "is_remote":True,
        "url":"http://172.31.205.27:32157/online-agent-demo/open/agent/getFlowInfoApi",
        "method":"post",
        "is_available": True
    },
    {
        "api": "points_info_api",
        "is_remote": True,
        "url": "http://172.31.205.27:32157/online-agent-demo/open/agent/pointsInfoApi",
        "method": "post",
        "is_available": True
    },
    {
        "api": "calculator_api",
        "is_remote": True,
        "url": "http://172.31.205.27:32157/online-agent-demo/open/agent/calculator",
        "method": "post",
        "is_available": True
    },
    {
        "api": "get_fee_balance_api",
        "is_remote":True,
        "url":"http://172.31.205.27:32157/online-agent-demo/open/agent/fee",
        "method":"post",
        "is_available": True
    },
    {
        "api": "get_pay_history_api",
        "is_remote":True,
        "url":"http://172.31.205.27:32157/online-agent-demo/open/agent/query/recharge",
        "method":"post",
        "is_available": True
    },
    {
        "api": "knowledge_retrieval_api",
        "is_remote":True,
        "url":"http://172.31.205.27:32157/online-agent-demo/open/agent/query/Knowledge",
        "method":"post",
        "is_available": True
    },
    {
        "api": "visualization_api",
        "is_remote":False,
        "url":None,
        "method":None,
        "is_available": True
    },
    {
        "api": "global_connection_traval_api",
        "is_remote": True,
        "url": None,
        "method": "post",
        "is_available": False
    },
    {
        "api": "global_connection_zone_api",
        "is_remote": True,
        "url": None,
        "method": "post",
        "is_available": False
    },
    {
        "api": "pay_living_expenses_api",
        "is_remote": True,
        "url": None,
        "method": "post",
        "is_available": False
    },
    {
        "api": "get_living_balance_info_api",
        "is_remote": True,
        "url": None,
        "method": "post",
        "is_available": False
    },
    {
        "api": "open_living_expenses_info_api",
        "is_remote": True,
        "url": None,
        "method": "post",
        "is_available": False
    },
    {
        "api": "multimedia_content_search_api",
        "is_remote": True,
        "url": None,
        "method": "post",
        "is_available": False
    },
    {
        "api": "multimedia_rank_search_api",
        "is_remote": True,
        "url": None,
        "method": "post",
        "is_available": False
    },
    {
        "api": "movie_ticket_api",
        "is_remote": True,
        "url": None,
        "method": "post",
        "is_available": False
    },
    {
        "api": "cinema_find_api",
        "is_remote": True,
        "url": None,
        "method": "post",
        "is_available": False
    },
    {
        "api":"complex_visualization_api",
        "is_remote":True,
        "is_available": True
    }
]
