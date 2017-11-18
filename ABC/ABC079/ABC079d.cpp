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

// refer:
// http://dai1741.github.io/maximum-algo-2012/docs/shortest-path/
typedef vector<vector<int> > Metrics;
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

void debugprint(int n) {
	REP(i, n) {
		REP(j, n) {
			if (i != j && d[i][j] != INF) {
				cout << i << "から" << j << "へのコスト: " << d[i][j] << endl;
			}
		}
	}
}

int main(){
	cin.tie(0);
	ios::sync_with_stdio(false);
	cout.precision(16);

    int h, w;
    cin >> h >> w;

    const int cmax = 10;
	d = Metrics(cmax, vector<int>(cmax, INF));
	REP(i, cmax) d[i][i] = 0;

	REP(i, cmax) {
        REP(j, cmax) {
            int from, to, cost;
            cin >> cost;
            from = i, to = j;
            d[from][to] = cost;
        }
    }

    warshall_floyd(cmax);

    // Aの読み込み始めますよお
    ll ans = 0;
    REP(i, h) {
        REP(j, w) {
            int t;
            cin >> t;
            if(t == -1 || t == 1) continue;
            ans += d[t][1];
        }
    }

    cout << ans << endl;

    return 0;
}
