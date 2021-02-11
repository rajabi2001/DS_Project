import heapq


def dijkstra ( mygraph , source):

    dist = dict()
    prev = dict()
    explored = set()
    unexplored = [(0 , source)]
    dist[source] = 0

    while unexplored :

        v_dist , v = heapq.heappop(unexplored)
        if v in explored: 
            continue
        explored.add(v)
    
        for u , w in mygraph[v] : 

            if u in explored: 
                continue

            if ( u not in dist ) or  ( v_dist + w < dist[u]) :
                dist[u] = v_dist + w 
                prev[u] = v
                heapq.heappush(unexplored , (v_dist + w , u))
    
    return prev




# mygraph = {

#     0 : [ (1, 4) ,(7, 8) ] ,
#     1 : [ (0 , 4) , (7 , 11) , (2 , 8)] ,
#     7 : [ (0 , 8) , (1 ,11) , (8 , 7) , (6 , 1)] ,
#     2 : [ (1 , 8) , (8 , 2) , (5 , 4) , (3 , 7)] , 
#     8 : [ (2 , 2) , (7 , 7) , (6 , 6) ] , 
#     6 : [ (8 , 6) , (7 , 1) , (5 , 2)] , 
#     5 : [ (6 , 2) , (2 , 4) , (3 , 14) , (4 , 10) ] ,
#     3 : [ (2 , 7) , (5 , 14) , (4 , 9) ] , 
#     4 : [ (3 , 9) , (5 , 10)]

# }
# n = 9
# source = 0
# print(mygraph)


# path = dijkstra(mygraph , source)
# print(path)

# mypath = ""       
# distination = 3
# while (distination != source ) :
#     mypath += str(distination) + " "
#     distination = path[distination]
# mypath += str(source)
# print(mypath)
 
        


   
