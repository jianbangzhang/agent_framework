# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : constants.py
# Time       ：2024/8/28 11:12
# Author     ：jianbang
# version    ：python 3.10
# company    : IFLYTEK Co.,Ltd.
# emil       : whdx072018@foxmail.com
# Description：
"""




# refiner
REFINER_SYSTEM_TEMPLATES="""你是一个multi-agent system，我需要对以下内容进行提炼反思。给你需要反思的内容，你需要反思出2个方面的内容：正向反思内容和负向反思内容。"""

REFINER_REQUIREMENTS_TRIPLETS="""正向反思输出按照问题及其对应的三元组（API[param:type]-after-responses）2个方面。负向反思从tools using和 parameters passing 进行反思，输出tools using或着parameters passing错误的三元组。你可以从API相似度高、参数拼写错误和不完整或错误的参数设置头脑风暴出三元组。"""
REFINER_REQUIREMENTS_NATURAL="""正向反思输出按照问题、规划过程和回复3个方面。负向反思从tools using和 parameters passing 2个方面输出。"""

REFINER_EXAMPLES_TRIPLETS="""【例子】
暖气费这个月还剩多少？
Thought: 需要查询暖气费的余额，所以先调用生活缴费余额查询工具。
Action: get_living_balance_info_api
Action_Parameter: {"type":["暖气费"]}
Observation:{"result": [{"type": "暖气费", "balance": "80.00元"}],"reminder":"灵犀已为您查到，您当前账户暖气费余额80元，建议您及时充值。"}
Thought: 已经查询到暖气费的余额，无需调用其他工具，现在可以回复给用户。
Finish: 您好，灵犀已为您查到，您当前账户暖气费余额80元，建议您及时充值。

Positive reflecting:
给你一个例子，你把它反思成三元组的形式：question:暖气费这个月还剩多少？ React: get_living_balance_info_api[
param:type]-after-灵犀已为您查到，您当前账户暖气费余额XXX元，建议您及时充值。

Negative reflecting:
positive reacting: get_payment_balance_info_api[param: 暖气费]-after-灵犀已为您查到，您当前账户暖气费余额80元，建议您及时充值。
negative reacting: get_living_balance_info_api[param: "type":"暖气费"]-after-参数传递错误。"""

REFINER_EXAMPLES_NATURAL="""【例子】
暖气费这个月还剩多少？
Thought: 需要查询暖气费的余额，所以先调用生活缴费余额查询工具。
Action: get_living_balance_info_api
Action_Parameter: {"type":["暖气费"]}
Observation:{"result": [{"type": "暖气费", "balance": "80.00元"}],"reminder":"灵犀已为您查到，您当前账户暖气费余额80元，建议您及时充值。"}
Thought: 已经查询到暖气费的余额，无需调用其他工具，现在可以回复给用户。
Finish: 您好，灵犀已为您查到，您当前账户暖气费余额80元，建议您及时充值。

正向反思：
给你一个例子，你把它反思成文本形式：question:暖气费这个月还剩多少？ 规划过程：先调用get_living_balance_info_api
，入参type；回复：您好，灵犀已为您查到，您当前账户暖气费余额XXX元，建议您及时充值。 


负向反思【基于Graph】
API相似度高：系统中可能存在其他用于查询余额的API，如get_account_balance_info_api或get_utility_balance_info_api，这些API名称和功能与get_living_balance_info_api非常接近，容易造成误调用。
参数拼写错误：如果type参数中的值被拼写错误（如"dianfei"而不是"电费"），API可能无法识别该参数，导致查询失败。
不完整或错误的参数设置：有些API可能需要多个参数共同传递，但如果遗漏了必需的参数或者误传了无关的参数，也可能导致API无法返回正确结果。"""
