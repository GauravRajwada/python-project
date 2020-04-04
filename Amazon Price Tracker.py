# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:53:36 2020

@author: Gaurav
"""


import requests
from bs4 import BeautifulSoup
import smtplib
url='https://www.amazon.in/Test-Exclusive-629/dp/B07HGLB1TJ/ref=sr_1_1_sspa?keywords=m30s&qid=1579894193&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyMDNXTlNMTDdDWlZSJmVuY3J5cHRlZElkPUEwNjAxNjMyMk1MWjc5RVNRQlFCUyZlbmNyeXB0ZWRBZElkPUEwMjczNzQ2MkZGTFFBSUc5SldPRyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

headers={'user-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

def check_price():

    page=requests.get(url, headers=headers)

    soup=BeautifulSoup(page.content,'html.parser')
    print(soup.prettify())

    title=soup.find(id="productTitle").get_text()
    price=soup.find(id="priceblock_ourprice").get_text()

    #converted_price=float(price[:-3])
    #Unable to convert string to FLoat so that i have used this
    converted_price=5
    if(converted_price<11500):
        send_mail()
    print(title.strip())
    print(price.strip())

    if(converted_price>111):
        send_mail()

def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('sintg1999@gmail.com','hkrzpehqchwbdvbo')

    subject='Price has fall down'
    body='Check amazon link https://www.amazon.in/Test-Exclusive-629/dp/B07HGLB1TJ/ref=sr_1_1_sspa?keywords=m30s&qid=1579894193&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyMDNXTlNMTDdDWlZSJmVuY3J5cHRlZElkPUEwNjAxNjMyMk1MWjc5RVNRQlFCUyZlbmNyeXB0ZWRBZElkPUEwMjczNzQ2MkZGTFFBSUc5SldPRyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

    msg=f"subject:{subject}\n\n{body}"
    server.sendmail(
        'sintg1999@gmail.com',
        'sinyash2000@gmail.com',
        msg
    )
    print("Hey email has been send")

    server.close()
check_price()