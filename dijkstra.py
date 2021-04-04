'''
Dijkstra's Algorithm

How to Run:
Scroll to bottom, change values for 'G' and 's', run the code in terminal
'''

import math

def dijkstra_list(dictionary,src):
    n = len(dictionary)
    dist=[math.inf]*n
    dist[src]=0
    visited=[0]*n

    queue=[]

    queue.append([0,src])
    while(len(queue)>0):
        t = queue.pop()
        u = t[1]
        visited[u]+=1

        for v in dictionary[u]:
            weight, end_vertex = v[0],v[1]
            # print(u,end_vertex)
            if dist[end_vertex] > dist[u]+weight:
                dist[end_vertex] = dist[u]+weight
            if visited[end_vertex]==0:
                queue.append([weight,end_vertex])
        queue = sorted(queue)

    return dist



def dijkstra_mat(G,src,ln):
    dist = [math.inf] * ln
    dist[src] = 0
    found = [0] * ln
    u = src
    for _ in range(ln):
        minm = math.inf
        for u1 in range(ln):
            if dist[u1] < minm and not found[u1]:
                minm = dist[u1]
                u = u1
        found[u]+=1
        for v in range(ln):
            if((not found[v] and G[u][v]) and (dist[v] > dist[u] + G[u][v])):
                 dist[v] = dist[u] + G[u][v]
    return dist


def driver(G,s):
    adjacency_list = mat_to_list(G)
    output = dijkstra_list(adjacency_list,s)
    print(f"\nusing adjacency list...............")
    for i,j in enumerate(output):
        print(f"\t\t {i} : {j}")
    print("\n\n")


    ln = len(G)
    out = dijkstra_mat(G,s,ln)
    print(f"using adjacency matrix...............")
    for i,j in enumerate(output):
        print(f"\t\t {i} : {j}")
    print()


def mat_to_list(G):
    dictionary={}
    n = len(G)
    for i in range(n):
        t = []
        for j in range(n):
            if G[i][j]>0:
                t.append([G[i][j],j])
        dictionary[i]=t
    return dictionary



if __name__ == "__main__":

    G = [[0,4,2],[4,0,1],[2,1,0]]
    s = 0

    driver(G,s)
