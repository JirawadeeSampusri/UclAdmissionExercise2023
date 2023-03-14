def reachable(adj_list, start_node):
  """
  adj_list = [[1, 3], [2], [0], [4], [3], []]
  You are asked to implement an algorithm to compute the nodes reachable from a given node by following the arcs.


  For the above example, the set of reachable nodes from 0 is {0, 1, 2, 3, 4} and from 3 is {3, 4}

  from 2 is {2,0,1,3,4}

  """
  reachable_list = []
  visit = [False]*len(adj_list) 
  q = []
  q.append(start_node)  
  visit[start_node] = True
  while (len(q) > 0):
    tmp_node = q.pop(0)
    reachable_list.append(tmp_node)
    for j in adj_list[tmp_node]:
      if (visit[j] == False):
        visit[j] = True
        q.append(j)
        
  return reachable_list





