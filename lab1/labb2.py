import math
from queue import Queue

import numpy as np

file= open('myinput1.txt','r')

vertex_count=int(file.readline().strip())
total_connections=int(file.readline().strip())


adj_matrix = list()
for i in range(vertex_count):
    adj_matrix.append(list())
for i in range(0,total_connections):
    line=file.readline().strip()
    vertices=line.split(" ")
    v=int(vertices[0])
    u=int(vertices[1])
    adj_matrix[v].append(u)
    adj_matrix[u].append(v)
    

linasPosition=int(file.readline().strip())
norasPosition=int(file.readline().strip())
larasPosition=int(file.readline().strip())



def BFS(Position, vertex_count, adj_matrix, linasPosition ):

    predecessor = list()
    for i in range(vertex_count):
        predecessor.append(0)
    distance = list()
    for i in range(vertex_count):
        distance.append(0)


    passed = list()
    for i in range(vertex_count):
        passed.append('grey')
    queue = list() 

    for i in range(vertex_count):

        distance[i] = math.inf
        predecessor[i] = -1

    passed[Position] = 'white'
    distance[Position] = 0
    queue.append(Position)

    while queue:
        s = queue.pop()
        
        for i in range(len(adj_matrix[s])):

            if passed[adj_matrix[s][i]] == 'grey':
                
                passed[adj_matrix[s][i]] = 'white'
                distance[adj_matrix[s][i]] = distance[s] + 1
                predecessor[adj_matrix[s][i]] = s
                queue.append(adj_matrix[s][i])

                if adj_matrix[s][i] == linasPosition:
                    

                    return str(distance[linasPosition])
                    
                
                
        
nora = BFS(norasPosition, vertex_count, adj_matrix, linasPosition)
lara = BFS(larasPosition, vertex_count, adj_matrix, linasPosition)

if nora < lara:
    print('nora')
else:
    print('lara')

