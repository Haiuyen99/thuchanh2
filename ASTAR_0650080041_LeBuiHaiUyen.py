map={
       "Arad":{"Sibiu":140,"Timisoara":118,"Zerind":75},
       "Timisoara":{"Lugoj":111,"Arad":118},
       "Lugoj":{"Mehadia":70,"Timisoara":111},
       "Mehadia":{"Dobreta":75,"Lugoj":70},
       "Dobreta":{"Craiova":120,"Mehadia":75},
       "Craiova":{"Rimnicu Vilcea":146,"Pitesti":138,"Dobreta":120},
       "Rimnicu Vilcea":{"Sibiu":80,"Pitesti":97,"Craiova":146},
       "Sibiu":{"Arad":140,"Fagaras":99,"Rimnicu Vilcea":80},
       "Zerind":{"Oradea":71,"Arad":75},
       "Oradea":{"Sibiu":151,"Zerind":71},
       "Fagaras":{"Bucharest":211,"Sibiu":99},
       "Pitesti":{"Rimnicu Vilcea":97,"Craiova":138,"Bucharest":101},
       "Bucharest":{"Giurgui":90,"Fagaras":211,"Pitesti":101,"Urziceni":85},
       "Urziceni":{"Bucharest":85,"Hirsova":98,"Vaslui":142},
       "Hirsova":{"Urziceni":98,"Eforie":86},
       "Eforie":{"Hirsova":86},
       "Vaslui":{"Urziceni":142,"lasi":92},
       "lasi":{"Vaslui":92,"Neamt":87},
       "Neamt":{"lasi":87},
       "Giurgui":{"Bucharest":90}
       
       }
map_2={
       "S":{"A":2,"C":5},
       "A":{"G":20},
       "G":{"D":7},
       "C":{"A":5,"D":2,"G":20},
       "D":{"B":4,"E":3},
       "B":{"A":4},
       "E":{"B":6,"G":5}
      }
map_3={
        "A":{"B":2,"C":1,"G":9},
        "B":{"D":3,"F":2},
        "F":{"G":4},
        "D":{"G":4},
        "C":{"E":4,"D":2},
        "E":{}
        }
heuristics_3={"A":6,"B":0,"C":6,"D":1,"E":10,"F":4,"G":0}
heuristics={"Arad":366,"Bucharest":0,"Craiova":160,"Dobreta":242,"Eforie":161,"Fagaras":178,"Giurgui":77,"Hirsova":151,"lasi":226,"Lugoj":244,"Mehadia":241,"Neamt":234,"Oradea":380,"Pitesti":98,"Rimnicu Vilcea":193,"Sibiu":253,"Timisoara":329,"Urziceni":80,"Vaslui":199,"Zerind":374}
map_4={
        "S":{"A":2,"B":3},
        "A":{"C":3},
        "B":{"C":1,"D":3},
        "C":{"D":1,"E":3},
        "D":{"F":2},
        "F":{"G":1},
        "E":{"G":2},
        "G":{}
        }
heuristics_4={"S":6,"A":4,"B":4,"C":4,"D":3.5,"E":1,"F":1,"G":0}
heuristics=heuristics
def getmin(lists): 
    s=lists[0]
    for i in lists:
        if i[1]<s[1]:
            s=i
    return s
def getelemt(lists,n): 
    for i in lists:
        if i[0]==n:
            return i
    return None
def Astar(map,start,goal):
    q=[]
    for node in map[start]:
        c=heuristics.get(node)
        c1=map.get(start,{}).get(node)
        q.append([node,c+c1,start,str(start+"->"+node),c1])
    while len(q)!=0:
        node,h,previous,path,cost=getmin(q)
        q.remove(getmin(q))
        
        if node==goal:
            return path,cost
            break
        if bool(node)==False:
            continue
        for n in map[node]:
            c1=cost+map.get(node,{}).get(n)
            cc=c1+heuristics.get(n)
            
            if bool(n)==True:
                if getelemt(q,n)!=None:
                    nod,hh,prev,pat,cos=getelemt(q,n)
                    if c1<=cos:
                        q.remove(getelemt(q,n))
                        q.append([n,cc,prev,str(path+"->"+n),c1])
                else:
                    cc=cost+heuristics.get(node)
                    c1=cost+map.get(node,{}).get(n)
                    q.append([n,cc,node,str(path+"->"+n),c1])
    
a=Astar(map,'Arad',"Bucharest")
print("Đường đi đến đích là : {}\n chi phi la: {}".format(a[0],a[1]))