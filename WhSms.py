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
    parser.add_argument("-t", "--tophone", dest="tophone", help="Use to specify the number to send to (with +)")
    parser.add_argument("-m", "--message", dest="message", help="Use to specify the message to send")
    return parser.parse_args()

args = main()

account_sid = (f'{args.accountsid}')
auth_token = (f'{args.authtoken}')

from_phone = (f'{args.fromphone}')
to_phone = (f'{args.tophone}')

client = Client(account_sid, auth_token)

def message():
    message = client.messages.create(body=(f'{args.message}'), from_=from_phone, to=to_phone)
    return message.sid

print("sending your message...")

try:
    message()
    print("message sent")

except Exception as e:
    print("unexpected mistake!", end="\n")
    print("Twilio Error:", e.code, "-", e.msg, end="\n")
    print("Enter all valid parameters (more -h)")
