# WpSms

a simple sms sender

# Installation

```
python3 -m pip install -r requirements.txt
```

# Usage

```
python3 WpSms.py -h
```

This will display help for the tool. Here are all the switches it supports.

```
Usage:
     python3 WpSms.py [Flags]

Flags:
    -as, --accountsid Use to specify twilio account sid
    -at, --authtoken  Use to specify twilio auth token
    -f, --fromphone   Use to specify twilio number (with +)
    -t, --tophone     Use to specify the message to send
Example:
    -as <twilio accound sid> -at <twilio auth token> -f +<your twilio phone number> -t +<target phone number> -m <message>
    --accoundsid <twilio accound sid> --authtoken <twilio auth token> --fromphone +<your twilio phone number> --tophone +<target phone number> --message <message>
```

> [!NOTE]
> If you have more than one word in your message, send your message in quotation marks

```
Example:
     -as <twilio accound sid> -at <twilio auth token> -f +<your twilio phone number> -t +<target phone number> -m "<message>"
     --accoundsid <twilio accound sid> --authtoken <twilio auth token> --fromphone +<your twilio phone number> --tophone +<target phone number> --message "<message>"
```
