# search algorithms: DFS, BFS, UCS, A*, GBFS, DLS

def dfs(graph, start, goal):
    visited = set()
    stack = [(start, [start])]
    visited.add(start)
    while stack:
        node, path = stack.pop()
        if node == goal:
            print(f"goual is {goal}")
            return path
        if node not in visited:
            visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))
                
                
    print(f"goal is {goal} not found")
    return None
    
graph = {
 'A' : ['B', 'C'],
 'B' : ['A', 'C', 'D'],
 'C' : ['A', 'B','D' ,'E'],
 'D' : ['B', 'C', 'E'],
 'E' : ['C','D']
}   

s = dfs(graph, 'A', 'E')
print(s) 
print("*"*30)

def bfs(graph, start, goal):
    visited = set()
    queue = [(start, [start])]
    visited.add(start)
    while queue:
        node, path = queue.pop(0)
        if node == goal:
            print(f"goual is {goal}")
            return path
        if node not in visited:
            visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
                
    print(f"goal is {goal} not found")
    return None

s = bfs(graph, 'A', 'E')
print(s)
print("*"*30)


def ucs(graph, start, goal):
    visited = set()
    queue = [(0, start, [start])]
    visited.add(start)
    while queue:
        cost, node, path = queue.pop(0)
        if node == goal:
            print(f"goual is {goal}")
            return path
        if node not in visited:
            visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((cost + 1, neighbor, path + [neighbor]))
                
    print(f"goal is {goal} not found")
    return None

s = ucs(graph, 'A', 'E')
print(s)
print("*"*30)

def a_star(graph, start, goal, heuristic):
    visited = set()
    queue = [(0, start, [start])]
    visited.add(start)
    while queue:
        cost, node, path = queue.pop(0)
        if node == goal:
            print(f"goual is {goal}")
            return path
        if node not in visited:
            visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                total_cost = cost + 1 + heuristic[neighbor]
                queue.append((total_cost, neighbor, path + [neighbor]))
                
    print(f"goal is {goal} not found")
    return None 

heuristic = {
 'A' : 4,
 'B' : 3,   
    'C' : 2,
    'D' : 1,
    'E' : 0
}
s = a_star(graph, 'A', 'E', heuristic)
print(s)

print("*"*30)

def gbfs(graph, start, goal):
    visited = set()
    queue = [(start, [start])]
    visited.add(start)
    while queue:
        node, path = queue.pop(0)
        if node == goal:
            print(f"goual is {goal}")
            return path
        if node not in visited:
            visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
                
    print(f"goal is {goal} not found")
    return None

s = gbfs(graph, 'A', 'E')
print(s)

print("*"*30)

def dls(graph, start, goal, depth):
    visited = set()
    stack = [(start, [start], 0)]
    visited.add(start)
    while stack:
        node, path, current_depth = stack.pop()
        if node == goal:
            print(f"goual is {goal}")
            return path
        if node not in visited and current_depth < depth:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor], current_depth + 1))
                
    print(f"goal is {goal} not found")
    return None

s = dls(graph, 'A', 'E', 2)
print(s)    






