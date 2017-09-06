# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 05:30:00 2017

@author: Aguir
"""

#Insercion

cnt=0
def orden_por_insercion(arr):
    global cnt
    for indice in range(1,len(arr)):
        valor=arr[indice] #valor es el elemento que vamos a comparar 
        i=indice-1        #i es el valor anterior al elemento que estamos comparar
        while i>=0:
            cnt+=1
            if (valor<arr[i]): 
                arr[i+1]=arr[i]
                arr[i]=valor
                i=i-1
            else:
                break
    return arr
    
