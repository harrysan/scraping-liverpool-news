# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 21:52:16 2021

@author: Harry
"""

import requests
from bs4 import BeautifulSoup
import json

class Detikcom:
    
    #output=[]
    
    def scrapbola1(self):

        sjson = {}
        sjson = []
        
        URL = self.URL
        page = requests.get(URL)
        
        soup = BeautifulSoup(page.content, 'html.parser')
        
        #print(soup)
        
        results = soup.find("div", {"class": "l_content"})
        
        #loop data
        count = 0
        results2 = results.findAll("article")
        
        for results in results2:
            judul = results.find('h2').text
            gambar = results.find('img')
            link = results.find('a').get('href')
            waktu = results.find("span", {"class": "date"})
            desc = results.find('p').getText()
            
            count = count+1
            
            judul = judul.replace('\n','')
            gambar = gambar['src'].replace('\n','')
            link = link.replace('\n','')
            waktu = waktu.getText().replace('Sepakbola','').replace('\n','')
            desc = desc.replace('\n','')
            
            sjson.append({"judul":judul,"gambar":gambar,"desc":desc,"waktu":waktu,"link":link})
            
            #print("Berita " + str(count))
            #print(judul.replace('\n',''))
            #print(gambar['src'].replace('\n',''))
            #print(link.replace('\n',''))
            #print(waktu.getText().replace('Sepakbola','').replace('\n',''))
            #print(desc.replace('\n',''))
            #print(" ")
            
        output = json.dumps(sjson)
        return output


    # init method or constructor    
    def __init__(self, url):   
        self.URL = url
        
detikcom = Detikcom('https://www.detik.com/tag/liverpool/?_ga=2.51486254.603129991.1615215012-794638011.1605885810')
output1 = detikcom.scrapbola1()
#print(detikcom.scrapbola())
