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
#define INF 1<<30
#define MP make_pair
#define mp make_pair
#define pb push_back
#define PB push_back
#define DEBUG(x) cout<<#x<<": "<<x<<endl
#define ll long long
#define ull unsigned long long
#define MOD 1000000007

bool graph[21][21];

int main(){
    cin.tie(0);
    ios::sync_with_stdio(false);
    cout.precision(16);

    int V, E, K;
    cin >> V >> E >> K;

    REP(i, E) {
        int a, b;
        cin >> a >> b;
        graph[a][b] = true;
        graph[b][a] = true;
    }

    REP(i, (int)pow(2.0, V)+1) {
        int t = i;
        int depth = 0;
        int count = 0;
        int bit[V];
        REP(j, V) bit[j] = (i & (int)(pow(2.0, j))) > 0 ? 1 : 0;
        while(t > 0) {
            if((t & 1) == 1) {
                count++;
                REP(j, V) {
                    if(graph[depth][j] && bit[j] == 1) {
                        count = 0; depth = 0; t = 0;
                        goto LAST;
                    }
                }
            }
            depth++;
            t >>= 1;
        }

        // print out
        if(count >= K) {
            REP(j, V) {
                if(bit[j] == 1) cout << j << endl;
            }
            goto finish;
        }
        LAST:;
    }

    finish:
    return 0;
}
