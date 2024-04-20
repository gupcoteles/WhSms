from twilio.rest import Client
import argparse
import time
import random
from assets.font.font import *

print(random.choice(Font))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-as", "--accountsid", dest="accountsid", help="Use to specify twilio account sid")
    parser.add_argument("-at", "--authtoken", dest="authtoken", help="Use to specify twilio auth token")
    parser.add_argument("-f", "--fromphone", dest="fromphone", help="Use to specify twilio number (with +)")
    parser.add_argument("-t", "--tophone", dest="tophone", help="Use to specify the target's number (with +)")
    parser.add_argument("-m", "--message", dest="message", help="Use to specify the message to send")
    return parser.parse_args()

args = main()

account_sid = ('' + args.accountsid + '')
auth_token = ('' + args.authtoken + '')

from_phone = ('' + args.fromphone + '')
to_phone = ('' + args.tophone + '')

client = Client(account_sid, auth_token)

def message():
    message = client.messages.create(body=('' + args.message + ''), from_=from_phone, to=to_phone)
    return message.sid

print("attack started")

counter = 0
while True:
    counter += 1
    try:
        print(message(), "attack: ", counter)
        time.sleep(0)


    except Exception as e:
        print("Twilio Error:", e.code, "-", e.msg, end="\n")
        print("Enter all valid parameters (more -h)")
        break