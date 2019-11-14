#!/usr/bin/env python3

import clipboard
import configuration
import jsoner
import parameters
import templater


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

    if args.eng:
        body = templater.get_template('email-eng.md').format(result)[:-1]
    else:
        body = templater.get_template('email-ita.md').format(result)[:-1]

    clipboard.copy(body)
    print(body)


if __name__ == "__main__":
    main()
