#! python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 15:40:54 2017

@author: JBC4


"""

import requests, bs4, re

the_guardian = 'https://www.theguardian.com/us'
res = requests.get(the_guardian)
res.raise_for_status()
weatherSoup = bs4.BeautifulSoup(res.text, "lxml")
a = weatherSoup.select('div.fc-item__container')

printString = re.sub('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n','',a[0].text)
printString = re.sub('\n\n\n\n\n\n\n','\n',printString)
printString = re.sub('\n\n\n\n\n\n','\n',printString)
printString = re.sub('\n\n\n\n','\n',printString)
printString = re.sub('\n\n\n','\n',printString)
printString = re.sub(' \n ','\n',printString)
print('\n********Headlines from the Guardian*********')
print(printString)


BBCtopten = 'https://www.bbc.com/news/popular/read'
res = requests.get(BBCtopten)
res.raise_for_status()
weatherSoup = bs4.BeautifulSoup(res.text, "lxml")
a = weatherSoup.select('#comp-most-popular')
#b = weatherSoup.select('.myforecast-current-lrg')
#temperature = b[0].getText()
print('******Top 10 Stories on BBC********')
printString = re.sub('\n\n','',a[0].text)
printString = re.sub('Most Read','',printString)
printString = re.sub('\n\n','',printString)

#newlinesinserted = re.sub(r"([1-10]+\w)", r"\n \1:  \w", printString)
#for i in range (1,10):
#    printString = printString.replace(str(i), "\n%s" % str(i))
    
print(printString)

                       
                       
