# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 06:27:31 2019

@author: Antik
"""

import os
from twilio.rest import Client
a="Antik"
account_sid = "AC74c65f66f1de79c6a6b4f9314f161135"
auth_token = "04ca45f4d51b1c9e6dff55d9b786e3e8"

client = Client(account_sid, auth_token)
print ("Enter:")
print("1. if you want to start waterpump\n")
print("2. if you want to start fertilizer spray\n")
n = int(input("Enter your choice: "))

if (n==1):
    message = client.messages.create (
        body=a,
        from_ = "+14797633931",
        to = "+919007488686"
        )
    print(message.sid)
    print("Water pumps are started")
elif (n==0):
    message = client.messages.create (
        body="Fertilizer pumps are started",
        from_ = "+14797633931",
        to = "+919007488686"
        )
    print(message.sid)
    print("Fertilizers spray are started")
    