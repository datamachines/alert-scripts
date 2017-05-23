#!/usr/bin/env python3

import yaml
import time
import argparse
import logging
from slackclient import SlackClient
from os.path import expanduser

# Load message data
data_file = expanduser("~") + '/.consume_data/data.yml'
data = yaml.safe_load(open(data_file))

# Constants 
TOKEN = data['TOKEN']
CHANNEL = data['CHANNEL']
MESSAGE = data['MESSAGE']
OK = True
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

# Main Execution

# Parse command line arguments
parser = argparse.ArgumentParser(description='consume a channel on Slack')
parser.add_argument('-t', type=str, help="API token of team to send results to", dest=TOKEN)
parser.add_argument('-c', type=str, help="name or ID of channel to consume", dest=CHANNEL)
parser.add_argument('-m', type=str, help="message to send to consume channel", dest=MESSAGE)
args = parser.parse_args()

# create client
sc = SlackClient(TOKEN)

# start connection
logging.info("starting connection...")
if sc.rtm_connect():  # connect to a Slack RTM websocket
	logging.info("connection successful...")
	time.sleep(1) # wait for response

	# read connection response
	logging.debug("[RTM Websocket Response] {}".format(sc.rtm_read())) # read initial response
	logging.debug("[RTM Websocket Response] {}".format(sc.rtm_read())) # read initial response
	
	# get channel
	logging.info("locating channel \'{}\'...".format(CHANNEL))
	response = sc.server.channels.find(CHANNEL)
	CHANNEL_ID = response.id

	# consume until error
	logging.info("consuming...")
	while OK:
		sc.rtm_send_message(CHANNEL_ID, MESSAGE) # send message
		time.sleep(1)	# wait one second
		response = sc.rtm_read()
		if response:
			if 'ok' in response[0]:	# skip other types of responses (i.e. 'reconnect_url')
				OK = response[0]['ok']
			elif 'type' in response[0]:
				if response[0]['type'] == 'error':
					OK = False
		logging.debug("[RTM Websocket Response] {}".format(response)) # read response

	# print error 
	logging.error("[RTM Websocket Response] Send Message Error: {}".format(response[0]['error']['msg']))
else:
    logging.error('[RTM Websocket Connection] FAILED: possible invalid token')

# exit on failure
logging.info("exiting...")