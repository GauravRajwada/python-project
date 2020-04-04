# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 16:08:54 2020

@author: Gaurav
"""
from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def getdata(url):
    r= requests.get(url)
    return r.text



def notifyme(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon="covid 19.ico",
        timeout=4
        
   )
if __name__=="__main__":
    # notifyme("Gaurav", "One more")
    while True:
        myhtmldata=getdata("https://www.mohfw.gov.in/")
        # print(myhtmldata)
        soup=BeautifulSoup(myhtmldata,"html.parser")
        print(soup.prettify())
        mydata=""
        
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            mydata+=tr.get_text()
        mydata=mydata[1:]
        itemlist=mydata.split("\n\n")
        state=["Uttar Pradesh","Delhi","Kerala","Maharashtra"]
        for i in itemlist[0:30]:
            datalist=i.split("\n")
            if datalist[1] in state:
                print(datalist)
                ntitle="Cases of Covid-19"
                ntext=f"State: {datalist[1]}\nTotal Cases: {datalist[2]} & Cured: {datalist[3]}\nDeath: {datalist[4]}\n"
                notifyme(ntitle,ntext)
                time.sleep(4)
        time.sleep(20)