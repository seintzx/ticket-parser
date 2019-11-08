# ticket-parser

parser for tickets, it take all gathered info for an easy markdown copy-paste

# Installation

```
pip install -r requirements.txt
```

# Usage

```
usage: parser.py [-h] [-s TOKEN] [-t TICKET]

Ticket parser to gather involved info

optional arguments:
  -h, --help            show this help message and exit
  -s TOKEN, --token TOKEN
                        set the session token
  -t TICKET, --ticket TICKET
                        set the ticket ID
```
If you want to copy results to clipboard
```
python3 parser.py -s TOKEN -t TICKET | xclip -sel clip
```
