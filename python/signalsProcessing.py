"""
    Retreive signal API
    author: Noureddine AYAD
    date=27 april 2023 
"""
#! /usr/bin/env python

import pandas as pd                                      
import csv, sys
import re

""" function : create  signals' dictionnary
{
 node_id: {'sampling_interval_ms': 00 , 'deadband_value': '', 'deadband_type': '', 'active': 0, keywords : [...] }
} """
def getSignals(signalsFileFullPath, keywordsFileFullPath):

    signals={}
    keywords={}
    if (signalsFileFullPath != "" and keywordsFileFullPath != ""):
        with open(signalsFileFullPath, newline='') as signalsCsv:
            reader = csv.DictReader(signalsCsv)
            #header = next(reader) # the first line in the header
            try:
                for row in reader:
                    node_id=row['node_id'][33:]
                    row.pop('node_id')
                    keywords=row['keywords']
                    if (keywords is not None):
                        names=getNames(keywords, keywordsFileFullPath)
                        row['keywords']=names
                    signals[node_id]= row
                    
            except csv.Error as e:
                sys.exit('file {}, line {}: {}'.format(signalsCsv, reader.line_num, e))
        return signals
    else:
        return "File(s) path(s) not valid...!!!"

""" function : create a keywords dictionnary
{
   id: {'name': 'name' , 'descrition': 'description' }
} """
def getKeywordsDico(keywordsFullPath):

    dico={}
    with open(keywordsFullPath, newline='') as keywordsFileCsv:
        reader = csv.DictReader(keywordsFileCsv)
        try:
            for row in reader:
                id=int(row['id'])
                row.pop('id')
                dico[id]= row 
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(keywordsFullPath, reader.line_num, e))

    return (dico)

# get Keywords names instead of ids
def getNames(keywords, keywordsFileFullPath ):
    keywordsDico=getKeywordsDico(keywordsFileFullPath)
    #ids=keywords.split(";")
    ids= re.findall(r'\d+',keywords)
    names=[]
    for id in ids:
        name= keywordsDico[int(id)]['name'] 
        names.append(name)
    return (names)


