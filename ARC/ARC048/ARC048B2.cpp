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

map<int, vector< pair<int, int> > > rate;
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
		rate[r].pb(mp(i, h));
	}

	int accu = 0;
	for(auto elem : rate) {
		int size = elem.second.size();
		if(size == 1) {
			int f = elem.second[0].first;
			result[f][0] = accu;
			result[f][1] = n - accu - 1;
		} else {
			for(int i = 1; i < 4; i++) {
				int tres[3] = {accu, (n - accu - size), -1};
				REP(j, size) tres[abs((i - elem.second[j].second + 3) % 3 - 2)]++;

				REP(j, size) {
					int f = elem.second[j].first;
					int s = elem.second[j].second;
					if(s == i) {
						result[f][0] = tres[0];
						result[f][1] = tres[1];
						result[f][2] = tres[2];
					}
				}
			}
		}
		accu += size;
	}

	// cout << "**RESULT**" << endl;
	REP(i, n) cout << result[i][0] << " " << result[i][1] << " " << result[i][2] << endl;
}
