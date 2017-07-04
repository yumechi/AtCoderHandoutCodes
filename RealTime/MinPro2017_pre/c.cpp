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

void solve() {
    int n, k;

    cin >> n >> k;
    if(n == k) {
        cout << "" << endl;
        return;
    }

    int alist[k];
    REP(i, k) {
        cin >> alist[i];
        alist[i]--;
    }
    string slist[n];
    REP(i, n) cin >> slist[i];

    vector<pair<string, bool> > newlist(n);
    string minword = "";
    REP(i, n) {
        bool flag = false;
        for(int j = 0; j < k; j++) {
            if(alist[j] == i) {
                flag = true;
                break;
            }
        }

        if(flag) {
            newlist[i] = mp(slist[i], true);
            if(minword.length() == 0) {
                minword = slist[i];
            }
            if(slist[i].length() < minword.length()) {
                minword = slist[i];
            }
        } else {
            newlist[i] = mp(slist[i], false);
        }
    }

    int wordindex = 0;
    string ans = "";
    while(wordindex < minword.length()) {
        bool flag = false;
        ans += minword[wordindex];
        for(auto elem : newlist) {
            if(elem.second) {
                if(elem.first.find(ans) != 0) {
                    cout << "-1" << endl;
                    return;
                }
            } else {
                if(elem.first.find(ans) == 0) {
                    flag = true;
                    break;
                }
            }
        }
        if(!flag) {
            cout << ans << endl;
            return;
        }
        wordindex++;
    }

    cout << "-1" << endl;
}


int main(){
    cin.tie(0);
    ios::sync_with_stdio(false);
    cout.precision(16);

    solve();

    return 0;
}
