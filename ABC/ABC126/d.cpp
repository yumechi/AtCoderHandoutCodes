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
vector<int> mark;
vector<bool> checked;
vector<vector<pair<int, int>>> vvp;
int current_mark = -1;

void dfs(int index) { 
    if(current_mark == -1) {
        mark[1] = 0;
        current_mark = 0;
    }
    for(int i = 0; i < vvp[index].size(); i++) {
        int n = vvp[index][i].first;
        int c = vvp[index][i].second;
        if(checked[n]) {
            continue;
        }
        mark[n] = c % 2 == 1 ? (mark[index] ^ 1) : mark[index];
        checked[n] = true;
        dfs(n);
    }
}

int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);
    cout.precision(16);

    int n;
    cin >> n;

    mark.resize(n + 1);
    checked.resize(n + 1);
    vvp.resize(n + 1);

    REP(i, n - 1) {
        int u, v, w;
        cin >> u >> v >> w;
        vvp[u].push_back(make_pair(v, w));
        vvp[v].push_back(make_pair(u, w));
    }

    dfs(1);

    for(int i = 1; i <= n; i++) {
        cout << mark[i] << endl;
    }

    return 0;
}
