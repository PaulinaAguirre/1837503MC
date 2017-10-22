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
        self.E=dict()        
        self.vecinos=dict()
        
    def A(self, v): #Agregar
        self.vertices.add(v)
        if not v in self.vecinos: #Vecindá de v
            self.vecinos[v]=set()
            
    def C(self, v, u, peso=1): #Concectar
        self.A(v)
        self.A(u)
        self.E[(v,u)]=self.E[(u,v)]=peso
        self.vecinos[v].add(u)
        self.vecinos[u].add(v)
        
    def __str__(self):
        return "Aristas= " + str(self.E)+"\nVertices = " +str(self.vertices)

#Algoritmo Dijkstra
    def shortest(self, v): # Dijkstra's algorithm
        q = [(0, v, ())] # arreglo "q" de las "Tuplas" de lo que se va a almacenar dondo 0 es la distancia, v el nodo y () el "camino" hacia el
        dist = dict() #diccionario de distancias 
        visited = set() #Conjunto de visitados
        while len(q) > 0: #mientras exista un nodo pendiente
            (l, u, p) = heappop(q) # Se toma la tupla con la distancia menor
            if u not in visited: # si no lo hemos visitado
                visited.add(u) #se agrega a visitados
                dist[u] = (l,u,list(flatten(p))[::-1] + [u])  	#agrega al diccionario
            p = (u, p) #Tupla del nodo y el camino
            for n in self.vecinos[u]: #Para cada hijo del nodo actual
                if n not in visited: #si no lo hemos visitado
                    el = self.E[(u,n)] #se toma la distancia del nodo acutal hacia el nodo hijo
                    heappush(q, (l + el, n, p)) #Se agrega al arreglo "q" la distancia actual mas la ditanacia hacia el nodo hijo, el nodo hijo n hacia donde se va, y el camino
        return dist #regresa el diccionario de distancias

###Grafillos para probar el Dijkstra###

g= grafo() #Grafillo con 5 nodos y 10 vertices
g.C('a','b', 8)
g.C('b','c', 6)
g.C('a','d', 2)
g.C('a','e', 9)
g.C('c','e', 1)
g.C('c','d', 4)
g.C('a','c', 4)
g.C('b','d', 6)
g.C('d','e', 3)
g.C('b','e', 5)

g2=grafo() #Grafo con 10 nodos y 20 vertices
g2.C('a','b', 6)
g2.C('a','c', 1)
g2.C('a','d', 2)
g2.C('a','e', 8)
g2.C('b','d', 3)
g2.C('b','g', 2)
g2.C('c','d', 2)
g2.C('d','h',15)
g2.C('e','h', 8)
g2.C('e','f',11)
g2.C('e','i', 2)
g2.C('g','h', 8)
g2.C('g','j',19)
g2.C('g','i',14)
g2.C('h','i', 4)
g2.C('h','f', 4)
g2.C('j','i', 5)
g2.C('f','i', 9)
g2.C('d','e', 1)
g2.C('b','h',20)

g3=grafo() #Grafo de 15 nodos y 30 vertices
g3.C('1','4',13)
g3.C('1','7', 2)
g3.C('2','1', 1)
g3.C('3','2', 2)
g3.C('3','1',25)
g3.C('3','5',30)
g3.C('5','2', 5)
g3.C('5','8',14)
g3.C('5','6', 4)
g3.C('6','3',11)
g3.C('6','9', 9)
g3.C('7','4',12)
g3.C('7','6',17)
g3.C('7','10',8)
g3.C('8','9', 3)
g3.C('8','11',6)
g3.C('9','5',15)
g3.C('10','9',8)
g3.C('11','10',7)
g3.C('11','12',1)
g3.C('8','14',4)
g3.C('14','11',2)
g3.C('9','13',8)
g3.C('13','11',3)
g3.C('7','15',2)
g3.C('15','6',1)
g3.C('10','15',4)
g3.C('15','8',3)
g3.C('10''13',9)
g3.C('8','13',0)

g4=grafo() #Grafillo de 20 nodos y 40 vertices
g4.C('A','B', 0)
g4.C('A','S', 9)
g4.C('A','D', 3)
g4.C('D','F',10)
g4.C('F','E', 5)
g4.C('B','D',15)
g4.C('D','E', 8)
g4.C('B','C', 8)
g4.C('E','G', 2)
g4.C('G','I', 9)
g4.C('G','H', 6)
g4.C('H','I',29)
g4.C('C','D',11)
g4.C('D','P', 4)
g4.C('C','Q', 1)
g4.C('Q','P', 9)
g4.C('F','P', 5)
g4.C('P','O',50)
g4.C('Q','S',12)
g4.C('S','R',33)
g4.C('Q','R', 4)
g4.C('S','T',18)
g4.C('T','O',14)
g4.C('Q','O',41)
g4.C('O','M', 7)
g4.C('O','L',75)
g4.C('T','N',44)
g4.C('N','M',22)
g4.C('M','L',19)
g4.C('L','G', 7)
g4.C('E','J',18)
g4.C('J','K',25)
g4.C('L','J', 6)
g4.C('J','H',32)
g4.C('K','I', 4)
g4.C('L','K',98)
g4.C('M','K',22)
g4.C('N','J',74)
g4.C('N','K', 5)
g4.C('P','L',25)

g5=grafo() #Grafo 25 nodos y 50 vertices
g5.C("1","2", 1)
g5.C("2","5", 4)
g5.C("3","7", 15)
g5.C("4","6", 22)
g5.C("5","8", 18)
g5.C("6","10",13)
g5.C("9","7", 5)
g5.C("10","1",7)
g5.C("11","25",17)
g5.C("15","4",21)
g5.C("2","15",30)
g5.C("12","18",35)
g5.C("13","12",42)
g5.C("7","21",0)
g5.C("14","17",18)
g5.C("6","14",23)
g5.C("9","2",45)
g5.C("21","17",49)
g5.C("15","13",31)
g5.C("20","1",20)
g5.C("16","22",28)
g5.C("22","5",4)
g5.C("9","12",13)
g5.C("17","10",17)
g5.C("6","16",43)
g5.C("11","21",35)
g5.C("8","16",28)
g5.C("18","24",1)
g5.C("13","19",5)
g5.C("17","19",12)
g5.C("1","11",17)
g5.C("19","4",20)
g5.C("6","21",9)
g5.C("9","14",3)
g5.C("20","10",14)
g5.C("12","20",19)
g5.C("21","8",8)
g5.C("9","13",11)
g5.C("3","9",0)
g5.C("22","14",16)
g5.C("13","21",9)
g5.C("4","5",14)
g5.C("21","22",17)
g5.C("11","12",6)
g5.C("23","15",8)
g5.C("6","17",4)
g5.C("3","20",19)
g5.C("24","12",12)
g5.C("7","21",4)
g5.C("25","12",5)

print(g.shortest('a'))
print(g2.shortest('a'))
print(g3.shortest('1'))
print(g4.shortest('A'))
print(g5.shortest('1'))



