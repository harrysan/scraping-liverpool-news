# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 22:11:56 2021

@author: Harry
"""

import requests
#import cssutils
from bs4 import BeautifulSoup
import json

class Okezone:
    
    #output=[]
    
    def scrapbola2(self):

        sjson = {}
        sjson = []
        
        URL = self.URL
        page = requests.get(URL)
        
        soup = BeautifulSoup(page.content, 'html.parser')
        
        #print(soup)
        
        results = soup.find("div", {"class": "col-md-7 col-sm-7 right"})
        count = 0
        results2 = results.findAll("div", {"class": "tag-wrapper"})
        
        for results in results2:
            judul = results.find("div", {"class": "quotes"})
            judul1 = judul.find("a", {"class": "ga_BreakingMore"}).text
            
            try:
                gambar = results.find("div", class_="gambar-head")['style']
                gambar1 = gambar.split("('", 1)[1].split("')")[0]
            except:
                gambar1 = 'no image'
            
            link = results.find('a').get('href')
            
            try:
                waktu = results.find("div", {"class": "media-time"}).getText()
            except:
                waktu = 'no time'
                
            try:
                desc = results.find('p').getText()
            except:
                desc = 'no desc'
            
            count = count+1
            
            judul1 = judul1.replace('\n','')
            gambar1 = gambar1.replace('\n','')
            link = link.replace('\n','')
            waktu = waktu[1:].replace('\n','')
            desc = desc.replace('\n','')
            
            #print("Berita " + str(count))
            #print(judul1.replace('\n',''))
            #print(gambar1.replace('\n',''))
            #print(link.replace('\n',''))
            #print(waktu[1:].replace('\n',''))
            #print(desc.replace('\n',''))
            #print(" ")
            
            sjson.append({"judul":judul1,"gambar":gambar1,"desc":desc,"waktu":waktu,"link":link})
            
        output = json.dumps(sjson)
        return output


    # init method or constructor    
    def __init__(self, url):   
        self.URL = url
        
okezone = Okezone('https://www.okezone.com/tag/liverpool')
output2 = okezone.scrapbola2()
#print(kompas.scrapbola())
