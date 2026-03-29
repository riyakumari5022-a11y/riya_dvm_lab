from collections import deque

graph = {0:[1,2],1:[3],2:[],3:[]}

def bfs(start):
    visited=set()
    q=deque([start])

    while q:
        node=q.popleft()
        if node not in visited:
            print(node)
            visited.add(node)
            q.extend(graph[node])

bfs(0)