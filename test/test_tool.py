# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test_tool.py
# Time       ：2024/8/25 22:10
# Author     ：jianbang
# version    ：python 3.10
# company    : IFLYTEK Co.,Ltd.
# emil       : whdx072018@foxmail.com
# Description：
"""

from src.tools import BaseTool
import os


code_lst=['sTlyjKgLdaIJ-Sfo6K6F9bHq69-kLbRPIDp7aMJQeP94u8JNtiwPxEtzW7ZNRHW0', '7LzDqHpCCCkxUOFEGjGhzCxYRduQFSjcpKFGAsruOkuvCLdGBRCLf8g7E74FQzVA', 'u_F8xtDm1dTXRMQlF20z_FyoIo1VIezISM4InvpkTN8qn-ckIb0NFGo3qsSb269N', 'Z3UiLcBHgfQY_ysC99jxW-m2T5VP-STUf6kRHYiOY1KhUHNAwIaQ-TZgaljtQ_or', 'JOR-vpdF7Uc2OtsjQYk8XH8T-qSovio8Ky6UDS1Gyal9C0pLTrSfRm2rSSsjUTYX', 'jOgB3cMiwvZNEiOpC4ByWCqtBTO3szKjEZVF6Af9djSaPO2JPOmpxooLswxfmVxo', 'aWdgnRYw_YRkeoUlwhp5cZXUpLU8yR18QE-BKApgK_QCBKJ5gephVfgS7cL0ltqQ', 'G8Q0tt7iUnLveCdvr2N7bVqRI9Fyvb3WJrQCzQft2rc6d6wcuBNOh1SkOM_F3ClX']


tools_and_developers={"get_weather_info_api":"周刚",
        "calendar_api":"昊晖",
        "get_bill_cost_in_month_api":"方岩",
        "get_subscribe_service_api":"方岩",
        "get_flow_info_api":"方岩",
        "points_info_api":"方岩",
        "calculator_api":"守法",
        "get_fee_balance_api":"守法",
        "get_pay_history_api":"昊晖",
        "knowledge_retrieval_api":"胡浩",
        "visualization_api":"胡浩",
        "get_living_balance_info_api":"zoukun",
        "open_living_expenses_info_api":"zoukun",
        "pay_living_expenses_api":"zoukun",
        "start_living_expenses_info_api":"zoukun",
        "global_connection_traval_api":"zoukun",
        "global_connection_zone_api":"zoukun",
        "movie_ticket_api":"zoukun",
        "cinema_find_api":"zoukun",
        "multimedia_content_search_api":"zoukun",
        "multimedia_rank_search_api":"zoukun"
}


tools_and_params={"get_weather_info_api":"{}",
        "calendar_api":"{'date':'去年本月'}",
        "get_bill_cost_in_month_api":'{"year_month": [{"year": "2024", "month": "2"},{"year": "2024", "month": "3"},{"year": "2024", "month": "4"},{"year": "2024", "month": "5"}]}',
        "get_subscribe_service_api":"{}",
        "get_flow_info_api":"{}",
        "points_info_api":"{}",
        "calculator_api":"{'expression':'(3+4)/2'}",
        "get_fee_balance_api":"{}",
        "get_pay_history_api":"{}",
        "knowledge_retrieval_api":"{'query':'什么是现金账本','keyword':'现金账本'}",
        "visualization_api":"{}",
        "get_living_balance_info_api":'{"type":["燃气费"]}',
        "open_living_expenses_info_api":'{}',
        "pay_living_expenses_api":'{"amount": "100.00元","type": "电费"}',
        "start_living_expenses_info_api":"{}",
        "global_connection_traval_api":'{"city": ["合肥", "上海"],"travel_type": ["机场休息室"]}',
        "global_connection_zone_api":"{}",
        "movie_ticket_api":'{"keyword":["九龙城寨"], "place":"北京"}',
        "cinema_find_api":'{"place":"北京"}',
        "multimedia_content_search_api":'{"user_query": "我想看一部由黄轩主演的动作电影，有什么推荐？","moduleType": ["movie"],"keyword": ["黄轩","动作"]}',
        "multimedia_rank_search_api":'{"moduleType":["music"]}'
}


if __name__ == '__main__':
    code_lst=[
        "wo5yIP6ZFSIXeOP3naNTamf_r_DrbEAUKxIM_Q3HtfJIPvvVmFAExIblVuXxw0c9",
        "r1UIKe5C9C4qU0b9jWGXw9025lgo4lxI-wD19OqtIDYK3QJLHGJEGZrI9HHi21bR",
        "Yv7r5vOMv-mA9mWgpCcR9MOA3V52zX62oWEVpEwgSLX5Ry-D_qs-ZWpIsgAju1oC",
        "kBIe55pt4fPxmzDp3JaT3Om47_6Y5s1_RSas7Vil9HbbCywZs7Wz6Cyoqnd8BTY5",
        "tcYGep_muqBtApXkUFCPTYKkVoFBTkqGUI2nWnBq8wWy2FKUnQxabX_kDl8duYTH",
        "wsnmAKdCH8g2uDECPR825dzv51ZkhRNYUHb1xJGgln7Z9viR0FGmiHiVlrtNLBnM,",
        "m-vMeDQ1kMhejo8Eb8GpM0WG2PSXkNqmLP1A2-JO71f0wewYzQA9zPHRS1fUCCVT",
        "wSu7EKPH6Ppl0cC5tz-ZJanSC2STvVDTBTvhEodtrwmoHS3ZOoqt4NI0McwJ8CVH",
        "wsnmAKdCH8g2uDECPR825dzv51ZkhRNYUHb1xJGgln7Z9viR0FGmiHiVlrtNLBnM",
        "qEaxy5xmf1oV6ov8ilS7HB-oS4rm7HIIIvsVQGiRMCU5qMCqZl4OpSwSzEAOyPth",
        "Ogne881jVwB1wZCM5xK1NSqbmMK7sfMSUIKZ4nGAv6K6op2YFmi43ioEAsdLHa_A",
        "DXVFkza4fe34JIZsUeF67hIclzLgzdoDeNQa3glLXY2hoLZSCTZiVrOstLT-I8aF",
        "bIou2y54WQBokgfVSFLu46EF_3dLFQQiIzidca-87yqjOaDfBsZk26OkrH2h8Tjl"
]
    for i,code in enumerate(code_lst):
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

        print()
        os.environ['authCode'] = code
        print(os.environ.get("authCode"))
        for tool in tools_and_developers:
            params=tools_and_params[tool]
            params=eval(params)
            try:
                res=BaseTool.execute(tool,**params)
                print()
                print(f"Call {tool} and result is {res[0]},and its developer is {tools_and_developers[tool]}.")
            except:
                print("*"*40+"FAILED"+"*"*40)
                print(f"Call {tool} failed,and its developer is {tools_and_developers[tool]}.")
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
