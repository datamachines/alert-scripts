#! /usr/bin/env python3

import yaml
import argparse
from os.path import expanduser
from slacker import Slacker

# Constants 

TOKEN = ""
USER = ""
MESSAGE = ""

# Main Execution

# Parse command line arguments
parser = argparse.ArgumentParser(description='Message a user on Slack')
parser.add_argument('-t', type=str, help="API token of team to send results to", dest=TOKEN)
parser.add_argument('-u', type=str, help="name of user or channel to send results to", dest=USER)
parser.add_argument('-m', type=str, help="message to send to user or channel", dest=MESSAGE)
args = parser.parse_args()

# Load message data
data_file = expanduser("~") + '/.message_data/data.yml'
data = yaml.safe_load(open(data_file))

slack = Slacker(data['TOKEN'])

# Get users list
response = slack.users.list()
users = response.body['members']

# find user
USER = data['USER'] # default
for user in users:
	if user['name'] == data['USER']:
		USER = user['id'] # replace USER with corresp. ID number

# message channel
try:
	slack.chat.post_message(USER, data['MESSAGE'], as_user=True)
except:
	print("Error: couldn't find \'{}\' slack user/channel".format(USER))
	exit(1)

