#!/usr/bin/env python3

import clipboard
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

    lkind = ["emailaddress", "host"]

    result = ""
    result += jsoner.scrape(info, "victims", lkind)
    result += jsoner.scrape(info, "attackers", lkind)
    result += jsoner.scrape(info, "context", ["emailsubject"])
    result += jsoner.scrape(info, "context", ["file"], "filename")
    result = result[:-1]

    clipboard.copy(result)
    print(result)


if __name__ == "__main__":
    main()
