#!/usr/bin/python
import smtplib
import yaml
import os
import sys

accountfile = os.path.expanduser("~") + "/.email/email-credentials.yml"
account = yaml.safe_load(open(accountfile))

to = sys.argv[1]
note = sys.argv[2]
message = """ From: %s
Subject: Something went wrong

%s

""" % (account['from'], note)

smtp = smtplib.SMTP_SSL()
smtp.connect(account['server'],int(account['port']))
smtp.login(account['username'], account['password'])
smtp.sendmail(account['from'],to,message)
