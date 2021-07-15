a_dict = {}


file = open("input3.txt")

for line in file:
    a = line.split()
    if int(a[1]) in a_dict:
        a_dict[int(a[1])].append(int(a[0]))
    else:
        a_dict[int(a[1])] = [int(a[0])]
    




distances = []

def bfs(nodes, a_dict, lina_position , nora_position, parent, dist):

    visited = [False for i in range(nodes)] 
    queue = [] 

    for i in range(nodes):

        dist[i] = 1000000
        parent[i] = -1

    visited[lina_position] = True
    dist[lina_position] = 0
    queue.append(lina_position)

    while queue:
        
        s = queue.pop(0)
        
        for i in range(len(a_dict[s])):
           
        

            if visited[a_dict[s][i]] == False:
                
                visited[a_dict[s][i]] = True
                dist[a_dict[s][i]] = dist[s] + 1
                parent[a_dict[s][i]] = s
                queue.append(a_dict[s][i])

                if a_dict[s][i] == nora_position:
                    return True

    return False

def shortestpath(a_dict, lina_position, nora_array, nodes):
    
    for nora_position in nora_array:
        

        parent = [0 for i in range(nodes)]
        dist = [0 for i in range(nodes)]

        if bfs(nodes, a_dict, lina_position, nora_position, parent, dist) != False:
            
            path =[]
            crawl = nora_position
            path.append(crawl)

            while parent[crawl] != -1:
                path.append(parent[crawl])
                crawl = parent[crawl]

            distances.append(dist[nora_position]) 
            
            


nora_array = [0, 1, 3, 5, 7]
shortestpath(a_dict, 9 , nora_array, 10)

print(min(distances))
