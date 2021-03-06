from collections import defaultdict

topology=defaultdict(list)


def addEdge(u,v):
    topology[u].append(v)

def dfsAlias(start,visited):
    visited.append(start)

    for i in topology[start]:
        if i not in visited:
            dfsAlias(i,visited)

    

def dfs(start):
    visited=[]

    dfsAlias(start,visited)

    print(visited)


def bfs(start):
    queue=[]
    visited=[]
    queue.append(start)
    visited.append(start)
    
    

    while queue:
        x=queue.pop(0)

        for i in topology[x]:
            if i not in visited :
                queue.append(i)
                visited.append(i)


    print(visited)
    
        
            
    


addEdge(2,3)
addEdge(2,4)
addEdge(4,5)
addEdge(4,6)
addEdge(4,2)
addEdge(3,7)
addEdge(3,8)
addEdge(3,2)

dfs(2)
bfs(2)
