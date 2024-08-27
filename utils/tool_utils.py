# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : tool_utils.py
# Time       ：2024/8/25 16:11
# Author     ：jianbang
# version    ：python 3.10
# company    : IFLYTEK Co.,Ltd.
# emil       : whdx072018@foxmail.com
# Description：
"""

tool_dict= {
    "get_bill_cost_in_month_api":
    {
        "tool": "账单查询工具",
        "api_name": "get_bill_cost_in_month_api",
        "api_description": "查询用户某个或多个月份的消费账单，返回内容包括当月的总消费金额，扣费项目和每项的扣费金额数据。",
        "parameters": [
            {
                "name": "year_month",
                "description": "用户需要查询的所有年月，每项必须是一个字典，其中month必填表示查询的月份，year选填表示查询的年份（默认值为""表示当前年份），month和year都必须是阿拉伯数字字符串，例如[{'year':'2024','month':'4'}]",
                "type": "List[Dict]",
                "required": True
            }
        ],
        "return_descrition": {
            "result": [
                {
                    "month": "表示本项查询结果所属的年份和月份",
                    "total_bill": "本月总消费金额",
                    "actual_pay": "实际应付金额（指本月总消费金额剔除他人代付、活动返还、优惠金额后的实际支付费用）",
                    "save_bill": "本期账单的总优惠金额（包括减免金额，活动范费抵扣金额）",
                    "business_bill": "套餐及固定费用（指基础套餐、语音包、流量包、宽带、来电显示等固定费用）",
                    "outplan_bill": "套餐外消费（包括套餐外语音费、套餐外上网费、套餐外短/彩信费）",
                    "added_bill": "增值业务费（包括互联网电视、彩铃、视频彩铃、咪咕会员等）"
                }
            ],
            "提醒事项": "回答用户时，需要提醒用户的注意事项，例如是否产生超套消费等。"
        }
    },

    "get_subscribe_service_api":
    {
        "tool": "已订业务查询工具",
        "api_name": "get_subscribe_service_api",
        "api_description": "用于查询获取用户套餐中包含的已订购业务的详细信息",
        "parameters": [],
        "return_descrition": {
            "result": [
                {
                    "service_name": "订购的业务名称",
                    "subscription_date": "业务订购日期",
                    "end_date": "业务结束时间"
                }
            ]
        }
    },


    "get_fee_balance_api":
    {
        "tool": "话费查询工具",
        "api_name": "get_fee_balance_api",
        "api_description": "查询账户内当前可用余额与本月已消费金额。",
        "parameters": [],
        "return_descrition": {
            "result": {
                    "left_money": "账户可用余额",
                    "used_money": "本月已消费金额",
                },
            "提醒事项": "回答用户时，需要提醒用户的注意事项，例如是否话费不足等。"
        }
    },

    "get_pay_history_api":
    {
        "tool": "充值记录查询工具",
        "api_name": "get_pay_history_api",
        "api_description": "查询获取用户历史充值记录信息。",
        "parameters": [],
        "return_descrition": {
            "result": [
                {
                    "amount": "充值金额",
                    "payType": "充值方式",
                    "payDate": "充值时间"
                }
            ]
        }
    },

    "get_flow_info_api":
    {
        "tool": "流量查询工具",
        "api_name": "get_flow_info_api",
        "api_description": "查询用户本月流量使用情况，返回内容包含本月不同类型的流量总数、已使用量、剩余量。",
        "parameters": [],
        "return_descrition": {
            "result": [
                {
                    "resource_unit": "资源单位",
                    "remaining_amount": "流量剩余",
                    "total_amount": "流量总量",
                    "used_amount": "流量已使用量",
                    "flow_category": "流量类型"
                }
            ],
            "提醒事项": "回答用户时，需要提醒用户的注意事项，例如是否流量不足等。"
        }
    },

    "points_info_api":
    {
        "tool": "积分查询工具",
        "api_name": "points_info_api",
        "api_description": "查询用户账户内当前可用积分总量。",
        "parameters": [],
        "return_descrition": {
            "result": {"totalPoint": "账户内积分总量"}
        }
    },

    "visualization_api":
    {
        "tool": "绘图工具",
        "api_name": "visualization_api",
        "api_description": "根据输入的横纵坐标和数值，绘制一张二维图表",
        "parameters": [
            {
                "name": "x",
                "description": "横轴数据，例如 ['一月', '二月', '三月']",
                "type": "List[str]",
                "required": True
            },
            {
                "name": "y",
                "description": "纵轴数据，例如 ['100', '150', '93']",
                "type": "List[str]",
                "required": True
            },
            {
                "name": "labels",
                "description": "横轴和纵轴的图例，例如 {'x':'月份', 'y':'消费金额（元）'}",
                "type": "dict",
                "required": True
            }
        ],
        "return_descrition": {
            "result": "是否绘图成功的信号"
        }
    },

    "calendar_api":
    {
        "tool": "日期查询工具",
        "api_name": "calendar_api",
        "api_description": "将口语表达的时间转换为标准格式的日期。",
        "parameters": [
            {
                "name": "date",
                "description": "日期或时间的模糊口语表达",
                "type": "str",
                "required": True
            }
        ],
        "return_descrition": {
            "result": {
                "date": "转换后的日期，为'yyyy-mm-dd'的格式",
                "星期": "这天是星期几"
            }
        }
    },

    "calculator_api":
    {
        "tool": "计算器工具",
        "api_name": "calculator_api",
        "api_description": "根据提供的数学表达式计算出正确的数值结果，适用于需要计算差值、总量、均值等等场景",
        "parameters": [
            {
                "name": "expression",
                "description": "需要执行的数学表达式，例如'(3+2)*5'",
                "type": "str",
                "required": True
            }
        ],
        "return_descrition": {
            "result": "表达式计算结果"
        }
    },

    "knowledge_retrieval_api":
    {
        "tool": "知识库查询工具",
        "api_name": "knowledge_retrieval_api",
        "api_description": "根据输入的query，查询知识库中相关文档内容。",
        "parameters": [
            {
                "name": "query",
                "description": "用户的提问的规范表达，例如:解释什么是话费透支免单",
                "required": True,
                "type": "str"
            },
            {
                "name": "keyword",
                "description": "用户问题的关键词，例如:话费透支免单",
                "required": True,
                "type": "str"
            }
        ],
        "return_descrition": {
            "result": "与该问题查到的相关文档内容"
        }
    },

    "get_weather_info_api":
    {
        "tool": "天气查询工具",
        "api_name": "get_weather_info_api",
        "api_description": "查询某个城市今天或未来某天的天气情况，不支持查询过去日期的天气。",
        "parameters": [
            {
                "name": "city",
                "description": "用户需要查询的城市名称列表，如果是空列表，则表示查询本地城市",
                "required": True,
                "type": "List[str]"
            },
            {
                "name": "date",
                "description": "用户需要查询的日期列表，必须是标准时间格式'yyyy-mm-dd'，如果查今天，可直接传入空列表，注意",
                "required": True,
                "type": "List[str]"
            }
        ],
        "return_descrition": {
            "result": [
                {
                    "city": "查询的城市名称",
                    "date": "查询的日期",
                    "weather": "天气，例如`晴`",
                    "temperatureRange": "气温范围",
                    "minimumTemperature": "最低气温",
                    "maximumTemperature": "最高气温",
                    "airQualityIndex": "空气质量指数",
                    "airQualityLevel": "空气质量等级",
                    "humidity": "湿度",
                    "wind": "风向",
                    "windForce": "风力",
                    "ultraviolet": "紫外线等级",
                    "clothing_suggestion": "衣着建议",
                    "coldIndex": "感冒指数",
                    "trafficIndex": "交通指数",
                    "exerciseIndex": "运动指数",
                    "tourismIndex": "旅游指数"
                }
            ]
        }
    },


    "global_connection_traval_api":
    {
        "tool": "全球通出行工具",
        "api_name": "global_connection_traval_api",
        "api_description": "提供全球通出行相关权益和服务页面跳转操作，全球通出行服务场景包括机场休息室服务、高铁休息室服务、高铁列车餐食服务、旅游礼遇、酒店礼遇、出境礼遇。",
        "parameters": [
            {
                "name": "city",
                "description": "用户提到的全球通出行权益相关的城市，可以是多个地点，当没提到任何地点时，应传入空列表",
                "required": True,
                "type": "List[str]"
            },
            {
                "name": "travel_type",
                "description": "当用户问题涉及机场休息室或高铁休息室时传入该参数，只能是'机场休息室'或'高铁休息室'，严禁传入其他任何内容，可以是二者都包含，例如['机场休息室']或者['机场休息室','高铁休息室']，当没有提到时，应传入空列表",
                "required": True,
                "type": "List[str]"
            }
        ],
        "return_descrition": {
            "result": "回复用户时的话术模板"
        }
    },

    "global_connection_zone_api":
    {
        "tool": "全球通专区工具",
        "api_name": "global_connection_zone_api",
        "api_description": "提供全球通专区页面跳转展示操作，全球通专区内容包含：全球通品牌活动（全球通星动日活动、逐马计划、全球通蓝色梦想公益计划）、5G直通车活动、全球通尊享服务、全球通尊享特权",
        "parameters": [],
        "return_descrition": {
            "result": "回复用户时的话术模板"
        }
    },

    "pay_living_expenses_api":
    {
        "tool": "生活缴费充值工具",
        "api_name": "pay_living_expenses_api",
        "api_description": "生活缴费充值接口，包括电费、水费、燃气费和暖气费等充值",
        "parameters": [
            {
                "name": "amount",
                "description": "充值金额",
                "type": "str",
                "required": True
            },
            {
                "name": "type",
                "description": "充值类型，包括'电费','水费','燃气费','暖气费'",
                "type": "str",
                "required": True
            }
        ],
        "return_descrition": {
            "result": "回复用户时的话术模板"
        }
    },

    "get_living_balance_info_api":
    {
        "tool": "生活缴费余额查询",
        "api_name": "get_living_balance_info_api",
        "api_description": "生活缴费余额查询接口，包括电费、水费、燃气费和暖气费等余额",
        "parameters": [
            {
                "name": "type",
                "description": "要查询的缴费类型，例如['电费']",
                "type": "List[str]",
                "required": True
            }
        ],
        "return_descrition": {
                "result": [
                    {
                    "type": "电费",
                    "balance": "50.00元"
                    },
                    {
                    "type": "水费",
                    "balance": "39元"
                    },
                    {
                    "type": "燃气费",
                    "balance": "100.00元"
                    }
                ],
                "reminder": "灵犀已为您查到，您当前账户电费余额50元，水费余额39元，燃气费余额100元。建议您及时充值。"
}
    },

    "open_living_expenses_info_api":
    {
        "tool": "生活缴费记录页面跳转工具",
        "api_name": "open_living_expenses_info_api",
        "api_description": "打开生活缴费记录的查询界面，查询电费、水费、燃气费和暖气费",
        "parameters": [],
        "return_descrition": {
            "result": "回复用户的话术模板"
        }
    },

    "multimedia_content_search_api":
    {
        "tool": "影视、音乐、阅读内容查询工具",
        "api_name": "multimedia_content_search_api",
        "api_description": "根据场景类别（电影/电视剧/音乐/阅读/）和关键词（如作品名称/导演/主演/歌手/作者/类型/风格）搜索出相关的具体作品。",
        "parameters": [
            {
                "name": "user_query",
                "description": "用户输入的query，例如'我想看沈腾主演的电影'",
                "type": "str",
                "required": True
            },
            {
                "name": "moduleType",
                "description": "需要查询的媒体类别，仅限于【'movie（表示电影）'、'tv（表示电视剧）'、'music（表示音乐）'、'reading（表示阅读）'】，如果提到多项应该输入其中的多项，但不能是枚举项之外的其他值。输入示例：['movie', 'music']",
                "type": "List[str]",
                "required": True
            },
            {
                "name": "keyword",
                "description": "用于搜索的关键词，可以是电影电视剧的名称、导演、主演、类型，或者音乐的歌名、歌手、专辑名，或者书籍的书名、作者、类型；如果提到多项应该输入其中的多项。输入示例：['周星驰', '功夫', '喜剧']",
                "type": "List[str]",
                "required": True
            }
        ],
        "return_descrition": {
            "result": [
                {
                    "name": "作品名称",
                    "moduleType": "作品类型",
                    "description": "作品简介"
                }
            ],
            "回复话术": "回复用户时的话术模板"
        }
    },

    "multimedia_rank_search_api":
    {
        "tool": "影视、音乐、阅读榜单查询工具",
        "api_name": "multimedia_rank_search_api",
        "api_description": "根据场景类别（电影/电视剧/音乐/阅读/）搜索出相应场景榜单上排名靠前的作品。",
        "parameters": [
            {
                "name": "moduleType",
                "description": "需要查询的媒体类别，仅限于【'movie（表示电影）'、'tv（表示电视剧）'、'music（表示音乐）'、'reading（表示阅读）'】，如果提到多项应该输入其中的多项，但不能是枚举项之外的其他值。输入示例：['movie', 'tv']",
                "type": "List[str]",
                "required": True
            }
        ],
        "return_descrition": {
            "result": [
                {
                    "name": "作品名称",
                    "moduleType": "作品类型"
                }
            ],
            "回复话术": "回复用户时的话术模板"
        }
    },

    "movie_ticket_api":
    {
        "tool": "电影购票工具",
        "api_name": "movie_ticket_api",
        "api_description": "在用户想要购买电影票时，根据输入的关键词，返回匹配到的电影详情。",
        "parameters": [
            {
                "name": "keyword",
                "description": "用户提到的关键词，例如电影的电影名、导演、演员、类型、简介等。输入示例：['爱情片', '泰坦尼克']",
                "type": "List[str]",
                "required": True
            },
            {
                "name": "place",
                "description": "用户提到的位置信息，例如城市、地区",
                "type": "str",
                "required": True
            }
        ],
        "return_descrition": {
            "result": [
                {
                    "name": "电影名称",
                    "description": "电影简介",
                }
            ],
            "回复话术": "回复用户时的话术模板"
        }
    },

    "cinema_find_api":
    {
        "tool": "电影院搜索工具",
        "api_name": "cinema_find_api",
        "api_description": "搜索附近的电影院",
        "parameters": [
            {
                "name": "place",
                "description": "用户提到的位置信息，例如城市、地区",
                "type": "str",
                "required": True
            }
        ],
        "return_descrition": {
            "result": "是否搜索成功",
            "回复话术": "回复用户时的话术模板"
        }
    },

    "complex_visualization_api":
    {
        "tool": "复杂绘图工具",
        "api_name": "complex_visualization_api",
        "api_description": "可以根据用户提供的数据，绘制图表，并返回完成状态",
        "parameters": [
            {
                "name": "x",
                "description": "横轴数据，例如 {'日期':['2024-01-20', '2024-01-21','2024-01-22']}",
                "type": "Dict",
                "required": True
            },
            {
                "name": "y",
                "description": "纵轴数据，括号为单位，例如 [{'最高气温(摄氏度)':['15', '14', '18']},{'最低气温(摄氏度)':['5', '2', '10']}]",
                "type": "List[Dict]",
                "required": True
            },
            {
                "name": "type",
                "description": "枚举值：折线图、柱状图、饼状图和表格。趋势类的数据选择折线图，对比类数据选择柱状图，详情类数据画饼状图，面板数据选择表格，例如 '折线图'。",
                "type": "str",
                "required": True
            }
        ],
        "return_descrition": {
                "result": "固定返回'success',表示绘图完成。"
        }
    }
}