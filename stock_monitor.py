#! /usr/bin/env python3
import os
from datetime import datetime, timedelta

from twilio.rest import Client

from lib.emailer import Emailer
from lib.stock_checker import StockChecker

logs = 'https://us-west-2.console.aws.amazon.com/cloudwatch/home?region=us-west-2#logStream:group=/aws/lambda' \
       '/stock_hawk '


def email_formatter():
    UAL_info = StockChecker().ual()
    EXPE_info = StockChecker().expe()
    RCL_info = StockChecker().rcl()
    DFS_info = StockChecker().dfs()

    if UAL_info or EXPE_info or RCL_info or DFS_info:
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
        print('Nothing to notify, bye..')
        return None


def send_email():
    if email_formatter():
        sender_env = os.getenv('SENDER')
        recipient_env = os.getenv('RECIPIENT')
        git_env = os.getenv('GIT')
        footer_text = "\n----------------------------------------------------------------" \
                      "----------------------------------------\n" \
                      "A report on the list shares you have purchased that has either deceeded the MIN purchase " \
                      "value or exceeded the MAX selling value.\n" \
                      "The data is being collected from https://finance.yahoo.com," \
                      f"\nFor more information check README.md in {git_env}"
        sender = f'Stock Hawk <{sender_env}>'
        recipient = [f'{recipient_env}']
        title = 'Stock Monitor Alert'
        text = f'{email_formatter()}\n\nNavigate to check logs: {logs}\n\n{footer_text}'
        email = Emailer(sender, recipient, title, text)
        return email
    else:
        return None


# two arguments for the below functions as lambda passes event, context by default
def send_whatsapp(data, context):
    if send_email():
        now = datetime.now() - timedelta(hours=5)
        dt_string = now.strftime("%A, %B %d, %Y %I:%M %p")
        sid = os.getenv('SID')
        token = os.getenv('TOKEN')
        sender = f"whatsapp:{os.getenv('SEND')}"
        receiver = f"whatsapp:{os.getenv('RECEIVE')}"
        client = Client(sid, token)
        from_number = sender
        to_number = receiver
        client.messages.create(body=f'{dt_string}\n\nStock Monitoring Notification\nLog info here\n{logs}',
                               from_=from_number,
                               to=to_number)
    else:
        return None


if __name__ == '__main__':
    send_whatsapp("data", "context")
