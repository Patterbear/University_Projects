def bfs(g, node):
    visited = []
    todo = []
    visited.append(node)
    todo.append(node)
    while todo:
        s = todo.pop(0) 
        print (s) 

        for neighbour in g[s]:
          if neighbour not in visited:
            visited.append(neighbour)
            todo.append(neighbour)


g = {'A' : ['B','D'],
  'B' : ['D', 'C'],
  'C' : ['E'],
  'D' : [],
  'E' : ['A'],
  'F' : []}

bfs(g, 'B')

