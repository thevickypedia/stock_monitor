#! /usr/bin/env python3
import os
import re

import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime, timedelta

current_time = datetime.now()
utc_to_cdt = current_time - timedelta(hours=5)
# dt_string = utc_to_cdt.strftime("%m/%d/%Y %H:%M:%S")
dt_string = utc_to_cdt.strftime("%A, %B %d, %Y %I:%M %p")


class StockChecker:
    def ual(self):
        stock = 'UAL'
        stock_name = 'United Airlines'
        stock_price = float(os.getenv('UAL'))
        global result
        r = requests.get(f'https://finance.yahoo.com/quote/{stock}')
        scrapped = bs(r.text, "html.parser")
        raw_data = scrapped.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0]
        price = float(raw_data.find('span').text)
        price_change = re.findall(r"\d+\.\d+", str(raw_data))
        threshold = float(os.getenv('UAL_threshold'))
        maxi = float(os.getenv('UAL_max'))

        if 'At close' in str(raw_data):
            print('\nAfter Market Hours, so check for yourself.\n')
            result = 'currently no change. Last change:'
        elif 'negativeColor' in str(raw_data):
            result = 'decreased'
        elif 'positiveColor' in str(raw_data):
            result = 'increased'
        diff = round(price - stock_price, 2)
        msg = f"The current price of {stock} is: ${price}\nYou bought it for: ${stock_price}\nDifference: " \
              f"{diff}\n{stock} share has {result} ${price_change[-2]}"

        if result == 'currently no change. Last change:':
            print(f'Data for {stock_name} as of {dt_string}:\n{msg}\n')
        elif diff < threshold:
            message = f'Time to buy new shares.\n\nData as of {dt_string}:\n{msg}\n'
            return message
        elif price > maxi:
            message_ = f'Time to sell shares.\n\nData as of {dt_string}:\n{msg}\n'
            return message_

    def expe(self):
        stock = 'EXPE'
        stock_name = 'Expedia'
        stock_price = float(os.getenv('EXPE'))
        global result
        r = requests.get(f'https://finance.yahoo.com/quote/{stock}')
        scrapped = bs(r.text, "html.parser")
        raw_data = scrapped.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0]
        price = float(raw_data.find('span').text)
        price_change = re.findall(r"\d+\.\d+", str(raw_data))
        threshold = float(os.getenv('EXPE_threshold'))
        maxi = float(os.getenv('EXPE_max'))

        if 'At close' in str(raw_data):
            result = 'currently no change. Last change:'
        elif 'negativeColor' in str(raw_data):
            result = 'decreased'
        elif 'positiveColor' in str(raw_data):
            result = 'increased'
        diff = round(price - stock_price, 2)
        msg = f"The current price of {stock} is: ${price}\nYou bought it for: ${stock_price}\nDifference: " \
              f"{diff}\n{stock} share has {result} ${price_change[-2]}"

        if result == 'currently no change. Last change:':
            print(f'Data for {stock_name} as of {dt_string}:\n{msg}\n')
        elif diff < threshold:
            message = f'Time to buy new shares.\n\nData as of {dt_string}:\n{msg}\n'
            return message
        elif price > maxi:
            message_ = f'Time to sell shares.\n\nData as of {dt_string}:\n{msg}\n'
            return message_

    def rcl(self):
        stock = 'RCL'
        stock_name = 'Royal Caribbean'
        stock_price = float(os.getenv('RCL'))
        global result
        r = requests.get(f'https://finance.yahoo.com/quote/{stock}')
        scrapped = bs(r.text, "html.parser")
        raw_data = scrapped.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0]
        price = float(raw_data.find('span').text)
        price_change = re.findall(r"\d+\.\d+", str(raw_data))
        threshold = float(os.getenv('RCL_threshold'))
        maxi = float(os.getenv('RCL_max'))

        if 'At close' in str(raw_data):
            result = 'currently no change. Last change:'
        elif 'negativeColor' in str(raw_data):
            result = 'decreased'
        elif 'positiveColor' in str(raw_data):
            result = 'increased'
        diff = round(price - stock_price, 2)
        msg = f"The current price of {stock} is: ${price}\nYou bought it for: ${stock_price}\nDifference: " \
              f"{diff}\n{stock} share has {result} ${price_change[-2]}"

        if result == 'currently no change. Last change:':
            print(f'Data for {stock_name} as of {dt_string}:\n{msg}\n')
        elif diff < threshold:
            message = f'Time to buy new shares.\n\nData as of {dt_string}:\n{msg}\n'
            return message
        elif price > maxi:
            message_ = f'Time to sell shares.\n\nData as of {dt_string}:\n{msg}\n'
            return message_

    def dfs(self):
        stock = 'DFS'
        stock_name = 'Discover Finance'
        stock_price = float(os.getenv('DFS'))
        global result
        r = requests.get(f'https://finance.yahoo.com/quote/{stock}')
        scrapped = bs(r.text, "html.parser")
        raw_data = scrapped.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0]
        price = float(raw_data.find('span').text)
        price_change = re.findall(r"\d+\.\d+", str(raw_data))
        threshold = float(os.getenv('DFS_threshold'))
        maxi = float(os.getenv('DFS_max'))

        if 'At close' in str(raw_data):
            result = 'currently no change. Last change:'
        elif 'negativeColor' in str(raw_data):
            result = 'decreased'
        elif 'positiveColor' in str(raw_data):
            result = 'increased'
        diff = round(price - stock_price, 2)
        msg = f"The current price of {stock} is: ${price}\nYou bought it for: ${stock_price}\nDifference: " \
              f"{diff}\n{stock} share has {result} ${price_change[-2]}"

        if result == 'currently no change. Last change:':
            print(f'Data for {stock_name} as of {dt_string}:\n{msg}\n')
        elif diff < threshold:
            message = f'Time to buy new shares.\n\nData as of {dt_string}:\n{msg}\n'
            return message
        elif price > maxi:
            message_ = f'Time to sell shares.\n\nData as of {dt_string}:\n{msg}\n'
            return message_
