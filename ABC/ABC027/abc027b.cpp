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

int main(){
    cin.tie(0);
    ios::sync_with_stdio(false);

    int n;
    cin >> n;

    int peoples[n];
    int sumpeoples = 0;
    REP(i, n) {
        int p;
        cin >> p;
        peoples[i] = p;
        sumpeoples += p;
    }

    if(sumpeoples % n != 0) {
        cout << "-1" << endl;
    } else {
        int pp = sumpeoples / n;  // perpeople
        int res = 0;
        REP(i, n-1) {
            int left = 0;
            FOR(j, 0, i+1) {
                left += peoples[j];
            }
            int right = 0;
            FOR(j, i+1, n) {
                right += peoples[j];
            }

            // cout << "DEBUG: " << left << " " << (i+1) * pp << endl;
            // cout << "DEBUG: " << right << " " << (n-i-1) * pp << endl;
            if(left != (i+1) * pp && right != (n-i-1) * pp) {
                res++;
            }
        }

        cout << res << endl;
    }

    return 0;
}
