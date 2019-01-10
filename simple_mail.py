#!/usr/bin/python

import smtplib

sender = 'sender_mail'
receivers = ['receiver_mails']

message = """From: From Name <send mail>
To: To Beth <receiver_mail>
Subject: SMTP e-mail test

This is a test e-mail to see whether python can send emails.
"""

try:
   smtpObj = smtplib.SMTP('SMPT Server and port')
   smtpObj.sendmail(sender, receivers, message)         
   print ("Successfully sent email")
except SMTPException:
   print ("Error: unable to send email")
