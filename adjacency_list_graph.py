import collections , io ,math
import heapq
import Dijkstra
import re


mygraph = collections.defaultdict(list)
mynodes = dict()
myedges = dict()
request = []

# myinput = """6 6
# 10 35.9853606 50.731763
# 15 35.9903606 50.731763
# 20 35.9953606 50.736763
# 25 35.9953606 50.724263
# 30 36.0003606 50.731763
# 35 36.0053606 50.731763
# 10 15
# 15 20
# 15 25
# 20 30
# 25 30
# 30 35
# """

# myrequest ="""0 10 35
# 2 15 35
# 7 15 35
# """

address = input("address please : ").replace("\"" , "")
with open(address) as reader :
    # print(reader.read())
    myinput = reader.read()
# print(myinput)

myrequest = []
number_request = int(input("number of request : "))
for i in range(number_request):
    myrequest.append(input()) 
print()

def update_wieght() :
    for i in mygraph :
        for ii in mygraph[i]:
            lenght , traffic = myedges[(i , ii[0])]
            ii[1] = lenght * (1 + (0.3 * traffic))

def find_path(source , distination , mygraph) :
    update_wieght()
    path = Dijkstra.dijkstra(mygraph , source)
    mypath = []
    while (distination != source ) :
        mypath.append(distination)
        distination = path[distination]
    mypath.append(source)
    return mypath

def update_time_traffic(time , time_traffic , myedges) :

    remove_list = []
    for el in time_traffic:
        if ( time < el[0] ) :
            continue
        for v , u in el[1] :
            myedges[(v , u)][1] -= 1
        remove_list.append (el)
    for i in remove_list :
        time_traffic.remove(i)
        

def find_take_time(path) :
    total_wieght = 0
    for i in range(len(path)-1) :
        v , u = path[i],path[i+1]
        for node in mygraph[v] :
            if node[0] == u :
                total_wieght += node[1] 
            
    x = (120 * total_wieght)
    # return float("{:.2f}".format(x))
    # return  round(x, 2)
    return x



buf = io.StringIO(myinput)
n , m = map(int ,buf.readlines(1)[0].replace("\n" , "").split(" "))
for i in range(n) : 
    node , x , y = buf.readlines(1)[0].replace("\n" , "").split(" ")
    node , x , y = int(node) , float(x) , float(y)
    mynodes[node] = (x , y)

for i in range(m) :
    v , u = map(int ,buf.readlines(1)[0].replace("\n" , "").split(" "))
    mygraph[v].append([u, 0])
    mygraph[u].append([v, 0])

# buf = io.StringIO(myrequest)
for i in myrequest :
    time  , node1 , node2 = i.split(" ")
    time  , node1 , node2 = float(time) , int(node1) , int(node2)
    request.append([time , node1 , node2])



for i in mygraph :
    for ii ,nn in mygraph[i]:
        lenght = math.dist([mynodes[i][0] , mynodes[i][1] ] , [mynodes[ii][0] , mynodes[ii][1] ])
        # lenght = round(lenght, 2)
        myedges[(i , ii)] = [lenght , 0]

update_wieght()

# print(request)
time = 0
time_traffic = []
answer = []

for re in request :
    time , source  , distination = re

    update_time_traffic(time,time_traffic,myedges)

    path = find_path(source , distination , mygraph)
    time_take = find_take_time(path)
    answer.append([path , time_take])

    path_node = []
    for i in range(len(path)-1) :
        v , u = path[i],path[i+1]
        path_node.append((v,u))
        path_node.append((u,v))
    time_traffic.append([time_take + time , path_node])

    for v , u in path_node :
        myedges[(v , u)][1] += 1


for p , t in answer :
    pt = ""
    for ii in p :
        pt += str(ii) + " "
    print(pt)
    print(t)
    # print()

    
    
    


    
    
    
