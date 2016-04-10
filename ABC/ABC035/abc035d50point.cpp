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
#define LINF 99999999999999999
#define ALEN(ARR) (sizeof(ARR) / sizeof((ARR)[0]))
#define MP make_pair
#define mp make_pair
#define pb push_back
#define PB push_back
#define DEBUG(x) cout<<#x<<": "<<x<<endl
#define DDEBUG(x,y) cout<<#x<<": "<<x<<", "<<#y<<": "<<y<<endl
#define ll long long
#define ull unsigned long long
#define MOD 1000000007

typedef vector<vector<ll> > Metrics;
Metrics d;

void warshall_floyd(int n) { // n:頂点数
	REP(i, n) {	// 経由する頂点
		REP(j, n) {	// 開始頂点
			REP(k, n) {	// 終端
				d[j][k] = min(d[j][k], d[j][i] + d[i][k]);
			}
		}
	}
}

ll money[100010];

int main(){
	cin.tie(0);
	ios::sync_with_stdio(false);
	cout.precision(16);

	int n, m, t;
	cin >> n >> m >> t;

	REP(i, n) cin >> money[i];

	d = Metrics(n, vector<ll>(n, LINF));
	REP(i, n) d[i][i] = 0;

	REP(i, m) {
		int from, to, cost;
		cin >> from >> to >> cost;
		from--; to--;
		d[from][to] = cost;
		// d[to][from] = cost; // if undirected graph
    }

    warshall_floyd(n);

	ll ans = money[0] * t;
	FOR(i, 1, n) {
		if(d[0][i] == LINF || d[i][0] == LINF) continue;
		ll temp = (t - (d[0][i] + d[i][0])) * money[i];
		ans = max(temp, ans);
	}

	// cout << "**RESULT**" << endl;
	cout << ans << endl;
}
