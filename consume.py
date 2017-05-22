#!/usr/bin/env python3

import requests
import json
import yaml
import time
import argparse
from os.path import expanduser

# Constants 
WEBHOOK = ''
CHANNEL = ''
USER = ''
MESSAGE = ''

# Main Execution

# Parse command line arguments
parser = argparse.ArgumentParser(description='Message a user on Slack')
parser.add_argument('-w', type=str, help="webhook url of team to send results to", dest=WEBHOOK)
parser.add_argument('-u', type=str, help="name of user to send results to", dest=USER)
parser.add_argument('-c', type=str, help="name of channel to send results to", dest=CHANNEL)
parser.add_argument('-m', type=str, help="message to send to user or channel", dest=MESSAGE)
args = parser.parse_args()

# Load message data
data_file = expanduser("~") + '/.consume_data/data.yml'
data = yaml.safe_load(open(data_file))

# send to either a USER or a CHANNEL
if data['USER'] != '':
	payload = {
		"text": data['MESSAGE'],
		"channel": data['CHANNEL'],
		"icon_emoji":":monkey_face:",
		"username": "George"
	}
else: 
	payload = {
		"text": data['MESSAGE'],
		"user": data['USER'],
		"icon_emoji":":monkey_face:",
		"username": "George"
	}

# consume channel with posts
print("consume.py: consuming...")

r = requests.post(data['WEBHOOK'], data = json.dumps(payload))
COUNT = 1
while r.text == 'ok':
	r = requests.post(data['WEBHOOK'], data = json.dumps(payload))
	COUNT += 1
	time.sleep(1) # API allows 1 message per second 

print("consume.py: sent {} messages before reaching rate limit".format(COUNT))
