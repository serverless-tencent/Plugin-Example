# -*- coding: utf8 -*-


def product_get():
    # todo: product_get action
    return {
        "result": "it is product_get action"
    }


def product_put():
    # todo: product_put action
    return {
        "result": "it is product_put action"
    }


def main_handler(event, context):
    print(str(event))
    if event["httpMethod"] == "GET":
        return product_get()
    if event["httpMethod"] == "PUT":
        return product_put()
