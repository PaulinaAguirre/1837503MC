# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 16:14:31 2017

@author: Aguir
"""

q = []
for i in range(100):
    q.append(i)

import random
random.shuffle(q)

def minimo(arr):
    valor_minimo = arr[0]
    aux = arr #arreglo auxiliar
    for elemento in aux:
       if(valor_minimo>elemento):
           valor_minimo=elemento
    return valor_minimo

def ordenar(arr):
    aux = arr
    s=[]
    for i in range(len(aux)):
        v_m = minimo(aux) 
        s.append(minimo(aux))
        aux.remove(v_m)
    
    return s
    