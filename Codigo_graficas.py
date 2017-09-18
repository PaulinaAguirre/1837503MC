# -*- coding: utf-8 -*-
""" 
Created on Mon Sep 18 11:10:24 2017

@author: Aguir
"""

import random
import copy

#arreglillo aleatorio 
def ran_n(n,lim_i=0,lim_s=100):
    arr=[]
    for i in range(n):
        arr.append(random.randint(lim_i,lim_s))
    return arr

#Bubble
def burbuja(A):
    cnt=0
    numero=len(A)
    i=0
    while(i<numero):
        j=i
        while(j<numero):
            cnt+=1
            if(A[i]>A[j]):
                temp=A[i]
                A[i]=A[j]
                A[j]=temp    
            j=j+1
        i=i+1
    return cnt
        
#Insercion
def insercion(arr):
    cnt=0
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
    return cnt
    
#Selection
def selection(arr):
    cnt=0
    for i in range(0,len(arr)-1):
        val=i
        for j in range(i+1, len(arr)):
            cnt +=1
            if arr[j]<arr[val]:
                val=j
            if val != i:
                aux = arr[i]
                arr[i]=arr[val]
                arr[val]=aux
    return cnt

#Algoritmo de ordenamiento
global operaciones
operaciones=0
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
    
longitud=2
while longitud<1010:
    p=ran_n(longitud)
    p1,p2,p3,p4 = copy.deepcopy(p), copy.deepcopy(p), copy.deepcopy(p), copy.deepcopy(p)
    b=burbuja(p1)
    c=selection(p2)
    d=insercion(p3)
    operaciones=0
    quick_sort(p4,0,len(p4)-1)
    print(longitud,b,c,d,operaciones)
    longitud+=25
    
    
    
    
    
