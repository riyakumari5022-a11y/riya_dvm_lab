graph = {0:[1,2],1:[3],2:[],3:[]}

def dfs(node,visited=set()):
    if node not in visited:
        print(node)
        visited.add(node)
        for n in graph[node]:
            dfs(n,visited)

dfs(0)