# -*- coding: utf-8 -*-
"""
Created on Sat May 15 16:39:19 2021

@author: HP
"""

#python 3 program to illustrate store efficiently using pickle module
#Module translates an in-memory python object into serialized byte stream
#a string of bytes that can be written to any file like object

import pickle
def storeData():
    #initializing data to be stored in db
    Omar = {'Key':'Omar', 'name': 'Omar Bongo', 'age':90, 'pay':40000}
    Mobutu = {'Key':'Mobutu', 'name': 'Mobutu Sese Seko', 'age':98, 'pay':50000}
    Bokasa = {'Key':'Bokasa', 'name': 'Jean-Bedel Bokassa', 'age':98, 'pay':45000}
    
    #database
    db={}
    db['Omar']=Omar
    db['Mobutu']=Mobutu
    db['Bokasa']=Bokasa
    
    #its important to use binary mode
    dbfile=open('dictatorPickle', 'ab')
    
    #source, destination
    pickle.dump(db, dbfile)
    dbfile.close()
    
    
def loadData():
    #for reading also binary mode is important
    dbfile=open('dictatorPickle', 'rb')
    db=pickle.load(dbfile)
    for keys in db:
        print(keys, '=>', db[keys])
    dbfile.close()
    
    
if __name__=='__main__':
    storeData()
    loadData()
    