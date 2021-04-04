'''
## Bellman-Ford Algorithm ##

Input format is no of vertices then no of edges and then starting vertex followed by directed edges with their weights)
Example:
input =
8 11 1
1 2 10
3 2 1
3 4 1
4 5 3
5 6 -1
7 6 -1
8 7 1
1 8 8
7 2 -4
2 6 2
6 3 -2

output =
1 2 5
1 3 5
1 4 6
1 5 9
1 6 7
1 7 9
1 8 8

'''

import math

def bellman_ford(G,s):
    n = len(G)
    dist=[math.inf]*n
    dist[s]=0

    for i in range(n):
        for u in range(n):
            for e in G[u]:
                v, w = e[0],e[1]
                if(dist[v] > (dist[u]+w)):
                    dist[v] = dist[u] + w

    for u in range(n):
        for v in G[u]:
            end_vertex, weight = v[0],v[1]
            if dist[end_vertex] > dist[u]+weight:
                return -1

    return dist

def main():
    print("")
    print("input = ")
    n, m, s = map(int, input().split())
    G = {}

    for i in range(n):
        G[i] = []

    for _ in range(m):
        u, v, w = map(int, input().split())
        G[u-1].append([v-1,w])

    out = bellman_ford(G,s-1)

    if(out != -1):
        print("output = ")
        for i,j in enumerate(out):
            if(s==(i+1)): continue;
            print(f"{s} {i+1} {j}")
    else:
        print("Negative Weight Cycle found")

    print("\n\n")

if __name__ == "__main__":
    main()
