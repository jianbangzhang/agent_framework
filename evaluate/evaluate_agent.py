# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : evaluate_agent.py
# Time       ：2024/9/2 09:01
# Author     ：jianbang
# version    ：python 3.10
# company    : IFLYTEK Co.,Ltd.
# emil       : whdx072018@foxmail.com
# Description：
"""
import rouge
import jieba
from rouge_chinese import Rouge


class EvaluateAgent(object):
    def __init__(self,generate_agent_text:str,gold_agent_text:str):
        self.generate_agent_text=generate_agent_text
        self.gold_agent_text=gold_agent_text

    def evaluate(self):
        predict_agent_api_params,predict_agent_text=self.parse_tracjectory(self.generate_agent_text)
        gold_agent_api_params,gold_agent_text=self.parse_tracjectory(self.gold_agent_text)

        api_score = self.compute_em_score_api(predict_agent_api_params, gold_agent_api_params)
        rouge_l_score = self.compute_rouge_l_zh(predict_agent_text,gold_agent_text)
        precision, recall, f1 =self.compute_argument_f1(predict_agent_api_params, gold_agent_api_params)
        evaluate_dict={"ApiScore":api_score,
                       "ParameterScore":{
                           "precision":precision,
                           "recall":recall,
                           "f1":f1},
                       "ThoughtAnswerRougeL":rouge_l_score
                       }
        return evaluate_dict



    def parse_tracjectory(self,text):
        """
        gold_api_calls = [{"api": "get_weather", "location": "New York", "date": "2022-08-01"},{}]
        agent_string str
        :param text:
        :return:
        """
        def get_content(line, token):
            content = ""
            if line.startswith(token):
                line = line.replace(token, "").strip()
                content += line
            return content

        agent_api_params=[]
        agent_text=""
        thought_lst, action_lst, param_lst, obs_lst, finish = [], [], [], [], []
        pipeline = [thought_lst, action_lst, param_lst, obs_lst, finish]

        line_lst = [line.strip() for line in text.strip().split("\n") if line.strip()]
        token_lst = "Thought Action Action_Parameter Observation Finish".split(" ")

        for line in line_lst:
            if len(line) == 0:
                continue
            line = line.replace("：", ":")

            for token, lst in zip(token_lst, pipeline):
                token = token + ":"
                res = get_content(line, token)
                if len(res) > 0:
                    lst.append(res)
                else:
                    continue

        assert len(action_lst) == len(param_lst) == len(obs_lst) and len(thought_lst) == len(action_lst) + 1 \
               and len(finish) == 1, "data is not right."

        for data in zip(thought_lst[0:-1], action_lst, param_lst, obs_lst):
            Thought, Action, Action_Parameter, Observation = data
            param_dict=eval(Action_Parameter)
            agent_api_params.append({"api":Action,**param_dict})
            agent_text+=" "+Thought

        agent_text+=" "+thought_lst[-1]+" "+finish[0]
        return agent_api_params,agent_text

    def compute_em_score_api(self,predictions, gold_labels):
        predictions, gold_labels = [p["api"] for p in predictions], [g["api"] for g in gold_labels]
        return sum([1 if pred in gold_labels else 0 for pred in predictions]) / len(gold_labels)

    def compute_rouge_l_zh(self,predictions, gold_labels):
        evaluator = Rouge()
        predictions = ' '.join(jieba.cut(predictions))
        gold_labels = ' '.join(jieba.cut(gold_labels))
        scores = evaluator.get_scores(predictions, gold_labels)
        rouge_l_f_score = scores[0]['rouge-l']['f']
        return rouge_l_f_score

    def compute_rouge_l_en(self,predictions, gold_labels):
        evaluator = rouge.Rouge(metrics=['rouge-l'])
        scores = evaluator.get_scores(predictions, gold_labels)
        rouge_l_f_score = scores[0]['rouge-l']['f']  # Accessing the first pair's f-score
        return rouge_l_f_score

    def compute_argument_f1(self,predictions, gold_labels):
        total_true_positives = 0  # Full Matches
        total_partial_true_positives = 0  # Half Matches
        total_predicted = 0
        total_actual = 0

        for pred, gold in zip(predictions, gold_labels):
            pred_args = set(pred.keys())
            gold_args = set(gold.keys())

            full_matches = sum([1 for arg in pred_args.intersection(gold_args) if pred[arg] == gold[arg]])
            half_matches = sum([1 for arg in pred_args.intersection(gold_args) if pred[arg] != gold[arg]])

            total_true_positives += full_matches
            total_partial_true_positives += half_matches
            total_predicted += len(pred)
            total_actual += len(gold)

        precision = (0.5 * total_partial_true_positives + total_true_positives) / total_predicted if total_predicted else 0
        recall = (0.5 * total_partial_true_positives + total_true_positives) / total_actual if total_actual else 0
        f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) else 0

        return precision, recall, f1







