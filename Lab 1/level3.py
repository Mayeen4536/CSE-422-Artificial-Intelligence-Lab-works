a_dict = {}


file = open("input3.txt")

for line in file:
    a = line.split()
    if int(a[0]) in a_dict:
        a_dict[int(a[0])].append(int(a[1]))
    else:
        a_dict[int(a[0])] = [int(a[1])]
    
    

print(a_dict)






def bfs(nodes, graph, nora_position , lina_position, parent, dist):

    visited = [False for i in range(nodes)] # List to keep track of visited nodes.
    queue = [] 

    for i in range(nodes):

        dist[i] = 1000000
        parent[i] = -1

    visited[nora_position] = True
    dist[nora_position] = 0
    queue.append(nora_position)

    while queue:
        s = queue.pop()
        
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
    
        


   

    



# Driver Code
k2 = shortestpath(a_dict, 2 , 9, 10)
k3 = shortestpath(a_dict, 6 , 9, 10)
k1 = shortestpath(a_dict, 5 , 9, 10)
k4 = shortestpath(a_dict, 7 , 9, 10)
k5 = shortestpath(a_dict, 4 , 9, 10)
k6 = shortestpath(a_dict, 3 , 9, 10)
print([k1, k2, k3, k4, k5, k6])
print(min(k1,k2,k3,k4,k5,k6))
