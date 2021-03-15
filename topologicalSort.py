'''
Group 5
Animesh Gupta (201851153)
Deep Shah (201851037)

Topological Sorting

'''

def topologicalSorting(G,n):
    enum = []

    indegree = [0]*n

    for i in range(n):
        indegree[i]=0
        for j in range(n):
            indegree[i] += G[j][i]

    def getStart(indegree):
        for i in range(n):
            if(indegree[i] == 0):
                return i
        return -1

    for i in range(n):
        j = getStart(indegree)
        if(j==-1):
            break
        enum.append(j)
        indegree[j] = -1
        for k in range(n):
            if(G[j][k] == 1):
                indegree[k] -= 1

    return enum


def main():
    n = int(input("Enter no. of Vertices: "))
    m = int(input("Enter no. of Edges: "))
    print("Enter space separated end-points for each edge (U->V) (Start at 0)\n\nU V")

    G = [[0 for col in range(n)]  for row in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        G[u][v]=1

    print("\nTopological Ordering: ")
    print(topologicalSorting(G,n))

if __name__ == "__main__":
    main()
