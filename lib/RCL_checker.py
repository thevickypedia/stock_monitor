#! /usr/bin/env python3
import logging
import os
import re
import sys
from datetime import datetime

import requests
from bs4 import BeautifulSoup as bs

stock = 'RCL'
stock_price = os.getenv('RCL')

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


class RCLChecker:
    def statistics(self):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
        logger = logging.getLogger('UAL_checker.py')

        global result
        r = requests.get(f'https://finance.yahoo.com/quote/{stock}')
        scrapped = bs(r.text, "html.parser")
        raw_data = scrapped.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0]
        price = raw_data.find('span').text
        percent = re.findall(r"\d+\.\d+", str(raw_data))

        if 'At close' in str(raw_data):
            result = 'currently no change. Last change:'
        elif 'negativeColor' in str(raw_data):
            result = 'decreased'
        elif 'positiveColor' in str(raw_data):
            result = 'increased'
        diff = round(float(price) - float(stock_price), 2)
        msg = f"The current price of {stock} is: ${price}\nYou bought it for: ${stock_price}\nDifference: " \
              f"{diff}\n{stock} share has {result} {percent[-1]}%"

        if result == 'currently no change. Last change:' and diff < 0:
            logger.info(f'\n{msg}\n')
        elif diff < 0:
            message = f'Time to buy new shares.\n\nData as of {dt_string}:\n{msg}\n'
            return message
