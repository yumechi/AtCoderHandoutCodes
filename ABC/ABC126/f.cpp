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
#define INF (1<<30)
#define ALEN(ARR) (sizeof(ARR) / sizeof((ARR)[0]))
#define MP make_pair
#define mp make_pair
#define pb push_back
#define PB push_back

#if DEBUG
#define _DEBUG(x) cout<<#x<<": "<<x<<endl
#define _DDEBUG(x,y) cout<<#x<<": "<<x<<", "<<#y<<": "<<y<<endl
#else
#define _DEBUG(x) ;
#define _DDEBUG(x,y) ;
#endif

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

/* template end */

int main(){
    cin.tie(0);
    ios::sync_with_stdio(false);
    cout.precision(16);

    ll m, k;
    cin >> m >> k;
    ll p2m = pow(2, m);

    if(m <= 1) {
        if(k == 0) {
            cout << (m == 0 ? "0 0" : "0 0 1 1") << endl;
        } else {
            cout << -1 << endl;
        }
        return 0;
    }

    if(k >= pow(2, m)) {
        cout << -1 << endl;
        return 0;
    }

    vector<ll> b(p2m);
    vector<ll> c(p2m);
    for(ll i = 0; i < p2m; i++) {
        b[i] = i;
        c[p2m - i - 1] = i;
    }
    b.erase(b.begin() + k);
    c.erase(c.begin() + (p2m - k - 1));
    
    vector<ll> ans(p2m * 2);
    ll idx = 0;
    for(auto bi : b) { ans[idx] = bi; idx++; }
    ans[idx++] = k;
    for(auto ci : c) { ans[idx] = ci; idx++; }
    ans[idx++] = k;

    for(int i = 0; i < idx; i++) {
        cout << ans[i] << (i != idx - 1 ? ' ' : '\n');
    }  

    return 0;
}

