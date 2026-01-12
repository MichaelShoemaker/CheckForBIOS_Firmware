#!/usr/bin/python3
import os
import json
import sys
import requests
import urllib3
import traceback
from secrets import slack_hook
from bs4 import BeautifulSoup

# Send Slack notification based on the given message
def slack_notification(message, webhook_url):
    try:
        slack_message = {'text': message}

        http = urllib3.PoolManager()
        response = http.request('POST',
                                webhook_url,
                                body = json.dumps(slack_message),
                                headers = {'Content-Type': 'application/json'},
                                retries = False)
    except:
        traceback.print_exc()

    return True

def check_bios():
    CURRENT_BIOS = 'F63c'

    url="https://www.gigabyte.com/Motherboard/B450-AORUS-PRO-WIFI-rev-1x/support#Support-Bios"


    # Make a GET request to fetch the raw HTML content
    resp = requests.get(url, headers = {"User-Agent":"joe-mama"})

    web_hook = slack_hook()    

    html_content = resp.text
    soup = BeautifulSoup(html_content, "lxml")
    mydivs = soup.find_all("div", class_="div-table-cell download-version")
    for tag in mydivs:
        if 'F' in tag.text:
            if tag.text.strip() > CURRENT_BIOS:
                
                message =  f"You are currently on version {CURRENT_BIOS}, but {tag.text.strip()} is available"

                webhook_url = web_hook

                slack_notification(message, webhook_url)

    

if __name__=='__main__':
    check_bios()
