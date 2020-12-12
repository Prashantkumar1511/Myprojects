# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 14:33:39 2020

@author: prashant sehrawat
"""
from bs4 import BeautifulSoup
import requests
import csv


source=requests.get('https://www.brainyquote.com/')
src=source.content

soup=BeautifulSoup(src,'lxml')

csv_file=open('author.csv','w')

csv_writer=csv.writer(csv_file)
csv_writer.writerow(['authors','Quotes'])



for a in soup.find_all('a','bq_on_link_cl'):
    author=a.text
    print(author)
    
    newlink="https://www.brainyquote.com/" + a.get('href')
    source1=requests.get(newlink)
    src1=source1.content
    soup1=BeautifulSoup(src1,'lxml')
    quote=soup1.find_all('a',"oncl_q")
    for images in quote:
        csv_writer.writerow([author,images.text])
        
        
    
   # print(linktext)
            
   
csv_file.close()    

    
    
