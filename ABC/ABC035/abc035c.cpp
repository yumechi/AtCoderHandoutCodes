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
#define DEBUG(x) cout<<#x<<": "<<x<<endl
#define DDEBUG(x,y) cout<<#x<<": "<<x<<", "<<#y<<": "<<y<<endl
#define ll long long
#define ull unsigned long long
#define MOD 1000000007

int memo[200010];

int main(){
	cin.tie(0);
	ios::sync_with_stdio(false);
	cout.precision(16);
	
	int n, q;
	cin >> n >> q;
	
	int l, r;
	REP(i, q) {
		cin >> l >> r;
		l--;
		memo[l]--; memo[r]++;
	}

	string res("");
	int cnt = memo[0];
	FOR(i, 1, n+1) {
		res += abs(cnt) % 2 == 0 ? "0" : "1";
		cnt += memo[i];
	}

	// cout << "** RESULT **" << endl; // debug
	cout << res << endl;
	
	return 0;
}
