# -*- coding: utf-8 -*-
"""
Created on Sat May 16 15:14:25 2020

@author: shane
"""
import pandas as pd
import os
from src.simmonssummary1 import simmonscleaner as sc
from src.simmonssummary1 import summaryfunc as sf
from src.movierankscraper import dfranked
from src.graphing import scriptscrape as ss
from src.graphing import consolidate as con
from src.graphing import displayer as disp

cwd=os.getcwd()
simmons = pd.read_excel(f'{cwd}\\data\\SimmonsResearch-OneView.xlsx')
simmons =sc(simmons)
sf(simmons)



import src.display