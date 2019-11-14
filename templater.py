#!/usr/bin/env python3


def get_template(path):
    TEMPLATE_DIR = "template/"
    with open(TEMPLATE_DIR + path, 'r') as file:
        body = file.read()
    file.close()
    return (body)
