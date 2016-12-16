#!/usr/bin/python
import requests
import json
import sys
chan = sys.argv[1]
message = sys.argv[2]

print "#" + chan, ":", message

webhookurl = "your webhook url from the slack admin"

payload = {
"text":message,
"channel": chan,
"icon_emoji":":skull_and_crossbones:",
"username": "error"
}

r = requests.post(webhookurl, data = json.dumps(payload))
print r.text
