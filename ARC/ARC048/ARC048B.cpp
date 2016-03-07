#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <queue>

#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <functional>
using namespace std;
#define FOR(i,a,b) for (int i=(a);i<(b);i++)
#define RFOR(i,a,b) for (int i=(b)-1;i>=(a);i--)
#define REP(i,n) for (int i=0;i<(n);i++)
#define RREP(i,n) for (int i=(n)-1;i>=0;i--)
#define INF 1<<30
#define ALEN(ARR) (sizeof(ARR) / sizeof((ARR)[0]))
#define MP make_pair
#define mp make_pair
#define pb push_back
#define PB push_back
#define DEBUG(x) cout<<#x<<": "<<x<<endl
#define ll long long
#define ull unsigned long long
#define MOD 1000000007

int data[100000][2];
map<int, vector<int> > rate;
int result[100000][3];

int main(){
	cin.tie(0);
	ios::sync_with_stdio(false);
	cout.precision(16);

	int n;
	cin >> n;
	
	REP(i, n) {
		int r, h;
		cin >> r >> h;
		data[i][0] = r;
		data[i][1] = h;
		
		rate[r].pb(i);
		rate[r].pb(h);
	}
	
	int accu = 0;
	for(auto elem : rate) {
		int size = elem.second.size();

		if(size == 2) {
			result[elem.second[0]][0] = accu;
			result[elem.second[0]][1] = n - accu - 1;
		} else {
			for(int i = 1; i < 4; i++) {
				int tres[3] = {0, 0, 0};
				
				for(int j = 1; j < size; j += 2) {
					int t = (i - elem.second[j] + 3) % 3;
					if(t == 0) {
						tres[2]++;
					} else if(t == 1) {
						tres[1]++;
					} else {
						tres[0]++;
					}
				}
				
				for(int j = 0; j < size; j += 2) {
					if(elem.second[j+1] == i) {
						result[elem.second[j]][0] = tres[0] + accu;
						result[elem.second[j]][1] = tres[1] + (n - accu - size/2);
						result[elem.second[j]][2] = tres[2] - 1;
					}
				}
			}
		}
		
		accu += size/2;
	}
	
	// cout << "**RESULT**" << endl;
	REP(i, n) {
		cout << result[i][0] << " " << result[i][1] << " " << result[i][2] << endl;
	}
}
