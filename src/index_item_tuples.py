#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 7, 2014

@author: anroco

How to get the index of a item of tuple in python?

¿Como obtener el indice de una tupla en python?
'''

#create a tuple
tupla = tuple('index tuple')
print(tupla)

#get index of the first item whose value is passed as parameter
index = tupla.index('e')
print (index)

#define the index from which you want to search
index = tupla.index('e', 4)
print (index)

#define the segment of the tuple to be searched
index = tupla.index('d', 2, 5)
print (index)

#if item not exists in the tuple return ValueError Exception
index = tupla.index('z')
