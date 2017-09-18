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
 
	int n, m, r;
	cin >> n >> m >> r;
    n++;
 
	d = Metrics(n, vector<ll>(n, 100000000000000));
	REP(i, n) d[i][i] = 0;
 
    vector<int> goal(r);
    REP(i, r) cin >> goal[i];
    sort(goal.begin(), goal.end());
    
    REP(i, m) {
		int from, to;
        ll cost;
		cin >> from >> to >> cost;
		d[from][to] = cost;
		d[to][from] = cost; // if undirected graph
    }
 
    warshall_floyd(n);
 
    ll ans = 1000000000000000;
    do {
         ll t = 0;
         REP(i, r-1) {
            t += d[ goal[i] ][ goal[i+1] ];
         }
         ans = min(ans, t);
    } while(next_permutation(goal.begin(), goal.end()));
 
    cout << ans << endl;
 
    return 0;
}
