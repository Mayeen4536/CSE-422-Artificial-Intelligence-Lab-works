
import math

import numpy as np

# Calculating Combinations (nCr)

def ncr(n, r):

    if n>r:
        numer = math.factorial(n)
        denom = math.factorial(n-r) * math.factorial(r)
        return numer // denom
    elif n==r:
        return 1
    else:
        return 0



# Fitness Function

def fitness(population):
    global total_pair
    global ap_array
    fitness_list = []
    ap_array = []
    for i in range(8):        
        ap_array.append([])
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
            
        

# Function for Finding diagonally attacking pairs

def diagonalpair(i,j):
    
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

                            
                elif population[i][j] < population[i][s]:
                    y = abs(population[i][j] - population[i][s])
                    if x==y:
                        if [population[i][j], population[i][s]] and [population[i][s], population[i][j]] not in ap_array[i]:
                            ap_array[i].append([population[i][j], population[i][s]])
                            
            else:
                if population[i][j] > population[i][s]:
                    y = abs(population[i][j] - population[i][s])
                
                    if x==y:
                        if [population[i][j], population[i][s]] and [population[i][s], population[i][j]] not in ap_array[i]:
                            ap_array[i].append([population[i][j], population[i][s]])
                            
                elif population[i][j] < population[i][s]:
                    y = abs(population[i][j] - population[i][s])
                    if x==y:
                        if [population[i][j], population[i][s]] and [population[i][s], population[i][j]] not in ap_array[i]:
                            ap_array[i].append([population[i][j], population[i][s]])
                            
            
    
# Function for Finding fitness percentage  

# def p(fit):
#     p = []
#     sum = np.sum(fit)
#     for i in range(len(fit)):
#         p.append(fit[i] / sum)
#     return p



# Crossover Function

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




# Mutate Function

def mutate(threshold):
    global population
    global new_population
    for i in range(len(new_population)):
        if np.random.rand() < threshold:
            index = np.random.randint(0,8) 
            value = np.random.randint(1,9)
            new_population[i][index] = value
    population = new_population
    


# Main Function

def Genetic_Algorithm():
    global fit_list
    global a
    global mutation_threshold
    global population
    global new_population
    global total_pair
    
    iteration = 0
    fitness(population)
    while total_pair not in fit_list:
        iteration += 1
        
        selected = (np.random.choice(a, 2, True, fit_list))
        crossover(population[selected[0]], population[selected[1]])
        mutate(mutation_threshold)
        fitness(population)
    
    place = fit_list.index(total_pair)

    print(iteration)            # Printing No. of Iterations 
    print(population[place])            # Printing the desired output / solved board
    print(fit_list)             # Printing the fitness list
    



n = 8           # No. of Queen
start_population = 4            # No. of Individuals/Chromosome
population = np.random.randint(1, 9, (start_population, n)) 
mutation_threshold = 0.3
total_pair = ncr(n , 2)         # Amount of total Possible pairs among n Queens

new_population = []
ap_array = []
fit_list = []
a = [0,1,2,3]

Genetic_Algorithm()         # Main Function Run






