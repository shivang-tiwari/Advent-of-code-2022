// हर हर महादेव
#include <bits/stdc++.h>
using namespace std;

string dir = "DURL";
vector<int> dx = {1,-1,0,0};
vector<int> dy = {0,0,1,-1};


struct knot{
	int x;
	int y;
	pair<int,int> last;
	
	knot(int _x,int _y){
		x = _x;
		y = _y;
	}
	
	knot(pair<int,int> p){
		x = p.first;
		y = p.second;
	}
	knot(){
		x = 0;
		y = 0;
	}
	void move(string s){
		last = {x,y};
		for(int k = 0; k < 4; k++){
			if(dir[k] == s[0]){
				x += dx[k];
				y += dy[k];
				return;
			}
		}
		assert(false);
	}
	void move(knot rp){
		int xx = rp.x - x, yy = rp.y - y;
		if(abs(xx) > 1){
			xx = red(xx);
		}
		if(abs(yy) > 1){
			yy = red(yy);
		}
		x += xx; y += yy;
		last = {x-xx,y-yy};
	}
	private:
	int red(int z){
		if(z == 0)return 0;
		return (z < 0 ? -1 : 1) * (abs(z)-1);
	}
};

bool nbr(const knot& p1, const knot &p2){
	return abs(p1.x-p2.x) <= 1 && abs(p1.y-p2.y) <= 1;
}


const int N = 10;

int main(){
	#ifdef shivang_ka_laptop
		freopen("in.txt" , "r", stdin);
	#endif
	vector<knot> rope(N,knot(15,11));
	string s;
	set<pair<int,int>> all;
	while(cin >> s){
		int n;
		cin >> n;
		while(n--){
			rope[0].move(s);
			for(int i = 1; i < N; i++){
				if(!nbr(rope[i-1],rope[i])){
					rope[i].move(rope[i-1]);
				}
			}
			all.insert({rope[N-1].x,rope[N-1].y});
		}
	}
	cout << all.size();
	return 0;
}
