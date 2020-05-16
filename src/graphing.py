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
from numpy.polynomial import Polynomial

def wordshifter(i):
    iValence,iFvec = emotion(i,labMT,shift=True,happsList=labMTvector)
    iStoppedVec = stopper(iFvec,labMTvector,labMTwordList,stopVal=1.0)
    return(emotionV(iStoppedVec,labMTvector))
def scriptscrape(filename):
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    plotlist=[]
    for i in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(i) 
        x = pageObj.extractText()
        x= re.sub('\d+\s\d+\S\d+\S\d+,\d+\s\S+\s\d+\S\d+\S\d+,\d+','\n',x)
        x= re.sub('<\S+\s+\S+>','\n',x)
        #for row in x.split('\n'):
        #    plotlist.append(wordshifter(row))
        plotlist.append(wordshifter(x))
    return(plotlist)
def flatlist(plotlist):
    flat_list = [item for sublist in plotlist for item in sublist]
    return(flat_list)
def consolidate(fn):
    plist=[]
    x=os.getcwd()
    directory_in_str= f'{x}\\transcripts\\'
    directory = os.fsencode(directory_in_str)           #defines directory as indicated string
    os.chdir(directory)                                 #navigate to directory specified
    for file in os.listdir(directory):                  #iterates over all the files here
        filename = os.fsdecode(file)                    #specifies filename from file
        if filename.startswith(fn):                  #isolates epub for further action
            #print(filename)
            plist.append(scriptscrape(filename))
    plist = flatlist(plist)
    return(plist)
def relative(flat_list):
    flat_list = [x-(sum(flat_list)/len(flat_list)) for x in flat_list]
    return(flat_list)
def displayer(plotlist3,title):
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
if __name__=="__main__":
    lang = 'english'
    labMT,labMTvector,labMTwordList = emotionFileReader(stopval=0.0,lang=lang,returnVector=True)
