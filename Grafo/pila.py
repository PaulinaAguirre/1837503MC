# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 11:11:29 2017

@author: Aguir
"""
### Pila y Fila ###

#Pila
class pila(object): #quitas el más nuevo
    def __init__(self):
        self.a=[]
            
    def obtener(self):
        return self.a.pop()
    
    def meter(self,e):
        self.a.append(e)
    @property
    def longitud(self):
        return len(self.a)
    
    def __str__(self):
        return str(self.a)
    
#Fila    
class fila(pila):
    def obtener(self):
        return self.a.pop(0)

### Grafo ###

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
    
### Busqueda por anchura y Busqueda por profundidad ###

#BFS
def BFS_n(g, ni):     #ni=vertice
    visitados=[]      #arreglillo con nodos visitados inicalmente vacio
    Vvisitar=fila()   #fila con los nodos por visitar
    Vvisitar.meter( ni )
    while Vvisitar.longitud > 0:
        nodo = Vvisitar.obtener()
        if nodo not in visitados:
            visitados.append(nodo)
            for vecino in g.vecinos[nodo]:
                Vvisitar.meter(vecino)
    return visitados

#DFS
def DFS_n(g, ni):
    visitados=[]      #arreglillo con nodos visitados inicalmente vacio
    Vvisitar=pila()   #pila con los nodos por visitar
    Vvisitar.meter( ni )
    while Vvisitar.longitud > 0:
        nodo = Vvisitar.obtener()
        if nodo not in visitados:
            visitados.append(nodo)
            for vecino in g.vecinos[nodo]:
                Vvisitar.meter(vecino)
    return visitados

    
    
        
        
