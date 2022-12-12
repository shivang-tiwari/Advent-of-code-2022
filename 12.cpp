// हर हर महादेव
#include <bits/stdc++.h>
using namespace std;
vector<int> dx = {-1,1,0,0};
vector<int> dy = {0,0,1,-1};

vector<int> pre;
vector<int> dist;
void dijkstra(int start,vector<vector<int>> &adj){
	dist.clear();dist.resize(adj.size(),1e9 + 50);
	pre.clear();pre.resize(adj.size(),-1);
	queue<pair<int,int>> que;
	que.push({dist[start] = 0, start});
	while (!que.empty()) {
		auto top = que.front();
		que.pop();
		if (top.first != dist[top.second]) continue;
		for(auto node : adj[top.second])
			if(dist[node] > top.first + 1) 
				que.push({dist[node] = top.first + 1, node}), pre[node] = top.second;
	}
}


int main(){
	#ifdef shivang_ka_laptop
		freopen("in.txt" , "r", stdin);
	#endif
	vector<string> a;
	string s;
	while(cin >> s){
		a.push_back(s);
	}
	int n = a.size(),m = a[0].size();
	
	auto id = [&](int i,int j){
		return i*m + j;
	};
	
	auto ok = [&](int i,int j){
		return min(i,j) >= 0 && i < n && j < m;
	};
	
	auto mp = [&](char c){
		if(c == 'S'){
			return 'a';
		}
		if(c == 'E'){
			return 'z';
		}
		return c;
	};
	
	auto can = [&](int i,int j,int x,int y){
		assert(ok(i,j));
		if(!ok(x,y)){
			return false;
		}
		return mp(a[x][y]) - mp(a[i][j]) <= 1;
	};
	
	
	vector<vector<int>> graph(n*m);
	
	auto addEdge = [&](int u,int v){
		graph[u].push_back(v);
	};
	int st = -1,en = -1;
	for(int i = 0; i < n; i++){
		for(int j = 0; j < m; j++){
			for(int k = 0; k < 4; k++){
				int x = i + dx[k],y = j + dy[k];
				if(can(i,j,x,y)){
					addEdge(id(x,y),id(i,j));
				}
				if(a[i][j] == 'S'){
					st = id(i,j);
				}
				if(a[i][j] == 'E'){
					en = id(i,j);
				}
			}
		}
	}
	dijkstra(en,graph);
	int best = 1e9 + 5;
	for(int i = 0; i < n; i++){
		for(int j = 0; j < m; j++){
			if(mp(a[i][j]) == 'a'){
				best = min(best,dist[id(i,j)]);
			}
		}
	}
	cout << best;
	return 0;
}

