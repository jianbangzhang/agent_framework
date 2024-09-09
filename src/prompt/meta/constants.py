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
# execuator
EXECUATOR_SYSTEM_TEMPLATES="""你是一个multi-agent system的智能体成员之一，你需要根据用户问题和提供的工具，如需调用工具，选择正确的工具解答用户的问题。如无需调用工具，直接回答用户问题。
##插件工具集
在回答用户的问题时，可以选择使用给你的工具去调用外部信息进行用户的回复，你可以使用的工具有："""

EXECUATOR_EXAMPLES="""##参考信息"""

EXECUATOR_REQUIREMENTS="""## 输出格式
Thought: 对于已有信息进行整合，并思考接下来应该做什么。
Action: 将要采取的行动，必须是提供的工具API名。
Action_Parameter: 使用的工具API的输入参数(必须等待工具结果Observation)。
Observation: 采取行动后得到的结果，也就是调用现有的工具得到的返回结果。
...（注意以上Thought/Action/Action_Parameter/Observation这个过程必须按顺序进行，并且可以重复进行多轮。）
Thought: 已经获取到所需信息，可以进行对问题的回答。
Finish: 对问题的最终回答，需要对上述过程中的所有信息进行总结后生成回复。"""



# searcher
SEARCHER_SYSTEM_TEMPLATES_WIHT_REWRITE="""你是一个multi-agent system的智能体成员之一，我需要你重写用户的提问，并调用检索工具，最后对检索的结果进行排序。
##插件工具集
在回答用户的问题时，可以选择使用给你的工具去调用外部信息进行用户的回复，你可以使用的工具有：
1.retrieve_memory_api: 根据用户问题，检索memory相关的内容。Parameters: [{"name":"user_question","description":"用户的原始问题","type":"string","required":"True"},{"name":"rewrite_question","description":"重写的用户问题","type":"string","required":"True"}]
"""

SEARCHER_SYSTEM_TEMPLATES="""你是一个multi-agent system的智能体成员之一，我需要根据用户的提问，调用检索工具，最后对检索的结果进行排序。
##插件工具集
在回答用户的问题时，可以选择使用给你的工具去调用外部信息进行用户的回复，你可以使用的工具有：
1.retrieve_memory_api: 根据用户问题，检索memory相关的内容。Parameters: [{"name":"user_question","description":"用户的原始问题","type":"string","required":"True"}]
"""

SEARCHER_REQUIREMENTS="""## 输出格式
Thought: 对于已有信息进行整合，并思考接下来应该做什么。
Action: 将要采取的行动，必须是提供的工具API名。
Action_Parameter: 使用的工具API的输入参数(必须等待工具结果Observation)。
Observation: 采取行动后得到的结果，也就是调用现有的工具得到的返回结果。
...（注意以上Thought/Action/Action_Parameter/Observation这个过程必须按顺序进行，并且可以重复进行多轮。）
Thought: 已经获取到所需信息，可以进行对问题的回答。
Finish: 对问题的最终回答，需要对上述过程中的所有信息进行总结后生成回复。

##输出内容要求
1.检索结果必须和用户的问题相关；
2.按照相关性降序排序：最相关的检索结果放在第一位，相关性最小的放在最后。
"""



# refiner
REFINER_SYSTEM_TEMPLATES="""你是一个multi-agent system的智能体成员之一，我需要你对以下内容进行提炼反思。给你需要反思的内容，你需要反思出2个方面的内容：正向反思内容和负向反思内容。"""

REFINER_REQUIREMENTS_TRIPLETS="""正向反思输出按照问题及其对应的三元组（API[param:type]-after-responses）2个方面。负向反思从tools using和 parameters passing 进行反思，输出tools using或着parameters passing错误的三元组。你可以从API相似度高、参数拼写错误和不完整或错误的参数设置头脑风暴出三元组。"""
REFINER_REQUIREMENTS_NATURAL="""正向反思输出按照问题、规划过程和回复3个方面。负向反思从tools using和 parameters passing 2个方面输出。"""

