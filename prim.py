'''
Group 5
Animesh Gupta (201851153)
Deep Shah (201851037)

Prim's Algorithm

How to Run:
Scroll to bottom, change value for 'G', run the code in terminal
'''

import math

def printMST(G,ln,nbr):
    print("Edge \tDistance")
    for i in range(1, ln):
        print (nbr[i], "-", i, "\t", G[i][ nbr[i] ] )

def prim(G):
    inf = math.inf
    ln = len(G)

    visited = [0] * ln
    nbr = [-1] * ln
    dist = [inf] * ln
    dist[0] = 0

    for _ in range(ln):

        minm = inf

        for u1 in range(ln):
            if dist[u1] < minm and not visited[u1]:
                minm = dist[u1]
                u = u1

        visited[u] += 1

        for v in range(ln):
            if((not visited[v]) and (dist[v] > G[u][v] > 0)):
                dist[v] = G[u][v]
                nbr[v] = u

    printMST(G,ln,nbr)


if __name__ == "__main__":

    G = [ [0, 2, 0, 6, 0], [2, 0, 3, 8, 5], [0, 3, 0, 0, 7], [6, 8, 0, 0, 9], [0, 5, 7, 9, 0]]

    prim(G)
