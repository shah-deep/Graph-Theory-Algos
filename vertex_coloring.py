"""
Algo by:
Deep Shah

(e) deepshah11111@gmail.com
"""


def getColor(G,colors,coloring,u):
    col = 1
    for c in colors:
        for v in G[u]:
            if(coloring[v] == c):
                col = c+1

        if(col==c):
            return col

    return col


def Color(G):
    n = len(G)
    colors = set()
    coloring = [None]*n

    for u in range(n):
        color = getColor(G,colors,coloring,u)
        colors.add(color)
        coloring[u] = color

    return coloring


def main():

    colours = ["Red", "Blue", "Green", "Yellow", "White", "Purple", "Orange", "Olive", "Maroon", "Grey"]

    print("Enter no. of vertices, edges: ")
    n, m = map(int, input().split())

    G= {}
    for i in range(n):
        G[i] = []

    print("\nEnter Edges U-V")
    for _ in range(m):
        u, v = map(int, input().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)

    c = Color(G)

    print("\nVertex Coloring:")
    for i in range(n):
        print(f"{i+1} : {colours[c[i]-1]}")

if __name__ == "__main__":
    main()


'''
Example Input:
Enter no. of vertices, edges:
7 8

Enter Edges U-V
1 2
1 3
3 4
4 5
5 7
6 7
4 6
3 5
'''
