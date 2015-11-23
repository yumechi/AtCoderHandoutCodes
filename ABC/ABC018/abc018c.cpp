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
#define ALEN(ARR) (sizeof(ARR) / sizeof((ARR)[0]))
#define MP make_pair
#define mp make_pair
#define pb push_back
#define PB push_back
#define DEBUG(x) cout<<#x<<": "<<x<<endl
#define ll long long
#define ull unsigned long long
#define MOD 1000000007

int main(){
  cin.tie(0);
  ios::sync_with_stdio(false);
  cout.precision(16);

  int r, c, k;
  cin >> r >> c >> k;

  bool table[r][c];
  string s;
  REP(i, r) {
      cin >> s;
      REP(j, c) {
          table[i][j] = (s.at(j) == 'o') ? true : false;
      }
  }

  int canup[r][c];
  int candown[r][c];
  REP(i, c) {
      int cnt = 0;
      // up count
      REP(j, r) {
          if(table[j][i]) cnt++;
          else cnt = 0;
          canup[j][i] = cnt;
      }

      // down count
      cnt = 0;
      RREP(j, r) {
          if(table[j][i]) cnt++;
          else cnt = 0;
          candown[j][i] = cnt;
      }
  }

  int res = 0;
  k--;
  FOR(i, k, r-k) {
      FOR(j, k, c-k) {
          bool flag = false;
          for(int l = -k; l <= k; l++) {
              if(min(candown[i][j+l], canup[i][j+l]) < (k - abs(l) + 1)) {
                  flag = true;
                  break;
              }
          }
          if(flag) continue;
          res++;
      }
  }

  cout << res << endl;
  return 0;
}
