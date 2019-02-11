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
int dp[200010][5];

int min_num(int a[], int l) {
    int r = INF;
    for(int i = 0; i <= l; i++) {
        r = min(r, a[i]);
    }
    return r;
}

int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);
    cout.precision(16);

    int n;
    cin >> n;
    vector<int> v(n);
    REP(i, n) {
        cin >> v[i];
    }

    for(int i = 0; i < n + 1; i++) {
        for(int j = 0; j < 5; j++) {
            dp[i][j] = INF;
        }
    }
    dp[0][0] = 0;

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < 5; j++) {
            int add_cost = [&] {
                if(j == 0 || j == 4) {
                    return v[i];
                }
                if(j == 1 || j == 3) {
                    return v[i] == 0 ? 2 : v[i] % 2;
                }
                return (v[i] % 2) ^ 1;
            }();
            dp[i + 1][j] = min(dp[i + 1][j], min_num(dp[i], j) + add_cost);
        }
    }

    int ans = INF;
    REP(i, 5) {
        ans = min(ans, dp[n][i]);
    }

#if DEBUG
    cout << "** RESULT **" << endl; // debug
#endif
    cout << ans << endl;
    return 0;
}
