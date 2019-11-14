# ticket-parser

parser for tickets, it takes all gathered info for an easy markdown copy-paste

# Installation

```
pip install -r requirements.txt
```

## Configuration file

Create the `config.txt` file or edit the existent one
```
[configuration]
URL = [url of the API]
token = [session token]
```
Without square brackets, replace every `%` with `%%`

# Usage

```
usage: parser.py [-h] -t TICKET [-e]

Ticket parser to gather involved info

optional arguments:
  -h, --help            show this help message and exit
  -t TICKET, --ticket TICKET
                        set the ticket ID
  -e, --eng             english version
```
If you want to copy results to clipboard
```
python parser.py -t TICKET | xclip -sel clip
```
