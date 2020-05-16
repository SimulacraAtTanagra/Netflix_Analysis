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
def dfranked(df):
    ia=IMDb()
    df['rank']=df.title.apply(ranksearch)
    df=df[['title','listed_in','type','rank']]
    df.columns=['title','genre','type','rank']
    return(df)