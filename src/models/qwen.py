# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : qwen.py
# Time       ：2024/9/1 10:54
# Author     ：jianbang
# version    ：python 3.10
# company    : IFLYTEK Co.,Ltd.
# emil       : whdx072018@foxmail.com
# Description：
"""
from .base_model import BaseModel
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer



class QWen2Model(BaseModel):
    def __init__(self,model_type,is_remote_llm,model_config,*args,**kwargs):
        """
        :param model_type:
        :param is_remote_llm:
        :param model_config:
        :param args:
        :param kwargs:
        """
        super(QWen2Model, self).__init__(model_type, is_remote_llm, model_config, *args, **kwargs)
        self.device=self._get_device()


    def _get_device(self):
        if torch.cuda.is_available():
            device_id=0
            device=torch.device(f"cuda:{device_id}")
        else:
            device=torch.device("cpu")
        return device


    def _get_model(self,model_name):
        """
        :param model_name:
        :return:
        """
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype="auto",
            device_map="auto",
            trust_remote_code=True
        )
        return model


    def _get_tokenizer(self,model_name):
        """
        :param model_name:
        :return:
        """
        tokenizer = AutoTokenizer.from_pretrained(model_name,trust_remote_code=True)
        return tokenizer


    def _call_qwen2(self,model_name,prompt,max_token,*args,**kwargs):
        """
        :param prompt:
        :param max_token:
        :param args:
        :param kwargs:
        :return:
        """
        model = self._get_model(model_name)
        tokenizer = self._get_tokenizer(model_name)

        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
        text = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )
        model_inputs = tokenizer([text], return_tensors="pt").to(self.device)

        generated_ids = model.generate(
            model_inputs.input_ids,
            max_new_tokens=max_token
        )
        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]

        response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        return response


    def _generate(self,model_name, prompt,max_token,*args,**kwargs):
        raise self._call_qwen2(prompt,max_token,*args,**kwargs)


    def _check_config(self,*args,**kwargs):
        if self.model_type=="qewn2":
            raise ValueError("model name is not right.")


    def __repr__(self):
        info = "This is qwen2 model,not qwen1.5."
        return info






















