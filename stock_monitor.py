#! /usr/bin/env python3
import os
import sys

from twilio.rest import Client

from lib.DFS_checker import DFSChecker
from lib.EXPE_checker import EXPEChecker
from lib.RCL_checker import RCLChecker
from lib.UAL_checker import UALChecker
from lib.emailer import Emailer


def email_formatter():
    UAL_info = UALChecker().statistics()
    EXPE_info = EXPEChecker().statistics()
    RCL_info = RCLChecker().statistics()
    DFS_info = DFSChecker().statistics()

    if UAL_info or EXPE_info or RCL_info or DFS_info is None:
        email_text = 'Stock Monitoring Notification\n'

        if UAL_info:
            email_text += '\nUnited Airlines Report:\n'
            email_text += UAL_info

        if EXPE_info:
            email_text += '\nExpedia Report:\n'
            email_text += EXPE_info

        if RCL_info:
            email_text += '\nRoyal Caribbean Report:\n'
            email_text += RCL_info

        if DFS_info:
            email_text += '\nDiscover Report:\n'
            email_text += DFS_info

        return email_text
    else:
        sys.exit()


def send_email():
    sender_env = os.getenv('SENDER')
    recipient_env = os.getenv('RECIPIENT')
    git_env = os.getenv('GIT')
    footer_text = "\n----------------------------------------------------------------" \
                  "----------------------------------------\n" \
                  "A report on the list shares you have purchased. " \
                  "The data is being collected from https://finance.yahoo.com," \
                  f"\nFor more information check README.md in {git_env}"
    sender = f'Stock Hawk <{sender_env}>'
    recipient = [f'{recipient_env}']
    title = 'Stock Monitor Alert'
    text = f'{email_formatter()}\n\n{footer_text}'
    email = Emailer(sender, recipient, title, text)
    return email


def send_whatsapp():
    sid = os.getenv('SID')
    token = os.getenv('TOKEN')
    sender = f"whatsapp:{os.getenv('SEND')}"
    receiver = f"whatsapp:{os.getenv('RECEIVE')}"
    client = Client(sid, token)
    from_number = sender
    to_number = receiver
    send_email()
    logs = 'https://us-west-2.console.aws.amazon.com/cloudwatch/home?region=us-west-2#logs:'
    client.messages.create(body=f'Stock Monitoring Notification\nLog info here\n{logs}',
                           from_=from_number,
                           to=to_number)


if __name__ == '__main__':
    send_whatsapp()
