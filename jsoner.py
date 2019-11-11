#!/usr/bin/env python3

import requests
import json


def get_json(url, token, ticket):
    url = url.format(ticket)
    key = "connect.sid"
    val = token
    jar = requests.cookies.RequestsCookieJar()
    jar.set(key, val)
    response = requests.get(url, cookies=jar)
    return (response.json())


def scrape(lis, where, what, deep=None):
    foobar = []
    name = "null"
    for foo in lis:
        if foo["_id"] == where:
            for bar in foo["value"]:
                if bar["kind"] == what:
                    if deep is None:
                        name = where
                        foobar.append(bar["name"])
                    else:
                        name = deep
                        foobar.append(bar["details"][deep])

    result = ""
    result += "- **{0}**\n".format(name)
    result += "\t```\n".expandtabs(4)
    for foo in sorted(foobar):
        result += "\t".expandtabs(4) + foo + "\n"
    result += "\t```\n".expandtabs(4)
    return (result)
