# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : uitls.py
# Time       ：2024/8/25 11:45
# Author     ：jianbang
# version    ：python 3.10
# company    : IFLYTEK Co.,Ltd.
# emil       : whdx072018@foxmail.com
# Description：
"""
import time
import traceback

def singleton(cls):
    """
    :param cls: one class that should not be reconstructed
    :return:
    """
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


def retry(max_retry=3, delay=1):
    """
    :param max_retry:
    :param delay:
    :return:
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            retry_count = 0
            result=""
            code=-1
            while retry_count < max_retry and code!=0:
                try:
                    result = func(*args, **kwargs)
                    code=0
                except Exception as e:
                    print(f"Exception occurred: {e}")
                    error = traceback.format_exc()
                    result={"error":str(error)}
                    code=-1
                    time.sleep(delay)
                retry_count+=1
            return result, code
        return wrapper
    return decorator



def getMsgFromText(text,token,filter_token):
    """
    :param text:
    :param token:
    :param filter_token:
    :return:
    """
    res=""
    text=text.replace("：",":").strip()
    if token in text:
        for line in text.split("\n"):
            line=line.strip()
            if line.startswith(token):
                res+=line
            else:
                continue

        if filter_token:
            res=res.replace(token,"").strip()
    else:
        res=text
    return res



def print_env(info):
    env_info=f"[Environment Info]:{info}"
    print(env_info)
    return env_info



def print_args(args):
    """
    :param args:class
    :return:
    """
    print_msg="[Config Info]:Set Agent Framework variables:"
    start_tab="\t"
    print(print_msg)
    attributes = args.__dict__

    for attr_name, attr_value in attributes.items():
        if hasattr(attr_value, '__dict__'):
            for name,value in attr_value.__dict__.items():
                print_msg+=f"\n{start_tab}{name}: {value}"
                print(f"{start_tab}{name}: {value}")
        else:
            print_msg+=f"\n{start_tab}{attr_name}: {attr_value}"
            print(f"{start_tab}{attr_name}: {attr_value}")
    return print_msg




def check_config_args(config):
    """
    descript:Verify if there are any inconsistencies in the parameter settings
    :param config: agent system config
    :return: bool-True or False
    """

    has_memory=config.has_memory
    n_shot = config.n_shot_prompt
    assert (n_shot==0 and not has_memory),"when there is n  "

