# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 09:17:04 2020

@author: shane
"""
from imdb import IMDb
import pandas as pd
import json
from pandas.io.json import json_normalize


def ranksearch(i):
    try:
        x= ia.search_movie(i)
        try:
            y=(x[0].movieID)
            z = ia.get_movie(int(y))
            return(z.data['rating'])
        except:
            pass
    except:
        pass
#this function pulls full synopsis if on imdb as string
#this can be used as a feeder for the graphing function to scrape storylines
def pullsynopsis(i):    
    try:
        x= ia.search_movie(i)
        try:
            y=(x[0].movieID)
            z = ia.get_movie(int(y))
            return(z.get('synopsis')[0])
        except:
            pass
    except:
        pass

def dfranked(df):
    ia=IMDb()
    df['rank']=df.title.apply(ranksearch)
    #df['fulltext']=df.title.apply(pullsynopsis)
    df=df[['title','listed_in','type','rank']]
    df.columns=['title','genre','type','rank']
    return(df)