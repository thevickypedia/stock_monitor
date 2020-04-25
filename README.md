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
* AWS_DEFAULT_REGION - Any AWS region where you have your 
* SEND - sender email address (verified via AWS SES)
* RECIPIENT - receiver email address (verified via AWS SES)
* GIT - git repo (hard code it)

## Usage

Option 1:
  * Download an interpreter such as pycharm [here](https://www.jetbrains.com/pycharm/download/download-thanks.html).
  * Setup python3 interpreter
  * Add environment variables in configurations
  
Option 2:
  * Create a .sh file with the above environment variables and run it or manually set each environment variable
  * Run the command<br/>python3 stock_monitor/stock_monitor.py
  
Option 3:
  * Install a docker and set the entry point to stock_monitor.py



Note: The code was built from the scratch but it was built with an intention to share knowledge and for educational purpose.<br/>Parts of the code can be easily hard coded but left as env to increase redundancy.<br/>The application is extremely customizable so remove/add files or part of code where ever unnecessary.
