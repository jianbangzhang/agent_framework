# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : tool.py
# Time       ：2024/8/25 16:14
# Author     ：jianbang
# version    ：python 3.10
# company    : IFLYTEK Co.,Ltd.
# emil       : whdx072018@foxmail.com
# Description：
"""
from abc import abstractmethod
from typing import Union, NoReturn,Sequence,Dict



class MetaClass(type):
    def __init__(cls, name, bases, attrs):
        """
        :param name:
        :param bases:
        :param attrs:
        """
        super().__init__(name, bases, attrs)

    @classmethod
    def register(cls):
        raise NotImplementedError


class BaseTool(metaclass=MetaClass):
    name = "baseTool"
    is_remote=False
    description="This is based class which manages all tool subclass."

    @classmethod
    def execute(cls, subclass_name:str, *args, **kwargs)->Union[str,Sequence,Dict,NoReturn]:
        """
        :param subclass_name: class.name
        :param args:
        :param kwargs:
        :return:
        """
        return cls._execute(subclass_name, *args, ** kwargs)

    @classmethod
    def _execute(cls,subclass_name:str, *args, **kwargs):
        for subclass in cls.__subclasses__():
            if hasattr(subclass, 'name') and subclass.name == subclass_name:
                observation,code=subclass()(*args, **kwargs)
                if "businessResult" in observation:
                    del observation["businessResult"]
                if "reminder" in observation and observation["reminder"] is None:
                    del observation["reminder"]
                return observation,code
            else:
                continue
        raise NotImplementedError(f"{subclass_name} is either regitered,or subclass of {cls}")

    @classmethod
    def register(cls, class_name:type)->bool:
        """
        :param class_name:
        :return:
        """
        if class_name in cls.__subclasses__():
            print(f"{class_name} has already been registered.")
            return True
        else:
            print(f"{class_name} is not registered")
            return False

    @abstractmethod
    def __call__(self, *args, **kwargs)->NoReturn:
        """
        :param args:
        :param kwargs:
        :return:
        """
        raise NotImplementedError


    def __repr__(self):
        """print function info"""
        function_info=str(self.name)+"\n"+str(self.is_remote)+"\n"+str(self.description)
        return function_info