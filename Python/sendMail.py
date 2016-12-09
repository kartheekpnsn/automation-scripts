#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#               File Owner - Kartheek Palepu            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import traceback
import smtplib

def mail(mid, subject, message):
  fromaddr = 'your-mail-id'
  toaddrs  = mid
  username = 'your-mail-id'
  password = 'your-mail-password'

  SUBJECT = subject
  TEXT = message
  # sendSMS(SUBJECT)
  # Prepare actual message
  message = 'From: '+ fromaddr +'\r\nTo: '+ toaddrs + '\r\nSubject: ' + SUBJECT +'\n\n' + TEXT + '\nThis is an automated mail message. Please do not reply to this.\n\nThanks and Regards\nYour_Name\nYour_Number'
  try:
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, message)
    server.quit()
  except Exception, err:
    print(traceback.format_exc())

# mail("kartheekpnsn@gmail.com", "HELLO WORLD", "Hello World, This is Kartheek")
