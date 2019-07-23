"""
Assignment 02
=============

The goal of this assignment is to implement synchronous scraping using standard python modules,
and compare the scraping speed to asynchronous mode.

Run this code with

    > fab run assignment02.py
"""

import urllib.request
from pathlib import Path
import csv
from tqdm import tqdm
import sys
import config as cfg
from yahoo import read_symbols, YAHOO_HTMLS

def scrape_descriptions_sync():
    """Scrape companies descriptions synchronously."""
    # TODO: Second assignment. Use https://docs.python.org/3/library/urllib.html

    symbols = read_symbols()
    progress = tqdm(total=len(symbols), file=sys.stdout, disable=False)
    YAHOO_HTMLS.mkdir(parents=True, exist_ok=True)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15',
    }

    for symbol in range(1, len(symbols)):
        url = 'https://finance.yahoo.com/quote/{symbol}/profile?p={symbol}'
        req = urllib.request.Request(url, headers = headers)
        resp = urllib.request.urlopen(req)
        respData = resp.read()
        saveFile = open(YAHOO_HTMLS /f'{symbol}.html', 'wb')
        saveFile.write(respData)
        saveFile.close()
        #except Exception as e:
         #   print(str(e))


def main():
    scrape_descriptions_sync()


if __name__ == '__main__':
    main()
