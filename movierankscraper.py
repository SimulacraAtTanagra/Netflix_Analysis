# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 09:17:04 2020

@author: shane
"""
from imdb import IMDb
import pandas as pd
import json
from pandas.io.json import json_normalize
import memedict as md

ia=IMDb()

collection = ia.search_movie('The Matrix')
for item in collection:
    print(item.movieID)
movie = ia.get_movie('00133093')
with open('c:\\users\\shane\\downloads\\newdata.txt','w') as f:
    print(movie.data, file=f)
print(movie.data['rating'])

df = pd.read_csv('c:\\users\\shane\\downloads\\netflix_titles.csv')
def ranksearch(i):
    try:
        x= ia.search_movie(i)
        try:
            y=(x[0].movieID)
            z = ia.get_movie(int(y))
            return(z.data['rating'])
        except:
            print(f"search for {i} went okay but didn't print")
    except:
        print(f"both search and print failed for {1}")


df['rank']=df.title.apply(ranksearch)
df.to_csv('c:\\users\\shane\\downloads\\netflix_w_rating.csv')
df.to_excel('c:\\users\\shane\\downloads\\netflix_w_rating.xls')



memebase = pd.read_json('c:\\users\\shane\\downloads\\dbjson\db.json')

memelist=[]
for i in memebase['_default'].values:
    memelist.append(i['title'])
memetext = []
for i in memelist:
    try:
        memetext.append(md.search(i))
    except:
        memetext.append('This meme was not found')
