// हर हर महादेव
#include <bits/stdc++.h>
#define int long long int
using namespace std;
const int N = 100100;
const int tot = 70000000;
const int thres = 30000000;

vector<string> split(string s){
	vector<string> a;
	string yet;
	for(char c : s){
		if(c == ' '){
			a.push_back(yet);
			yet.clear();
		}
		else{
			yet += c;
		}
	}
	a.push_back(yet);
	return a;
}


int32_t main(){
	#ifdef shivang_ka_laptop
		freopen("in.txt" , "r", stdin);
	#endif
	
	string s;
	vector<vector<int>> graph(N);
	vector<int> par(N,-1);
	vector<int> wt(N);
	vector<string> id(N);
	
	id[0] = "/";
	
	auto addEdge = [&](int u,int v){
		if(par[v] != -1){
			assert(par[v] == u);
			return;
		}
		graph[u].push_back(v);
		par[v]= u;
	};
	
	int cur = 0,cnt = 0;
	while(true){
		getline(cin,s);
		if(s == "-1"){
			break;
		}
		vector<string> a = split(s);
		if(a[0] == "$"){
			if(a[1] == "cd"){
				if(a[2] == ".."){
					cur = par[cur];
				}
				else if(a[2] == "/"){
					cur = 0;
				}
				else{
					for(int x : graph[cur]){
						if(id[x] == a[2]){
							cur = x;
							break;
						}
					}
				}
			}
			continue;
		}
		if(isdigit(a[0][0])){
			wt[cur] += stoll(a[0]);
		}
		else{
			assert(a[0] == "dir");
			id[++cnt] = a[1];
			addEdge(cur,cnt);
		}
	}
	
	function<void(int)> dfs = [&](int i){
		for(int x : graph[i]){
			dfs(x);
			wt[i] += wt[x];
		}
	}; dfs(0);
	
	int need = thres - (tot - wt[0]);
	
	int ans = 1e18;
	for(int i = 0; i < N; i++){
		if(wt[i] >= need){
			ans = min(ans,wt[i]);
		}
	}
	cout << ans;
	return 0;
}
