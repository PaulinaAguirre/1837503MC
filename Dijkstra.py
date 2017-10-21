# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 11:27:25 2017

@author: Aguir
"""
from heapq import heappop, heappush

def flatten(L):
    while len(L)>0:
        yield L[0]
        L=L[1]
        
#Grafo    
class grafo:
    def __init__(self):
        self.vertices=set()
        self.E=dict() #para las aristas
        self.vecinos=dict()
        
    def A(self, v): #Agregar
        self.vertices.add(v)
        if not v in self.vecinos: #Vecindá de v
            self.vecinos[v]=set()
            
    def C(self, v, u, peso=1): #Concectar
        self.A(v)
        self.A(u)
        self.E[(v,u)]=self.E[(v,u)]=peso
        self.vecinos[v].add(u)
        self.vecinos[u].add(v)
        
    def __str__(self):
        return "Aristas= " + str(self.E)+"\nVertices = " +str(self.vertices)

#Algoritmo Dijkstra
    def shortest(self,v):
        q= [(0, v, ())]
        dist = dict()
        visited = set()
        while len(q) > 0:
            (l, u, p) = heappop(q)
            if u not in visited:
                visited.add(u)
                dist[u]= (1,u,list(flatten(p))[::-1]+[u])
            p= (u,p)
            for n in self.vecinos[u]:
                if n not in visited:
                    el = self.E[(u,n)]
                    heappush(q, (l+el, n, p))
        return dist

###Grafillos para probar el Dijkstra###

g= grafo() #Grafillo con 5 nodos y 10 vertices
g.C('a','b', 2)
g.C('b','c', 3)
g.C('a','d', 5)
g.C('a','e', 6)
g.C('c','e', 4)
g.C('c','b', 2)
g.C('a','c', 4)
g.shortest('a')

g2=grafo()
g2.C('a','b',5)
g2.C('a','c',5)
g2.C('d','c',5)
g2.C('e','c',5)
g2.C('a','f',5)
g2.C('g','i',5)
g2.C('h','b',5)
g2.C('j','i',5)
g2.C('a','j',5)
g2.C('a','h',5)
g2.C('j','c',5)
g2.shortest('a')


