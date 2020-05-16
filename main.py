# -*- coding: utf-8 -*-
"""
Created on Sat May 16 15:14:25 2020

@author: shane
"""

# %%

import pandas as pd
import os
from src.simmonssummary1 import simmonscleaner as sc
from src.simmonssummary1 import grouping as gp
from src.simmonssummary1 import summaryfunc as sf
from src.movierankscraper import dfranked
from src.graphing import consolidate as con
from src.graphing import displayer as disp

# %%

cwd=os.getcwd()
#sorting through the simmons data
simmons = pd.read_excel(f'{cwd}\\data\\SimmonsResearch-OneView.xlsx')
simmons =sc(simmons)

# %%

#taking a look at a profile of a user for one of the several brands in the dataset
sf(simmons,gp(simmons)[0])

# %%

#generating ranking data by looking at netflix's catalog listings in imdb
rankings = pd.read_csv(f'{cwd}\\data\\netflix_titles.csv')
rankings=dfranked(rankings)

# %%

#analyzing and displaying summary data about genre composition and imdb ratings
#though we generated ranking data in a df, it already exists in a file
import src.display

# %%

#Showing story curves for the material we havein transcripts
disp(con("Tiger-King"),"Tiger King Sentiment")

# %%

disp(con("BIRD BOX"),"Bird Box Sentiment")

# %%

disp(con("Awakens"),"Star Wars: The Force Awakens Sentiment")