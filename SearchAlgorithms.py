# search algorithms: DFS, DIS, IDS, BFS, UCS, A*, GBFS, DLS

# DFS: Depth First Search
def dfs(graph, start, goal):
    visited = set()
    stack = [(start,[start])] # stack is a list of tuples, each tuple contains a node and the path to reach that node from the start node (LIFO)
    visited.add(start)
    while stack:
        node, path = stack.pop() # pop the last element from the stack, which is the most recently added node and its path
        if node == goal:
            print(f"dfs goal is {goal}")
            print(f"Shortest Path: {' -> '.join(path)}")
            return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor, path + [neighbor]))# append the neighbor and the path to the stack (append meaning adding to the end of the list)
    print(f"dfs goal is {goal} not found")
    return None
                
    
    
graph = {
 'A' : ['B', 'C'],
 'B' : ['A', 'C', 'D'],
 'C' : ['A', 'B','D' ,'E'],
 'D' : ['B', 'C', 'E'],
 'E' : ['C','D']
}   

s = dfs(graph, 'A', 'D')
print(s) 
print("*"*30)
#////////////////////////////////////////////////////////
# DLS: Depth Limited Search
def dls(graph, start, goal, limit):
    visited = set()
    stack = [(start, 0, [start])] # (start) for the node, (0) for depth, and ([start]) for the path to reach that node from the start node
    while stack:
        node, depth, path = stack.pop() 
        if node == goal:
            print(f"dls goal is {goal}")
            print(f"Shortest Path: {' -> '.join(path)} and depth is {depth}")
            return True
        if depth < limit:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append((neighbor, depth + 1, path + [neighbor]))
    print(f"dls goal is {goal} not found")
    return None

graph = {
 'A' : ['B', 'C'],
 'B' : ['A', 'C', 'D'],
 'C' : ['A', 'B','D' ,'E'],
 'D' : ['B', 'C', 'E'],
 'E' : ['C','D']
} 

s = dls(graph, 'A', 'D', 3)
print(s) 
print("*"*30)
#////////////////////////////////////////////////////////
# IDS: Iterative Deepening Search
def ids(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"IDS with depth limit: {depth}")
        result = dls(graph, start, goal, depth) # depth 
        if result:
            return result
    print(f"ids goal is {goal} not found within max depth {max_depth}")
    return None
s = ids(graph, 'A', 'D', 3)
print(s)
print("*"*30)

#///////////////////////////////////////////////////////
# BFS: Breadth First Search
from collections import deque
""" 
 deque is a double-ended queue
 that allows us to efficiently add 
 and remove elements from both ends of the queue, 
 which is useful for BFS where we need to add elements to the end of the queue
 and remove elements from the front of the queue (FIFO) 
"""
def bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])# using deque for efficient popping from the front of the queue (FIFO)
    visited.add(start)
    while queue:
        node, path = queue.popleft()# (popleft) to remove the first element from the queue, which is the oldest added node and its path
        if node == goal:
            print(f"bfs goal is {goal}")
            print(f"Shortest Path: {' -> '.join(path)}")
            return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor])) 
        
    print(f"bfs goal is {goal} not found")
    return None
graph = {
 'A' : ['B', 'C'],
 'B' : ['A', 'C', 'D'],
 'C' : ['A', 'B','D' ,'E'],
 'D' : ['B', 'C', 'E'],
 'E' : ['C','D']
} 

s = bfs(graph, 'A', 'E')
print(s)
print("*"*30)

#////////////////////////////////////////////////////////
# UCS: Uniform Cost Search

def path_cost(path):
    total_cost = 0
    for (node, cost) in path: # because path is a list of tuples (node, cost)
        total_cost += cost
    return total_cost, path[-1][0] # the last node in the queue. ex: if it is the last node: ('s',0) -> path[-1][0] is just 's' 

