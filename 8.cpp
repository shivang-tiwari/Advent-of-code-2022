// हर हर महादेव
#include <bits/stdc++.h>
using namespace std;


vector<int> dx = {-1,1,0,0};
vector<int> dy = {0,0,1,-1};

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
	
	int ans = 0;
	
	for(int i = 0; i < n; i++){
		for(int j = 0; j < m; j++){
			int here = 1;
			for(int k = 0; k < 4; k++){
				int x = i + dx[k],y = j + dy[k],cnt = 1;
				while(x >= 0 && y >= 0 && x < n && y < m && a[x][y] < a[i][j]){
					x += dx[k];
					y += dy[k];
					cnt++;
				}
				if(!(x >= 0 && y >= 0 && x < n && y < m)){
					cnt--;
				}
				here *= cnt;
			}
			ans = max(ans,here);
			
		}
	}
	cout << ans;
	return 0;
}
