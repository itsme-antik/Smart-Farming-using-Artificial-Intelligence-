# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 06:31:41 2019

@author: Antik
"""

from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACa865c07c05278d91995550e45e36c1ea'
auth_token = 'd14b19df3a87471c1bd7e850f4836392'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello there!',
                              from_='whatsapp:+1 732 733 2557',
                              to='whatsapp:+919007488686'
                          )