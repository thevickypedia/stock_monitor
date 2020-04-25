#! /usr/bin/env python3
import os
import sys

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
        sys.exit()


if __name__ == '__main__':
    sender_env = os.getenv('SEND')
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
    Emailer(sender, recipient, title, text)
