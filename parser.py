#!/usr/bin/env python3

import jsoner
import parameters
import configuration


def main():
    args = parameters.param()
    url = str(configuration.get_config()['url'])
    token = str(configuration.get_config()['token'])

    if args.ticket:
        ticket = args.ticket
    else:
        ticket = ""

    info = jsoner.get_json(url, token, ticket)

    jsoner.scrape(info, "victims", "emailaddress")
    jsoner.scrape(info, "attackers", "emailaddress")
    jsoner.scrape(info, "context", "emailsubject")
    jsoner.scrape(info, "context", "file", "filename")


if __name__ == "__main__":
    main()
