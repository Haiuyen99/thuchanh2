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

def getminUCS(li):
    s=li[0]
    for i in li:
        if i[1]<s[1]:
            s=i
    return s
def get(li,x):
    for i in li:
        if i[0]==x:
            return i
    return None

def ucs(map,s,goal):
    if not s in map.keys() or not goal in map.keys():
        return None
    queue=[]
    final=[]
    for n in map[s]:
        c=map.get(s,{}).get(n)
        queue.append([n,c,s,s+"->"+n]) # node,cost,previous,path
        if n==goal:
            final.append([n,c,s,s+"->"+n])
    explored=[s]
    traversal=[s]
    while len(queue)!=0:
        node,cost,previous,path=getminUCS(queue)
        queue.remove(getminUCS(queue))
        if node not in explored: traversal.append(node)
        explored.append(node)
        for n in map[node]:
            if n not in explored:
                c=map.get(node,{}).get(n)+cost
                if n==goal and get(final,n)==None:
                    prev=node
                    final.append([n,c,prev,path+"->"+n])
                elif n==goal and get(final,n)!=None:
                    a=get(final,n)
                    if a[1]>c:
                        final.remove(get(final,n))
                        final.append([n,c,node,path+"->"+n])
                else:
                    queue.append([n,c,node,path+"->"+n])
    return final[0][1],final[0][3],traversal

a=ucs(map,'Arad','Bucharest')
print("Duong di den đích : {}".format(a[1],a[0],a[2]))