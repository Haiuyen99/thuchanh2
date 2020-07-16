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
heuristics={"Arad":366,"Bucharest":0,"Craiova":160,"Dobreta":242,"Eforie":161,"Fagaras":178,"Giurgui":77,"Hirsova":151,"lasi":226,"Lugoj":244,"Mehadia":241,"Neamt":234,"Oradea":380,"Pitesti":98,"Rimnicu Vilcea":193,"Sibiu":253,"Timisoara":329,"Urziceni":80,"Vaslui":199,"Zerind":374}

def getminHEU(q):
    s=q[0]
    for i in q:
        if s[1]>i[1]:
            s=i
    return s

def gbfs(map,start,goal,heuristics):
    if not start and goal in map.keys():
        return None
    temp=[]
    for n in map[start]:
        c=heuristics.get(n)
        cost=map.get(start,{}).get(n)
        temp.append([n,c,cost,str(start+"->"+n)])
    while len(temp)!=0:
        node,heu,cost,path=getminHEU(temp)
        temp.clear()
        if node==goal:
            return [cost,path]
            break
        for g in map[node]:
            cc=map.get(node,{}).get(g)+cost
            he=heuristics.get(g)
            temp.append([g,he,cc,path+"->"+g])

a=gbfs(map,'Arad','Bucharest',heuristics)
print("Duong di den đích là: {}".format(a[1],a[0]))