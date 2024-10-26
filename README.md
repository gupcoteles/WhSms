# WhSms

A simple sms sender.

# Installation

```
python3 -m pip install -r requirements.txt
```


>[!NOTE]
>You Should have installed python

>[!TIP]
>You can install python from <a href="https://www.python.org/downloads/" target="_blank">here</a>.


# Usage

```
python WhSms.py -h
```

This will display help for the tool. Here are all the switches it supports.

```
Usage:
     python3 WhSms.py [Flags]

Flags:
    -as, --accountsid Use to specify twilio account sid
    -at, --authtoken  Use to specify twilio auth token
    -f, --fromphone   Use to specify twilio number (with +)
    -t, --tophone     Use to specify the message to send (with +)
Example:
    python3 WhSms.py -as <twilio accound sid> -at <twilio auth token> -f +<your twilio phone number> -t +<target phone number> -m <message>
    python3 WhSms.py --accoundsid <twilio accound sid> --authtoken <twilio auth token> --fromphone +<your twilio phone number> --tophone +<target phone number> --message <message>
```

> [!NOTE]
> If you have more than one word in your message, send your message in quotation marks

```
Example:
     python3 WhSms.py -as <twilio accound sid> -at <twilio auth token> -f +<your twilio phone number> -t +<target phone number> -m "<message>"
     python3 WhSms.py --accoundsid <twilio accound sid> --authtoken <twilio auth token> --fromphone +<your twilio phone number> --tophone +<target phone number> --message "<message>"
```
