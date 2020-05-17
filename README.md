# Stock Monitor
A report on the list of shares you have purchased

## Pre-Req:

1. AWS account

2. Verify sender and recipient (can be same but not advisable) email addresses in AWS SES (Simple Email Service)

3. Create a lambda function or ECS task if you wish to run this on a cron schedule / on demand (optional as you can run it using your local IDE)

## Setup

1. git clone this repository

2. Run this command in your terminal to install necessary packages<br/>cd stock_monitor/lib && pip3 install -r requirements.txt

2. Make sure you add the following env variables
* UAL, EXPE, RCL, DFS - The price you bought these stock for (change values as these are my portfolio)
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
* UAL_threshold, EXPE_threshold, RCL_threshold, DFS_threshold - The threshold difference after which you'd like to be notified (ex: If you have bought XXX stock for $60 and currently it is $63, if your threshold is < 3 you will be notified)
* UAL_max, EXPE_max, RCL_max, DFS_max - Maximum value after which you'd like to be notified

## Usage

Option 1:
  * Download an IDE such as [pycharm](https://www.jetbrains.com/pycharm/download/download-thanks.html).
  * Setup python3 interpreter
  * Add environment variables in configurations
  
Option 2:
  * Create a .sh file with the above environment variables and run it or manually set each environment variable
  * Run the command<br/>python3 stock_monitor/stock_monitor.py
  
Option 3:
  * Install a docker and set the entry point to stock_monitor.py

Click [here](https://www.twilio.com/docs/whatsapp/quickstart/python) to get started with Twilio or refer [twilio](https://pypi.org/project/twilio/) docs for quick start.<br/>If you prefer not to use whats app notifications then simply change send_whatsapp() to send_email() in [stock_monitor.py](https://github.com/vignesh1793/stock_monitor/blob/master/stock_monitor.py#L92) and add arguments 'data, context' [here](https://github.com/vignesh1793/stock_monitor/blob/master/stock_monitor.py#L51)<br/>By doing this the [send_whatsapp()](https://github.com/vignesh1793/stock_monitor/blob/master/stock_monitor.py#L62-L76) function will never be called.


Note: The code was built from the scratch but it was built with an intention to share knowledge and for educational purpose.<br/>Parts of the code can be easily hard coded but left as env to increase reusability.<br/>The application is extremely customizable so remove/add parts of code where ever unnecessary.
