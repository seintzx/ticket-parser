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


def scrape(lis, where, lwhat, deep=None):
    foobar = []
    name = None
    for foo in lis:
        if foo["_id"] == where:
            for bar in foo["value"]:
                for what in lwhat:
                    if bar["kind"] == what:
                        if deep is None:
                            name = what if where is "context" else where
                            foobar.append(bar["name"])
                        else:
                            name = deep
                            foobar.append(bar["details"][deep])

    if name is not None:
        res = ""
        res += "- **{0}**\n".format(name)
        res += "\t```\n".expandtabs(4)
        for foo in sorted(foobar):
            res += "\t".expandtabs(4) + foo + "\n"
        res += "\t```\n".expandtabs(4)
        return (res)
    return ("")
