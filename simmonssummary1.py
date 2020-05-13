# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 01:06:44 2020

@author: shane
"""

import pandas as pd
import re 
find = re.compile(r"^([^:]*):*")
def stringer(x):
    try:
        return(x.split(':')[0])
    except:
        return(x)
def stringer2(x):
    try:
        return(x.split(':')[1])
    except:
        return(x)


'''
list1= ['total','AMAZON PAYG','AMAZON PRIME','CRACKLE','GOOGLE PLAY','HULU PAID',
        'HULU FREE',',ITUNES','NETFLIX','SLING TV','VUDU','SATELITE',
        'CABLE','OTHER','NOTA']

list2=['_sample','_weighted_sample','_vert_perc','_horiz_perc','_index']
list3= []
for i in list1:
    for b in list2:
        list3.append(f'{i}{b}')
        
#this was to create the column names because simmons sucks are tabular data output
'''

df =pd.read_excel('c://users//shane//downloads//SimmonsResearch-OneView.xlsx')
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

df.columns = (['category', 'total_sample', 'total_weighted_sample', 'total_vert_perc',
 'total_horiz_perc', 'total_index', 'AMAZON PAYG_sample', 'AMAZON PAYG_weighted_sample',
 'AMAZON PAYG_vert_perc', 'AMAZON PAYG_horiz_perc', 'AMAZON PAYG_index', 'AMAZON PRIME_sample',
 'AMAZON PRIME_weighted_sample', 'AMAZON PRIME_vert_perc', 'AMAZON PRIME_horiz_perc', 'AMAZON PRIME_index',
 'CRACKLE_sample', 'CRACKLE_weighted_sample', 'CRACKLE_vert_perc', 'CRACKLE_horiz_perc',
 'CRACKLE_index', 'GOOGLE PLAY_sample', 'GOOGLE PLAY_weighted_sample', 'GOOGLE PLAY_vert_perc',
 'GOOGLE PLAY_horiz_perc', 'GOOGLE PLAY_index', 'HULU PAID_sample', 'HULU PAID_weighted_sample',
 'HULU PAID_vert_perc', 'HULU PAID_horiz_perc', 'HULU PAID_index', 'HULU FREE_sample',
 'HULU FREE_weighted_sample', 'HULU FREE_vert_perc', 'HULU FREE_horiz_perc', 'HULU FREE_index',
 'ITUNES_sample', ',ITUNES_weighted_sample', 'ITUNES_vert_perc', 'ITUNES_horiz_perc',
 'ITUNES_index', 'NETFLIX_sample', 'NETFLIX_weighted_sample', 'NETFLIX_vert_perc',
 'NETFLIX_horiz_perc', 'NETFLIX_index', 'SLING TV_sample', 'SLING TV_weighted_sample',
 'SLING TV_vert_perc', 'SLING TV_horiz_perc', 'SLING TV_index', 'VUDU_sample',
 'VUDU_weighted_sample', 'VUDU_vert_perc', 'VUDU_horiz_perc', 'VUDU_index',
 'SATELITE_sample', 'SATELITE_weighted_sample', 'SATELITE_vert_perc', 'SATELITE_horiz_perc',
 'SATELITE_index', 'CABLE_sample', 'CABLE_weighted_sample', 'CABLE_vert_perc',
 'CABLE_horiz_perc', 'CABLE_index', 'OTHER_sample', 'OTHER_weighted_sample',
 'OTHER_vert_perc', 'OTHER_horiz_perc', 'OTHER_index', 'NOTA_sample',
 'NOTA_weighted_sample', 'NOTA_vert_perc', 'NOTA_horiz_perc', 'NOTA_index'])
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
titlegroups= [x for x in df.columns if x.endswith("perc")][2:]
titlehorz= [x for x in titlegroups if "horiz" in x]
titlevert= [x for x in titlegroups if "vert" in x]
titlegroups[0][-10:]
find = re.compile(r"^([^:]*).*")
df['type'] = df.category.apply(stringer)
df['subtype'] = df.category.apply(stringer2)
with open('c://users/shane//downloads//newoutput.txt','w') as f:
    for y in titlehorz:
        for i in df.type.unique():
            x = df[df.type==i][f'{y}'].max()
            try:
                v=df[df.type==i][df[f'{y}']>=x].subtype.values[0]
            except:
                v=df[df.type==i][df[f'{y}']>=x].subtype
            print(f'In the category of {i}, {v} has most horizontal percentage',file=f)
        print(f"This concludes the segment of analysis for {y[:-10]}",file=f)

    for z in titlevert:
        for i in df.type.unique():
            x = df[df.type==i][f'{z}'].max()
            try: 
                v= df[df.type==i][df[f'{z}']>=x].subtype.values[0]        
            except:
                v= df[df.type==i][df[f'{z}']>=x].subtype
            print(f'In the category of {i}, {v} has most vertical percentage',file=f)
        print(f"This concludes the segment of analysis for {z[:-10]}",file=f)
