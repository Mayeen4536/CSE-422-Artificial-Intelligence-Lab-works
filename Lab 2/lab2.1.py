
import collections
import math
import operator as op
from functools import reduce

import numpy as np


def ncr(n, r):

    if n>r:
        numer = math.factorial(n)
        denom = math.factorial(n-r) * math.factorial(r)
        return numer // denom
    elif n==r:
        return 1
    else:
        return 0



population =np.random.randint(1, 9, (4, 8))

new_population = []
total_pair = ncr(8 , 2)

fit_list = []

a = [0,1,2,3]
ap_array = []
# for i in range(8):        
#     ap_array.append([])



def fitness(population):
    global total_pair
    global ap_array
    ap_array = []
    for i in range(8):        
        ap_array.append([])
    fitness_list = []
    for i in range(len(population)):
        
        ap = 0
        array = []
        for j in range(len(population[i])):
        
            if population[i][j] not in array:
                
                array.append(population[i][j])
                if np.count_nonzero(population[i]==population[i][j]) > 1:
                    
                    ap += ncr(np.count_nonzero(population[i]==population[i][j]), 2)
                    
        
                    
            diagonalpair(i,j)
            
        ap += len(ap_array[i])
        non_attacking_pair = 0
        non_attacking_pair = total_pair - ap
        fitness_list.append(non_attacking_pair)
        
        global fit_list 
        fit_list = []
        fit_list = fitness_list
        
            
        



def diagonalpair(i,j):
    l = 1
    r = 1
    global ap_array

    
    for s in range(len(population[i])):
        
        
        if s!=j:
            x = abs(j-s)
            if j > s:
                if population[i][j] > population[i][s]:
                    y = abs(population[i][j] - population[i][s])
                
                    if x==y:
                        if [population[i][j], population[i][s]] and [population[i][s], population[i][j]] not in ap_array[i]:
                            ap_array[i].append([population[i][j], population[i][s]])

                            l += 1
                elif population[i][j] < population[i][s]:
                    y = abs(population[i][j] - population[i][s])
                    if x==y:
                        if [population[i][j], population[i][s]] and [population[i][s], population[i][j]] not in ap_array[i]:
                            ap_array[i].append([population[i][j], population[i][s]])
                            r += 1
            else:
                if population[i][j] > population[i][s]:
                    y = abs(population[i][j] - population[i][s])
                
                    if x==y:
                        if [population[i][j], population[i][s]] and [population[i][s], population[i][j]] not in ap_array[i]:
                            ap_array[i].append([population[i][j], population[i][s]])
                            r += 1
                elif population[i][j] < population[i][s]:
                    y = abs(population[i][j] - population[i][s])
                    if x==y:
                        if [population[i][j], population[i][s]] and [population[i][s], population[i][j]] not in ap_array[i]:
                            ap_array[i].append([population[i][j], population[i][s]])
                            l += 1
            
def p(fit):
    p = []
    sum = np.sum(fit)
    for i in range(len(fit)):
        p.append(fit[i] / sum)
    return p

def crossover(x,y):
    global new_population
    global population
    new_population = []
    point = np.random.randint(1,8)
    
    c1x = x[0:point]
    c1y = y[point:]
    c2x = y[0:point]
    c2y = x[point:]
    child1 = np.concatenate((c1x, c1y))
    child2 = np.concatenate((c2x, c2y))
    
    
    select = np.random.choice(3, 4)
    
    for i in select:
        if i == 0:
            new_population.append(child1)
        else:
            new_population.append(child2)
        
    population = new_population

def mutate(threshold):
    global population
    global new_population
    for i in range(len(new_population)):
        if np.random.rand() < threshold:
            index = np.random.randint(0,8) 
            value = np.random.randint(1,9)
            new_population[i][index] = value
    population = new_population
    



iteration = 0
fitness(population)
while total_pair not in fit_list:
    iteration += 1
    
    selected = (np.random.choice(a, 2, True, p(fit_list)))
    crossover(population[selected[0]], population[selected[1]])
    mutate(0.3)
    fitness(population)
place = fit_list.index(total_pair)
print(iteration)
print(population[place])
print(fit_list)
print(population)
