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
#include <iterator>

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

/** FOR VECTOR DEBUG */
template <typename T>
ostream& operator<< (ostream& out, const vector<T>& v) {
  if ( !v.empty() ) {
    out << '[';
    copy (v.begin(), v.end(), ostream_iterator<T>(out, ", "));
    out << "\b\b]";
  }
  return out;
}


int main(){
	cin.tie(0);
	ios::sync_with_stdio(false);
	cout.precision(16);

    int n, mink;
    cin >> n >> mink;

    int xs[n];
    int ys[n];
    REP(i, n) cin >> xs[i] >> ys[i];

    set<int> xst(xs, xs + n);
    set<int> yst(ys, ys + n);

    ll ans = 1LL * (*xst.rbegin() - *xst.begin()) * (*yst.rbegin() - *yst.begin());

    REP(i, xst.size()) {
        FOR(j, i + 1, xst.size()) {
            REP(k, yst.size()) {
                FOR(l, k + 1, yst.size()) {

                    auto xiter1 = xst.begin();
                    auto xiter2 = xst.begin();
                    advance(xiter1, i);
                    advance(xiter2, j);
                    int ix = min(*xiter1, *xiter2);
                    int jx = max(*xiter1, *xiter2);
                    
                    auto yiter1 = yst.begin();
                    auto yiter2 = yst.begin();
                    advance(yiter1, k);
                    advance(yiter2, l);
                    int ky = min(*yiter1, *yiter2);
                    int ly = max(*yiter1, *yiter2);

                    int count = 0;
                    REP(m, n) {
                        if(ix <= xs[m] && xs[m] <= jx 
                                && ky <= ys[m] && ys[m] <= ly) {
                            count++;
                        }
                    }

                    if(count >= mink) {
                        ans = min(ans, 1LL * (jx - ix) * (ly - ky));
                    }
                }
            }
        }
    }
#if DEBUG
	cout << "** RESULT **" << endl; // debug
#endif
    cout << ans << endl;	
	return 0;
}
