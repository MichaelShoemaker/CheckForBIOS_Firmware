#!/usr/bin/python3
import os
import sys

import requests
from bs4 import BeautifulSoup


def check_bios():
    CURRENT_BIOS = 'F62d'

    url="https://www.gigabyte.com/Motherboard/B450-AORUS-PRO-WIFI-rev-1x/support#support-dl-bios"


    # Make a GET request to fetch the raw HTML content
    resp = requests.get(url)

    if resp.status_code != 200:
        os.system(f"notify-send 'BIOS CHECK FAIL' '{url} appears to be down'")
        sys.exit(1)

    html_content = resp.text
    soup = BeautifulSoup(html_content, "lxml")
    mydivs = soup.find_all("div", class_="div-table-cell download-version")
    for tag in mydivs:
        if 'F' in tag.text:
            if tag.text.strip() > CURRENT_BIOS:
                print(tag.text.strip())
                os.system(f"notify-send 'NEW BIOS AVAILABLE' 'You are currently on version {CURRENT_BIOS}\n, but {tag.text.strip()} is available'")


if __name__=='__main__':
    check_bios()