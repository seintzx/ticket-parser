#!/usr/bin/env python3

import argparse


def param():
    parser = argparse.ArgumentParser(
        description="Ticket parser to gather involved info")

    parser.add_argument("-t",
                        "--ticket",
                        help="set the ticket ID",
                        action="store",
                        required=True)

    parser.add_argument("-e",
                        "--eng",
                        action="store_true",
                        help="English version")

    return (parser.parse_args())
