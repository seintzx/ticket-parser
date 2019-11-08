# ticket-parser

parser for tickets, it takes all gathered info for an easy markdown copy-paste

# Installation

```
pip install -r requirements.txt
```

## Configuration file

Edit the `config.txt` with your API key
```
[configuration]
API = [virus total api key]
```
Without square brackets, replace every `%` with `%%`

# Usage

```
usage: parser.py [-h] -t TICKET

Ticket parser to gather involved info

optional arguments:
  -h, --help            show this help message and exit
  -t TICKET, --ticket TICKET
                        set the ticket ID
```
If you want to copy results to clipboard
```
python parser.py -t TICKET | xclip -sel clip
```
