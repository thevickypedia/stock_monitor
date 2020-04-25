#! /usr/bin/env python3
import os
import re
import sys
from datetime import datetime

import requests
from bs4 import BeautifulSoup as bs

stock = 'EXPE'
stock_price = os.getenv('EXPE')

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


class EXPEChecker:
    def statistics(self):
        global result, diff
        r = requests.get(f'https://finance.yahoo.com/quote/{stock}')
        scrapped = bs(r.text, "html.parser")
        raw_data = scrapped.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0]
        price = raw_data.find('span').text
        percent = re.findall(r"\d+\.\d+", str(raw_data))

        if 'tertiaryColor' in str(raw_data) and len(percent) > 5:
            print('After Market Hours\nCheck for yourself lazy ASS')
            sys.exit()
        elif 'negativeColor' in str(raw_data):
            result = 'decreased'
        elif 'positiveColor' in str(raw_data):
            result = 'increased'
        diff = round(float(price) - float(stock_price), 2)
        msg = f"The current price of {stock} is: ${price}\nYou bought it for: ${stock_price}\nDifference: " \
              f"{diff}\n{stock} share has {result} {percent[-1]}%"
        if diff < 0:
            message = f'Time to buy new shares.\n\nData as of {dt_string}:\n{msg}\n'
            return message
