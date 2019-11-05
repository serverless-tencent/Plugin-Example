# -*- coding: utf8 -*-


def main_handler(event, context):
    with open("index.html", "r", encoding='utf-8') as f:
        html_data = f.read()
    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {"Content-Type": "text/html"},
        "body": html_data
    }

