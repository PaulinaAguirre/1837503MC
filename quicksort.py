# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 11:30:05 2017

@author: Aguir
"""

import random

#Arreglillo aleatorio
def ran_num(n,lim_inf=0, lim_sup=100):
    arr = []
    for i in range(n):
        arr.append(random.randint(lim_inf, lim_sup))
    return arr

#Algoritmo de ordenamiento
def quick_sort(arr,bajo,alto):
    global operaciones
    if bajo < alto:
        operaciones += 3
        valor = particion(arr, bajo, alto)    
        quick_sort(arr,bajo,valor-1)
        quick_sort(arr, valor+1 , alto)
    return operaciones

#Funcion aux
def particion(arr, bajo, alto):
    global operaciones
    operaciones += 1
    pivote = arr[alto]
    wall = bajo-1
    operaciones += 1
    for j in range(bajo, alto):
        operaciones += 1
        if arr[j]<pivote:
            wall += 1
            cambiar(arr,wall,j)
            operaciones += 5
    operaciones += 1
    if(arr[alto]< arr[wall+1]):
        operaciones += 3
        cambiar(arr,wall+1,alto)
    return wall+1

#Funcion para cambiar los elementos
def cambiar(arr, a, b):
    aux = arr[a]
    arr[a]= arr[b]
    arr[b]= aux


#Ejemplillo

global operaciones 
operaciones = 0
p = ran_num(10)
print("arr desordenado", p)
print()
num = quick_sort(p, 0, len(p)-1)
print("arr ordenado" ,p)
print("Número de operaciones : " + str(num) ) 

