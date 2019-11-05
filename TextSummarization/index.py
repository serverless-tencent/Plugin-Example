# -*- coding: utf8 -*-
import logging
import jieba.analyse
from snownlp import SnowNLP

logging.basicConfig(level=logging.NOTSET)


def FromSnowNlp(text, summary_num):
    s = SnowNLP(text)
    return s.summary(summary_num)


def FromJieba(text, keywords_type, keywords_num):
    if keywords_type == "tfidf":
        return jieba.analyse.extract_tags(text, topK=keywords_num)
    elif keywords_type == "textrank":
        return jieba.analyse.textrank(text, topK=keywords_num)
    else:
        return None


def main_handler(event, context):
    text = event["text"]
    summary_num = event["summary_num"]
    keywords_num = event["keywords_num"]
    keywords_type = event["keywords_type"]
    return {"keywords": FromJieba(text, keywords_type, keywords_num),
            "summary": FromSnowNlp(text, summary_num)}
