# -*- coding: utf-8 -*-
"""
Created on Sun May 10 15:16:21 2020

@author: shane
"""

import pandas as pd
import matplotlib.pyplot as plt
from math import ceil
import os
def genreident(x,i):
    if i in x.lower():
        return(i)
def isinhere(x):
    if x in df.title.unique():
        return("Yes")
def fixend(x):
    if x[-1]==" ":
        return(x[:-1])
    else:
        return(x)
cwd = os.getcwd()
df =pd.read_excel(f"{cwd}\\data\\originals.xlsx")
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
df.type= df.type.apply(fixend)
genres= pd.read_excel(f"{cwd}\\data\\genres.xlsx")
genres.columns=genres.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
genres = genres[genres.genre!="adventure"]
genres = genres[genres.genre!="independent"]
for i in genres.genre.unique():
    df[f'{i}']= df.genre.apply(genreident,args=[i])
    
counts= []
for i in genres.genre.unique():    
    x = df[df[f'{i}'].isnull()==False].shape[0]
    counts.append(x)
y = list(genres.genre.unique())
cntdf = pd.DataFrame(counts) 
cntdf[1]=y
cntdf= cntdf.sort_values(by=[0],ascending=False)
cntdf.columns = ['num','genre']

axes = plt.figure().add_subplot(111)
plt.bar(list(cntdf.genre.values)[:5],[ceil((x/df.shape[0])*100) for x in list(cntdf.num.values)[:5]])
plt.title('Top 5 genres for Originals as % of Originals')
label = ["Comedy","Drama","Documentary","Animation","Thriller"]
a=axes.get_xticks()
a = label
axes.set_xticklabels(a)
plt.xticks(rotation='vertical')
plt.show()

total =pd.read_excel(f"{cwd}\\data\\ratings.xlsx")

for i in genres.genre.unique():
    total[f'{i}']= total.genre.apply(genreident,args=[i])
total['original'] = total.title.apply(isinhere)

cnt = []
for i in genres.genre.unique():    
    x = total[total[f'{i}'].isnull()==False].shape[0]
    cnt.append(x)

cntdf2 = pd.DataFrame(cnt) 
cntdf2[1]=y
cntdf2= cntdf2.sort_values(by=[0],ascending=False)
cntdf2.columns = ['num','genre']
  
axes = plt.figure().add_subplot(111)      
plt.bar(list(cntdf2.genre.values)[:5],[ceil((x/total.shape[0])*100) for x in list(cntdf2.num.values)[:5]])
plt.title('Top 5 genres overall as % of Catalog')
label = ["Drama","Comedy","Documentary","Action","Romance"]
a=axes.get_xticks()
a = label
axes.set_xticklabels(a)
plt.xticks(rotation='vertical')
plt.show()

typevals= [total[total.type=="TV Show"].shape[0],total[total.type!="TV Show"].shape[0]]
typetypes = ['Serials','Movies']

fig1, ax1 = plt.subplots()
explode = (0, 0.1) 
ax1.pie(typevals, explode=explode, labels=typetypes, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('% of Catalog by Type')
plt.show()


otypes = []
ovals = []
for i in df.type.unique():
    ovals.append(df[df.type==i].shape[0])
    otypes.append(i)


fig1, ax1 = plt.subplots()
explode = (.2, .2,.2,.2) 
ax1.pie(ovals, explode=explode, labels=otypes, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('% of Originals by Type')
plt.show()

ocomp =  [total[total.original.isnull()==False].shape[0],total[total.original.isnull()==True].shape[0]]
oname = ['Original', 'Leased']

fig1, ax1 = plt.subplots()
explode = (0, 0.1) 
ax1.pie(ocomp, explode=explode, labels=oname, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('% of Catalog by Type')
plt.show()

origplt = [total[total.original.isnull()==False]['rank'].mean(),total[total.original.isnull()==False]['rank'].median(),total[total.original.isnull()==False]['rank'].mode()[0]]

nonorigplt = [total[total.original.isnull()==True]['rank'].mean(), total[total.original.isnull()==True]['rank'].median(), total[total.original.isnull()==True]['rank'].mode()[0]]
axes = plt.figure().add_subplot(111)   
plt.scatter([i for i in range(len(origplt))],origplt,label=' Netflix Originals')
plt.plot([i for i in range(len(origplt))],origplt)
plt.scatter([i for i in range(len(nonorigplt))],nonorigplt,label='Others')
plt.plot([i for i in range(len(nonorigplt))],nonorigplt)
plt.legend()
label = ["Mean","Median","Mode"]
plt.title("iMDb Score Analysis")
#axes.xaxis.set_minor_locator(plt.MaxNLocator(3))
plt.xticks([0,1,2])
#plt.locator_params(numticks=3)
a=axes.get_xticks()
a = label
axes.set_xticklabels(a)
plt.show()