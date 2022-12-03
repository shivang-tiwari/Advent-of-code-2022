// हर हर महादेव
#include <bits/stdc++.h>
using namespace std;

int priority(char c){
	return c >= 'a' && c <= 'z' ? c-'a'+1 : 26 + c-'A'+1;
}

string com(string s,string t){
	set<char> all(s.begin(),s.end());
	string res;
	for(char c : t){
		if(all.find(c) != all.end()){
			res += c;
		}
	}
	return res;
}


int solve(vector<string> a){
	string res = a[0];
	for(auto p : a){
		res = com(res,p);
	}
	return priority(res[0]);
}

int main(){
	#ifdef shivang_ka_laptop
		freopen("in.txt" , "r", stdin);
	#endif
	
	string s;
	int ans = 0;
	vector<string> a;
	while(cin >> s){
		a.push_back(s);
		if(a.size() == 3){
			ans += solve(a);
			a.clear();
		}
	}
	cout << ans;
	return 0;
}

