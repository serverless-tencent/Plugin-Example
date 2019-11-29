# -*- coding: utf8 -*-


def student_get(event, context):
    print(str(event))
    # todo: student action
    return {
        "result": "it is student_get action"
    }


def teacher_put(event, context):
    print(str(event))
    # todo: teacher action
    return {
        "result": "it is teacher_put action"
    }
