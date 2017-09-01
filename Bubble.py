# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

def burbuja(A):
    numero=len(A)
    i=0
    while(i<numero):
        j=i
        while(j<numero):
            if(A[i]>A[j]):
                temp=A[i]
                A[i]=A[j]
                A[j]=temp    
            j=j+1
        i=i+1
    for A in A:
        print(A)
        