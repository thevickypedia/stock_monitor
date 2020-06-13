# Stock Monitor
A report on the list of shares you have purchased

Click to visit the AWS version [Black Pearl](https://github.com/thevickypedia/black_pearl)

## Pre-Req:

1. AWS account

2. Verify sender and recipient (can be same but not advisable) email addresses in AWS SES (Simple Email Service)

3. Create a lambda function or ECS task if you wish to run this on a cron schedule / on demand (optional as you can run it using your local IDE)

## Setup

1. git clone this repository

2. Run this command in your terminal to install necessary packages<br/>cd yahoo_finance_monitor/lib && pip3 install -r requirements.txt

2. Make sure you add the following env variables
* ACCESS_KEY - AWS access key id
* SECRET_KEY - AWS secret access key
* SENDER - sender email address (verified via AWS SES)
* RECIPIENT - receiver email address (verified via AWS SES)
* ACCESS_KEY - AWS access to authenticate into your AWS account
* SECRET_KEY - AWS secret key
* SID - s-id from twilio
* TOKEN - token from twilio
* SEND - sender whats app number (fromat - +1xxxxxxxxxx)
* RECEIVE - receiver whats app number (fromat - +1xxxxxxxxxx)
* stock_1 - Symbol for the stock you'd like to track (Eg: MSFT for Microsoft)
* stock_1_min - The minimum value below which you'd like to be notified
* stock_1_max - The maximum value above which you'd like to be notified
* Note: Keep increasing the # as you want more stocks to be tracked. (Limit: 25)

## Usage

Option 1:
  * Download an IDE such as [pycharm](https://www.jetbrains.com/pycharm/download/download-thanks.html).
  * Setup python3 interpreter
  * Add environment variables in configurations
  
Option 2:
  * Create a .sh file with the above environment variables and run it or manually set each environment variable
  * Run the command<br/>python3 yahoo_finance_monitor/stock_monitor.py
  
Option 3:
  * Install a docker and set the entry point to stock_monitor.py

Click [here](https://www.twilio.com/docs/whatsapp/quickstart/python) to get started with Twilio or refer [twilio](https://pypi.org/project/twilio/) docs for quick start.<br/>If you prefer not to use whats app notifications then simply change send_whatsapp() to send_email() in [stock_monitor.py](https://github.com/thevickypedia/stock_monitor/blob/master/stock_monitor.py#L174) and add arguments 'data, context' [here](https://github.com/thevickypedia/stock_monitor/blob/master/stock_monitor.py#L51)<br/>By doing this the [send_whatsapp()](https://github.com/thevickypedia/stock_monitor/blob/master/stock_monitor.py#L62-L76) function will never be called.


Note: The code was built from the scratch but it was built with an intention to share knowledge and for educational purpose.<br/>Parts of the code can be easily hard coded but left as env to increase reusability.<br/>The application is extremely customizable so remove/add parts of code where ever unnecessary.
