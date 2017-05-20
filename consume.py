#!/usr/bin/env python3

import requests
import json
import sys
import os

# Constants 
ARGUMENTS   = sys.argv[1:]
WEBHOOK = 'https://hooks.slack.com/services/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'
CHANNEL = '#general'
USER = ''
MESSAGE = ':banana:'

# Functions 

def usage(exit_code=0):
   print('''Usage: {} [-w WEBHOOK -u USER -c CHANNEL -m MESSAGE]
   -t TOKEN API token of team to send results to
   -u USER name of user or channel to send results to
   -m MESSAGE message to send to user\n'''.format(os.path.basename(sys.argv[0])))
   sys.exit(exit_code)


# Main Execution

# Parse command line arguments
while ARGUMENTS and ARGUMENTS[0].startswith('-') and len(ARGUMENTS[0]) > 1:
	arg = ARGUMENTS.pop(0)
	if arg == '-h':
		usage(0)
	elif arg == '-w':
		WEBHOOK = ARGUMENTS.pop(0)
	elif arg == '-c':
		CHANNEL = ARGUMENTS.pop(0)
	elif arg == '-u':
		USER = ARGUMENTS.pop(0)
	elif arg == '-m':
		MESSAGE = ARGUMENTS.pop(0)
	else:
		usage(1)

# send to either a USER or a CHANNEL
if USER != '':
	payload = {
		"text": MESSAGE,
		"channel": CHANNEL,
		"icon_emoji":":monkey_face:",
		"username": "George"
	}
else: 
	payload = {
		"text": MESSAGE,
		"user": USER,
		"icon_emoji":":monkey_face:",
		"username": "George"
	}

try:
	while 1:
		r = requests.post(WEBHOOK, data = json.dumps(payload))
except:
	# exit gracefully
	exit(0)