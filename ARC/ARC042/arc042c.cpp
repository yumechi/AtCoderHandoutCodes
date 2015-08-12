#include <iostream>
#include <cstdio>
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
#define MP make_pair
#define mp make_pair
#define pb push_back
#define PB push_back
#define DEBUG(x) cout<<#x<<": "<<x<<endl
#define ll long long
#define ull unsigned long long

int dp[5005];

int main(){
    cin.tie(0);
    ios::sync_with_stdio(false);
    cout.precision(16);

    int n, p;
    cin >> n >> p;

    vector< pair<int, int> > data(n);
    REP(i, n) {
        cin >> data[i].first >> data[i].second;
    }

    sort(data.begin(), data.end());
    reverse(data.begin(), data.end());

    int res = 0;
    REP(i, n) {
        int f = data[i].first;
        int s = data[i].second;
        RREP(j, p) {
            if(j+f <= p) {
                dp[j+f] = max(dp[j+f], s+dp[j]);
            }
        }

        // put on next data
        if(i < n-1) res = max(res, dp[p]+data[i+1].second);
        /*  DEBUG
        REP(j, p+1) cout << dp[j] << " ";
        cout << endl;
        DEBUG(res);
        */
    }

    cout <<  max(res, dp[p]) << endl;
    return 0;
}
