a_dict = {}


file = open("input2.txt")

for line in file:
    a = line.split()
    if int(a[0]) in a_dict:
        a_dict[int(a[0])].append(int(a[1]))
    else:
        a_dict[int(a[0])] = [int(a[1])]
        

    if int(a[1]) in a_dict:
        a_dict[int(a[1])].append(int(a[0]))
    else:
        a_dict[int(a[1])] = [int(a[0])]
    
    

print(a_dict)






def bfs(nodes, graph, nora_position , lina_position, parent, dist):

    visited = [False for i in range(nodes)] 
    queue = [] 

    for i in range(nodes):

        dist[i] = 1000000
        parent[i] = -1

    visited[nora_position] = True
    dist[nora_position] = 0
    queue.append(nora_position)

    while queue:
        s = queue.pop(0)
        
        for i in range(len(a_dict[s])):

            if visited[a_dict[s][i]] == False:
                
                visited[a_dict[s][i]] = True
                dist[a_dict[s][i]] = dist[s] + 1
                parent[a_dict[s][i]] = s
                queue.append(a_dict[s][i])

                if a_dict[s][i] == lina_position:
                    return True

    return False

def shortestpath(a_dict, nora_position, lina_position, nodes):

    parent = [0 for i in range(nodes)]
    dist = [0 for i in range(nodes)]

    if bfs(nodes, a_dict, nora_position, lina_position, parent, dist) != False:
    
        path =[]
        crawl = lina_position
        path.append(crawl)

        while parent[crawl] != -1:
            path.append(parent[crawl])
            crawl = parent[crawl]

        return dist[lina_position]
    
        

nora = shortestpath(a_dict, 5 , 7, 9)
lara = shortestpath(a_dict, 3 , 7, 9)

print('Nora needs ' + str(nora) + ' moves')
print('Lara needs ' + str(lara) + ' moves')

if nora < lara:
    print ('So winner is Nora')
elif nora > lara:
    print ('So winner is Lara')
else:
    print ('Both wins')
