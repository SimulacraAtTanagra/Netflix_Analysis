# -*- coding: utf-8 -*-
"""
Created on Mon May 11 19:45:09 2020

@author: shane
"""

from labMTsimple.storyLab import *
import re
import matplotlib.pyplot as plt
from matplotlib import animation
import PyPDF2 
import os

#from storyLab import*

saturday ="Good god almighty, great balls of fire. Ain't this just the best damn day god did ever put into existence?"
sunday = "Goddamn it if another one o these children steps on my lawn, I swear to almighty christ I'll kill them"
list1= [saturday,sunday]
lang = 'english'
labMT,labMTvector,labMTwordList = emotionFileReader(stopval=0.0,lang=lang,returnVector=True)
list2=[]
def wordshifter(i):
    iValence,iFvec = emotion(i,labMT,shift=True,happsList=labMTvector)
    iStoppedVec = stopper(iFvec,labMTvector,labMTwordList,stopVal=1.0)
    return(emotionV(iStoppedVec,labMTvector))
def graphit(filename,title):
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    plotlist3=[]
    for i in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(i) 
        x = pageObj.extractText()
        x= re.sub('\d+\s\d+\S\d+\S\d+,\d+\s\S+\s\d+\S\d+\S\d+,\d+','\n',x)
        x= re.sub('<\S+\s+\S+>','\n',x)
        #for row in x.split('\n'):
        #    plotlist.append(wordshifter(row))
        plotlist3.append(wordshifter(x))
    #plotlist3 = [x-(sum(plotlist3)/len(plotlist3)) for x in plotlist3]
    plt.figure(figsize=(12,4))
    y=plotlist3
    x=[(x/len(plotlist3))*100 for x  in range(len(plotlist3))]
    #plt.plot(x, y,alpha=.5)
    plt.title(title)
    plt.ylabel("Sentiment of dialog relative to mean")
    plt.xlabel("Percent of Movie")
    p = Polynomial.fit(x, y, 30)
    plt.plot(*p.linspace())
    plt.show()
graphit('c:\\users\\shane\\downloads\\BIRD BOX by Eric Heisserer.pdf',"Bird Box Sentiment")
graphit('c:\\users\\shane\\downloads\\Blake Crouch - Dark Matter-Crown (2016).pdf',"Dark Matter")
    
plotlist=[]
plotlist2=[]

directory_in_str = 'c:\\users\\shane\\downloads\\'
directory = os.fsencode(directory_in_str)           #defines directory as indicated string
os.chdir(directory)                                 #navigate to directory specified
for file in os.listdir(directory):                  #iterates over all the files here
    filename = os.fsdecode(file)                    #specifies filename from file
    if filename.startswith("Tiger-King"):                  #isolates epub for further action
        #print(filename)
        
        pdfFileObj = open(filename, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
        plotlist2=[]
        for i in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(i) 
            x = pageObj.extractText()
            x= re.sub('\d+\s\d+\S\d+\S\d+,\d+\s\S+\s\d+\S\d+\S\d+,\d+','\n',x)
            x= re.sub('<\S+\s+\S+>','\n',x)
            #for row in x.split('\n'):
            #    plotlist.append(wordshifter(row))
            plotlist2.append(wordshifter(x))
        plotlist.append(plotlist2)
        plotlist2 = [x-(sum(plotlist2)/len(plotlist2)) for x in plotlist2]
        
        plt.plot([(x/len(plotlist2))*100 for x  in range(len(plotlist2))],plotlist2)
        plt.title("Tiger King, Episode 7")
        plt.ylabel("Sentiment of dialog relative to mean")
        plt.xlabel("Percent of Episode")
        plt.show()

flat_list = [item for sublist in plotlist for item in sublist]
flat_list = [x-(sum(flat_list)/len(flat_list)) for x in flat_list]
import numpy
import matplotlib.pyplot as plt
plt.figure(figsize=(12,4))
y=flat_list
x=[(i/len(flat_list))*100 for i  in range(len(flat_list))]
plt.plot(x, y,alpha=.5)
from numpy.polynomial import Polynomial
plt.title("Tiger King Series Sentiment")
plt.ylabel("Sentiment of dialog relative to mean")
plt.xlabel("Percent of Series")
p = Polynomial.fit(x, y, 30)
plt.plot(*p.linspace())
plt.show()
#this gives us the file for tiger king series sentiment, next is star wars




'''
plt.figure(figsize=(12,4))
plt.scatter([(x/len(flat_list))*100 for x  in range(len(flat_list))],flat_list,s=1,alpha=.5)
plt.plot([(x/len(flat_list))*100 for x  in range(len(flat_list))],flat_list,alpha=.4)
plt.title("Tiger King Series Sentiment")
plt.ylabel("Sentiment of dialog relative to mean")
plt.xlabel("Percent of Series")
plt.show()
'''     
fig, ax1 = plt.subplots(1,figsize=(12,6))
for i in plotlist:
    ax1.plot([(x/len(i))*100 for x  in range(len(i))],i)
else:
    plt.show()
pltlist = [x for x in plotlist]
'''
fig = plt.figure()
ax = plt.axes()
line, = ax.plot([], [], lw=3)
def init():
    line.set_data([], [])
    return line,
def updatefig(i):
    x= pltlist[i]
    y = [(o/len(x))*100 for o in range(len(x))]
    line.set_data(x, y)
    return line,    
ani = animation.FuncAnimation(fig, updatefig, init_func=init,frames=200, interval=20, blit=True)
plt.show()
'''
#pltlist = iter(pltlist)
'''while (1) : 
    val = next(pltlist,'end') 
    if val == 'end': 
        print ('list end') 
        break
    else : 
        print (val) '''
#pdfFileObj = open('c:\\users\\shane\\downloads\\BIRD BOX by Eric Heisserer','rb')
  
# creating a page object 

# extracting text from page 
# closing the pdf file object 
#pdfFileObj.close() 
plotlist2 = [x-(sum(plotlist2)/len(plotlist2)) for x in plotlist2]


plotlist = [x for x in plotlist if x>0]
plt.scatter(range(len(plotlist)),plotlist)
plt.show()
#plt.scatter([(x/len(plotlist))*100 for x  in range(len(plotlist))],plotlist)
plt.plot([(x/len(plotlist))*100 for x  in range(len(plotlist))],plotlist)
plt.show()
list14=[]
#plt.scatter([(x/len(plotlist2))*100 for x  in range(len(plotlist2))],plotlist2)
list14.append(plt.plot([(x/len(plotlist2))*100 for x  in range(len(plotlist2))],plotlist2))
plt.show()

for i,x in enumerate(list14):
    list14[i]
    plt.show()
    
    
]