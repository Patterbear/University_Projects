def is_connected(g, dst, src):
    visited = []
    todo = []
    visited.append(src)
    todo.append(src)
    while todo:
        s = todo.pop(0) 
        #print (s) 

        for neighbour in g[s]:
          if neighbour not in visited:
            visited.append(neighbour)
            todo.append(neighbour)

    if dst not in visited:
        return False
    else:
        return True


g = {'A' : ['B','D'],
  'B' : ['D', 'C'],
  'C' : ['E'],
  'D' : [],
  'E' : ['A'],
  'F' : []}

print(is_connected(g, 'A', 'E'))
print(is_connected(g, 'A', 'F'))

