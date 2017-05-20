#! /usr/bin/env python3

import sys
import os
from slacker import Slacker

# Constants 

ARGUMENTS   = sys.argv[1:]
TOKEN = 'xoxp-185264591041-185758810371-186690127527-0a3745a255e587d51d8b71b9f5e44209'
USER = 'ckelly19'
MESSAGE = ':banana:'

# Functions 

def usage(exit_code=0):
   print('''Usage: {} [-t TOKEN -u USER -m MESSAGE]
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
	elif arg == '-t':
		TOKEN = ARGUMENTS.pop(0)
	elif arg == '-u':
		USER = ARGUMENTS.pop(0)
	elif arg == '-m':
		MESSAGE = ARGUMENTS.pop(0)
	else:
		usage(1)

slack = Slacker(TOKEN)

# Get users list
response = slack.users.list()
users = response.body['members']

# find user
for user in users:
	if user['name'] == USER:
		USER = user['id'] # replace USER with corresp. ID number

# message channel
try:
	slack.chat.post_message(USER, MESSAGE, as_user=True)
except:
	print("Error: couldn't find \'{}\' slack user/channel".format(USER))
	exit(1)

