/// Hopcroft-Karp Algorithm ///


#include<bits/stdc++.h>
using namespace std;

list<int> *G;

bool bfs(int *setU, int *setV, int *dist, int m)
{
	queue<int> que;

	for (int u=1; u<=m; u++)
	{
		if (setU[u]==0)
		{
			dist[u] = 0;
			que.push(u);
		}

		else dist[u] = INT_MAX;
	}

	dist[0] = INT_MAX;

	while (!que.empty())
	{
		int u = que.front();
		que.pop();

		if (dist[u] < dist[0])
		{
			list<int>::iterator i;
			for (i=G[u].begin(); i!=G[u].end(); ++i)
			{
				int v = *i;

				if (dist[setV[v]] == INT_MAX)
				{
					dist[setV[v]] = dist[u] + 1;
					que.push(setV[v]);
				}
			}
		}
	}

	return (dist[0] != INT_MAX);
}

bool dfs(int u, int *setU, int *setV, int *dist)
{
	if (u != 0)
	{
		list<int>::iterator i;

		for (i=G[u].begin(); i!=G[u].end(); ++i) {

			int v = *i;
            if ((dist[setV[v]] == dist[u]+1) && dfs(setV[v], setU, setV, dist))
            {
                setU[u] = v;
                setV[v] = u;
                return true;
            }
		}

		dist[u] = INT_MAX;
		return false;
	}

	return true;
}

void hopcroft_karp(int m, int n)
{
	int setU[m+1], setV[n+1], dist[m+1];

	for (int u=0; u<=m; u++)
		setU[u] = 0;

	for (int v=0; v<=n; v++)
		setV[v] = 0;

	int cnt = 0;

	while (bfs(setU, setV, dist, m)) {
		for (int u=1; u<=m; u++) {
			if (!setU[u] && dfs(u, setU, setV, dist))
                cnt++;
		}
	}

    cout << "\nMaximum Matching:" << endl;
    for(int i=1; i<cnt+1; i++)
         cout << "u" << setU[i] << " - v" << setV[i] << endl;

	cout << "\nCount: " << cnt << endl;
}

int main()
{
	int n;
	cout << "Enter no. of edges: " << flush;
	cin >> n;
	G = new list<int>[n+1];
	cout << "Enter space seperated end-points for each edge (start at 1) \n" << endl;
	cout << "U V" << endl;
	int u_max=0, v_max=0;
	for(int i=0; i<n; i++){
        int u, v;
        cin >> u >> v;
        if(u>u_max) u_max = u;
        if(v>v_max) v_max = v;
        G[u].push_back(v);
	}

	hopcroft_karp(u_max, v_max);

  // Example 1    Example 2
	// u1 - v2      u1 - v1
	// u1 - v3      u1 - v3
	// u2 - v1      u2 - v3
	// u3 - v2      u3 - v4
	// u4 - v2      u4 - v3
	// u4 - v4      u4 - v2

	return 0;
}
