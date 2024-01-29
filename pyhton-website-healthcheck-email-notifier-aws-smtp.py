import subprocess
import requests
import time
import os
import urllib.request

url = 'https://<url-to-be-checked>/'

def send_mail():
    sender_email = "sender@expample.com"
    recipient_email = "recevier@expample.com"
    subject = "URL Destination Unreachable"
    body = "The wedsite %s is down. Please contact the Ops Team"%url
    profile = "aws-profile"
    aws_region = "region-of-smtp"
    
    command = [
        "aws", "ses", "send-email",
        "--from", sender_email,
        "--destination", f"ToAddresses={recipient_email}",
        "--message", f"Subject={{Data={subject},Charset=UTF-8}},Body={{Text={{Data={body},Charset=UTF-8}}}}",
        "--profile", profile,
        "--region", aws_region
    ]

    try:
        # Run the AWS CLI command
        subprocess.run(command, check=True)
        print("Email sent successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print("Failed to send email.")

while True:
    try:
        status_code = urllib.request.urlopen(url).getcode()
        website_is_up = status_code == 200
        print("Destination Reachable")
    except:
        print("Destination Unreachable")
        send_mail()

    time.sleep(900)
