#!/usr/bin/python

import csv
import smtplib
from email.mime.text import MIMEText
from email.Header import Header

def sendmail(info_list):
    msg = MIMEText(info_list[2], "html", "utf-8")
    msg['Subject'] = Header("TEST SUBJECT", "utf-8")
    msg['From'] = "jkmutua@safaricom.com"
    msg['To'] = info_list[1]
    s = smtplib.SMTP('172.29.229.67')
    ##s.ehlo()
    ##s.starttls()
    ##s.login("YOUR EMAIL USERNAME", "YOUR EMAIL PASSWORD")
    s.sendmail("Change Management", info_list[1], msg.as_string())

def main():
    with open("msg.csv", "rb") as csvfile:
        msg_reader = csv.reader(csvfile)
        msg_reader.next()
        map(lambda x: sendmail(x), msg_reader)

if __name__ == "__main__":
    main()