def ucs(graph, start, goal):
    visited = []
    queue = [[(start, 0)]] # just a list of paths, each path is a list of tuples (node, cost)
    while queue:
        queue.sort(key=path_cost) # because we want to sort the queue based on the total cost of the path, we use the path_cost function as the key for sorting
        path = queue.pop(0) # pop the path with the lowest cost from the queue, (0) mining the first element of the queue, which is the path with the lowest cost
        node = path[-1][0] # get the last node in the path, because the last node is the current node we are exploring, and we want to check if it is the goal node or not
        if node in visited:
            continue 
        visited.append(node)
        if node == goal:
            print(f"ucs goal is {goal} with cost {path_cost(path)[0]}")
            print(f"Shortest Path: {' -> '.join([n for n, c in path])}")
            return path
        else:
            adjacent_nodes = graph.get(node, [])
            for (node2, cost) in adjacent_nodes:
                new_path = path.copy()# Because we do not edit the original path, we need to create a copy of it to add the new node and cost to it
                new_path.append((node2, cost))
                queue.append(new_path) 
    print(f"ucs goal is {goal} not found")  
    return None            
                
graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('D', 1), ('E', 6)],
    'C': [('G', 3)],
    'D': [('G', 4)],
    'E': [('G', 1)],
    'G': []
}
s = ucs(graph, 'A', 'G')
print(s)
print("*"*30)
#/////////////////////////////////////////////////////////
#A*: A Star Search
def path_f_cost(path): # f(n) = g(n) + h(n)
    g_cost = 0
    for (node, cost) in path:
        g_cost += cost
    last_node = path[-1][0]
    h_cost = H_table[last_node] 
    f_cost = g_cost + h_cost
    return f_cost, last_node  

def a_star_search(graph, start, goal):
    visited = []
    queue = [[(start, 0)]] # just a list of paths, each path is a list of tuples (node, cost)
    while queue:
        queue.sort(key=path_f_cost)
        path = queue.pop(0)
        node = path[-1][0] # get the last node in the path, because the last node is the current node we are exploring, and we want to check if it is the goal node or not
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            print(f"a* goal is {goal} with cost {path_f_cost(path)[0]}")
            print(f"Shortest Path: {' -> '.join([n for n, c in path])}")
            return path
        else:
            adjacent_nodes = graph.get(node, [])
            for (node2, cost) in adjacent_nodes:
                new_path = path.copy()
                new_path.append((node2, cost))
                queue.append(new_path)
                
    print(f"a* goal is {goal} not found")  
    return None          
    
graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('D', 1), ('E', 6)],
    'C': [('G', 3)],
    'D': [('G', 4)],
    'E': [('G', 1)],
    'G': []
}
H_table = {
 'A' : 4,
 'B' : 3,   
    'C' : 2,
    'D' : 1,
    'E' : 0,
    'G' : 0
}
s = a_star_search(graph, 'A', 'G')
print(s)

print("*"*30)
#////////////////////////////////////////////////////////
# GBFS: Greedy Best First Search
def path_h_cost(path): # f(n) = h(n) 
    last_node = path[-1][0]
    h_cost = H_table[last_node]
    f_cost = h_cost
    return f_cost, last_node 

def gbfs(graph, start, goal):
    visited = []
    queue = [[(start, 0)]]
    while queue:
        queue.sort(key=path_h_cost) # sorting by h-cost 
        path = queue.pop(0) # choosing last h-cost
        node = path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            print(f"gbfs goal is {goal} with heuristic cost {path_h_cost(path)[0]}")
            print(f"Shortest Path: {' -> '.join([n for n, c in path])}")
            return path
        else:
            adjacent_nodes = graph.get(node, [])
            for (node2, cost) in adjacent_nodes:
                new_path = path.copy()
                new_path.append((node2, cost))
                queue.append(new_path)
                
    print(f"gbfs goal is {goal} not found")
    return None

graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('D', 1), ('E', 6)],
    'C': [('G', 3)],
    'D': [('G', 4)],
    'E': [('G', 1)],
    'G': []
}
H_table = {
 'A' : 4,
 'B' : 3,   
    'C' : 2,
    'D' : 1,
    'E' : 0,
    'G' : 0
}
s = gbfs(graph, 'A', 'G')
print(s)

 






