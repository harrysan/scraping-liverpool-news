# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup
import json

class Bolanet:
    
    #output=[]
    
    def scrapbola(self):

        sjson = {}
        sjson = []

        URL = self.URL
        page = requests.get(URL)
        
        soup = BeautifulSoup(page.content, 'html.parser')
        
        #print(soup)
        
        results = soup.find("div", {"class": "newslist"})
        
        #pertama atas
        atas = results.find("div", {"class": "item_hl"})
        judul1 = atas.find('h2').text
        gambar1 = atas.find('img')
        #desc1 = atas.find('p', attrs={'class' : 'syn'}).getText()
        waktu1 = atas.find("div", {"class": "info"})
        link1 = waktu1.find('a').get('href')
        
        #fix
        judul1 = judul1.replace('\n','')
        gambar1 = gambar1['src'].replace('\n','')
        waktu1 = waktu1.getText().replace('\n','')
        link1 = link1.replace('\n','')
        
        #dict1[0] = {judul1,gambar1,'null',waktu1,link1}
        sjson.append({"judul":judul1,"gambar":gambar1,"desc":'null',"waktu":waktu1,"link":link1})
        
        #print("Berita 1")
        #print(judul1.replace('\n',''))
        #print(gambar1['src'].replace('\n',''))
        #print(waktu1.getText().replace('\n',''))
        #print(link1.replace('\n',''))
        #print(" ")
        
        #sisanya dibawah
        count = 1
        
        results2 = results.findAll("div", {"class": "item"})
        for results in results2:
            judul = results.find("a", {"class": "ntitle"})
            gambar = results.find('img')
            #desc = atas.find('p', attrs={'class' : 'syn'}).getText()
            waktu = results.find("div", {"class": "info"})
            link = waktu.find('a').get('href')
            
            #fix
            judul = judul.getText().replace('\n','')
            gambar = gambar['src'].replace('\n','')
            link = link.replace('\n','')
            waktu = waktu.getText().replace('\n','')
            
            sjson.append({"judul":judul,"gambar":gambar,"desc":'no desc',"waktu":waktu,"link":link})
            
            count = count+1
            
            #print("Berita " + str(count))
            #print(judul.getText().replace('\n',''))
            #print(gambar['src'].replace('\n',''))
            #print(link.replace('\n',''))
            #print(waktu.getText().replace('\n',''))
            #print(" ")
            
            if count==10:
                break
            
        #print(sjson)
        output = json.dumps(sjson)
        return output


    # init method or constructor    
    def __init__(self, url):   
        self.URL = url
        
bolanet = Bolanet('https://www.bola.net/tag/liverpool/')
output = bolanet.scrapbola()
#print(bolanet.scrapbola())