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
#define INF 1<<29
#define ALEN(ARR) (sizeof(ARR) / sizeof((ARR)[0]))
#define MP make_pair
#define mp make_pair
#define pb push_back
#define PB push_back
#define _DEBUG(x) cout<<#x<<": "<<x<<endl
#define _DDEBUG(x,y) cout<<#x<<": "<<x<<", "<<#y<<": "<<y<<endl
#define ll long long
#define ull unsigned long long
#define MOD 1000000007
#define MAXNUM 1000000

int MODS[MAXNUM + 1];
int MODPAIRS[MAXNUM + 1];
int PAIRS[MAXNUM + 1];


int main(){
	cin.tie(0);
	ios::sync_with_stdio(false);
	cout.precision(16);

	int n, m;
	int ans = 0;
	cin >> n >> m;

	REP(i, n) {
		int t;
		cin >> t;
		MODS[t % m]++;
		PAIRS[t]++;
	}

	REP(i, MAXNUM + 1) {
		if(PAIRS[i] > 0) {
			MODPAIRS[i] += PAIRS[i];
		}
	}

	int midlow = m / 2;
	int midhigh = (m + 1) / 2;
	while(midlow >= 0 && midhigh <= m) {
		int t = min(MODS[midlow], MODS[midhigh]);
		ans += t;
		if(MODPAIRS[midlow] - t * 2 >= 2) {
			ans += MODPAIRS[midlow] / 2;
		}
		if(MODPAIRS[midhigh] - t * 2 >= 2) {
			ans += MODPAIRS[midhigh] / 2;
		}
		midlow--;
		midhigh++;
	}

	ans += MODPAIRS[0] / 2;

#if DEBUG
	cout << "** RESULT **" << endl; // debug
#endif
	cout << ans << endl;
	
	return 0;
}
