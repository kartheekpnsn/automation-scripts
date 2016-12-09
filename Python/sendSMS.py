#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#               File Owner - Kartheek Palepu            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import twilio
import twilio.rest
from twilio.rest import TwilioRestClient
from generateLogs import *
from datetime import datetime
# ACCOUNT_SID = "ACdb78c3a4d074a8716fab8a49199c6ae8"
# AUTH_TOKEN = "80ff03c75250f09c9489ae6ea199be13"
ACCOUNT_SID = "add your own id found in twilio.com/user/account"
AUTH_TOKEN = "add your own token found in twilio.com/user/account"
def sendSMS(my_message):
  try:
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    print client
    messages = client.messages.create(to='+919886872955', from_='+12038839799', body=my_message)
    generateLogs("SMS_Logs", str(datetime.now()) + "- SENT SUCCESSFULLY\n")
    generateLogs("SMS_Logs", "====================================================\n")
  except twilio.TwilioRestException as e:
    generateLogs("SMS_Logs",str(datetime.now()) + "- FAILED " + str(e) + "\n")
    generateLogs("SMS_Logs", "====================================================\n")
