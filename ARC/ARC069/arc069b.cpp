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

int main(){
    cin.tie(0);
    ios::sync_with_stdio(false);
    cout.precision(16);

    int n;
    string line;
    cin >> n >> line;

    string ans = "";
    REP(i, 4) {
        string t_ans = "";
        int t = i;
        REP(j, 2) {
            t_ans += t & 1 ? "W" : "S";
            t >>= 1;
        }
        FOR(j, 2, n) {
            if(t_ans[j-1] == 'S') {
                if(line[j-1] == 'o') {
                    t_ans += t_ans[j-2] == 'S' ? "S" : "W";
                } else {
                    t_ans += t_ans[j-2] == 'S' ? "W" : "S";
                }
            } else {
                if(line[j-1] == 'o') {
                    t_ans += t_ans[j-2] == 'S' ? "W" : "S";
                } else {
                    t_ans += t_ans[j-2] == 'S' ? "S" : "W";
                }
            }
        }
#if DEBUG
        cout << t_ans << endl;
#endif
        string decode_check = "";
        REP(j, n) {
            if(t_ans[j] == 'S') {
                if(t_ans[(n+j-1) % n] == t_ans[(n+j+1) % n]) {
                    decode_check += "o";
                } else {
                    decode_check += "x";
                }
            } else {
                if(t_ans[(n+j-1) % n] == t_ans[(n+j+1) % n]) {
                    decode_check += "x";
                } else {
                    decode_check += "o";
                }
            }
        }
#if DEBUG
        cout << decode_check << endl;
#endif
        if(decode_check == line) {
            ans = t_ans;
            break;
        }
    }

#if DEBUG
    cout << "** RESULT **" << endl; // debug
#endif
    cout << (ans.length() == 0 ? "-1" : ans) << endl;

    return 0;
}