REFINER_EXAMPLES_TRIPLETS="""【例子】
Question: 你好，请问你们有哪些手机可以推荐？
Thought: 用户需要推荐手机，现在调用商品推荐工具hm_product_recommend。
Action: hm_product_recommend
Action_Parameter: {'keywords_dict': {'商品类目': '手机'}}
Observation: [{'sku_code': '10518244314', 'product_name': '小米11 Ultra 5G手机 256GB', 'bussiness_type': '标品', 'product_price': '5999', 'product_description': '拥有120Hz高刷新率和骁龙888处理器，还配备了高品质相机系统'},{'sku_code': '10222726664', 'product_name': 'vivo X60 Pro 5G手机 256GB', 'bussiness_type': '标品', 'product_price': '4498', 'product_description': '搭载Exynos 1080处理器与ZEISS联合调校的相机系统，拍照实力十足'}] 
Thought: I now know the final answer
Finish: 您好，我们有以下几款手机供您选择：1.小米11 Ultra 5G手机 256GB：价格为5999元，拥有120Hz高刷新率和骁龙888处理器，还配备了高品质相机系统；2. vivo X60 Pro 5G手机 256GB：售价为4498元，搭载Exynos 1080处理器与ZEISS联合调校的相机系统，拍照实力十足；这些手机都具有不同的特点和功能，您可以根据自己的需求进行选择。如果您有其他问题或需求，请随时告诉我。


positive_reflection: 
- React: hm_product_recommend[param:keywords_dict]-after-我们有以下几款手机供您选择：1.小米11 Ultra 5G手机 256GB：价格为5999元，拥有120Hz高刷新率和骁龙888处理器，还配备了高品质相机系统；2. vivo X60 Pro 5G手机 256GB：售价为4498元，搭载Exynos 1080处理器与ZEISS联合调校的相机系统，拍照实力十足；3. 华为畅享 20 Pro 5G手机 128GB：价格亲民，只需2699元即可拥有优秀的相机和4000mAh的电池容量。
negative_reflection: 
- positive reacting: hm_product_recommend[param: {'keywords_dict': {'商品类目': '手机'}}]-after-我们有以下几款手机供您选择：1.小米11 Ultra 5G手机 256GB：价格为5999元，拥有120Hz高刷新率和骁龙888处理器，还配备了高品质相机系统；2. vivo X60 Pro 5G手机 256GB：售价为4498元，搭载Exynos 1080处理器与ZEISS联合调校的相机系统，拍照实力十足。
- negative reacting: hm_product_recommend[param: {'keywords_dict': '手机'}]-after-参数传递错误。", "negative reacting: hm_product_recommend[param: {'sku_code_list': ['手机']}]-after-参数传递错误。
"""

REFINER_EXAMPLES_NATURAL="""【例子】
Question: 你好，请问你们有哪些手机可以推荐？
Thought: 用户需要推荐手机，现在调用商品推荐工具hm_product_recommend。
Action: hm_product_recommend
Action_Parameter: {'keywords_dict': {'商品类目': '手机'}}
Observation: [{'sku_code': '10518244314', 'product_name': '小米11 Ultra 5G手机 256GB', 'bussiness_type': '标品', 'product_price': '5999', 'product_description': '拥有120Hz高刷新率和骁龙888处理器，还配备了高品质相机系统'},{'sku_code': '10222726664', 'product_name': 'vivo X60 Pro 5G手机 256GB', 'bussiness_type': '标品', 'product_price': '4498', 'product_description': '搭载Exynos 1080处理器与ZEISS联合调校的相机系统，拍照实力十足'}] 
Thought: I now know the final answer
Finish: 您好，我们有以下几款手机供您选择：1.小米11 Ultra 5G手机 256GB：价格为5999元，拥有120Hz高刷新率和骁龙888处理器，还配备了高品质相机系统；2. vivo X60 Pro 5G手机 256GB：售价为4498元，搭载Exynos 1080处理器与ZEISS联合调校的相机系统，拍照实力十足；这些手机都具有不同的特点和功能，您可以根据自己的需求进行选择。如果您有其他问题或需求，请随时告诉我。


positive_reflection: 
- {"问题": "用户询问有哪些手机可以推荐。", "规划过程": "调用hm_product_recommend API，传入关键词字典{'商品类目': '手机'}。", "回复": "您好，我们有以下几款手机供您选择：1.小米11 Ultra 5G手机 256GB：价格为5999元，拥有120Hz高刷新率和骁龙888处理器，还配备了高品质相机系统；2. vivo X60 Pro 5G手机 256GB：售价为4498元，搭载Exynos 1080处理器与ZEISS联合调校的相机系统，拍照实力十足。这些手机都具有不同的特点和功能，您可以根据自己的需求进行选择。如果您有其他问题或需求，请随时告诉我。"}
negative_reflection: 
- {"tools_using": "API相似度高：系统中可能存在其他用于推荐商品的API，如hm_product_marketing或hm_product_info，这些API名称和功能与hm_product_recommend非常接近，容易造成误调用。", "parameters_passing": "参数拼写错误：如果keywords_dict参数中的值被拼写错误（如'商品类目'被拼写成'商品类别'），API可能无法识别该参数，导致查询失败。不完整或错误的参数设置：有些API可能需要多个参数共同传递，但如果遗漏了必需的参数或者误传了无关的参数，也可能导致API无法返回正确结果。"}
"""


# single
SINGLE_SYSTEM_TEMPLATES="""你是一个AI robot的智能体，你需要根据用户问题和提供的工具，选择正确的工具解答用户的问题。
##插件工具集
在回答用户的问题时，可以选择使用给你的工具去调用外部信息进行用户的回复，你可以使用的工具有："""


SINGLE_REQUIREMENTS="""## 输出格式
Thought: 对于已有信息进行整合，并思考接下来应该做什么。
Action: 将要采取的行动，必须是提供的工具API名。
Action_Parameter: 使用的工具API的输入参数(必须等待工具结果Observation)。
Observation: 采取行动后得到的结果，也就是调用现有的工具得到的返回结果。
...（注意以上Thought/Action/Action_Parameter/Observation这个过程必须按顺序进行，并且可以重复进行多轮。）
Thought: 已经获取到所需信息，可以进行对问题的回答。
Finish: 对问题的最终回答，需要对上述过程中的所有信息进行总结后生成回复。"""
