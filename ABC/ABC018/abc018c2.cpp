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
      int last = 0;
      int now = 0;
      int cnt = 0;

      // up count
      while(cnt < r) {
          while(cnt < r && table[cnt][i]) cnt++;
          if(cnt < r) {
              canup[cnt][i] = 0;
          } else {
              break;
          }
          now = cnt;
          int t = now;
          while(last <= --now) canup[now][i] = now - last + 1;
          last = t + 1;
          cnt = t + 1;
      }
      now = cnt - 1;
      while(last <= now) {
          canup[now][i] = now - last + 1;
          now--;
      }
      // down count
      last = r - 1;
      cnt = r - 1;
      while(cnt >= 0) {
          while(cnt >= 0 && table[cnt][i]) cnt--;
          if(cnt >= 0) {
              candown[cnt][i] = 0;
          } else {
              break;
          }
          now = cnt;
          int t = now;
          while(now < last) {
              candown[now+1][i] = last - now;
              now++;
          }
          last = t - 1;
          cnt = t - 1;
      }
      now = 0;
      while(now <= last) {
          candown[now][i] = last - now + 1;
          now++;
      }
  }

/*
  // DEBUG
  cout << endl;
  REP(i, c) {
      REP(j, r) {
          DEBUG(canup[j][i]);
      }
      cout << endl;
  }
  cout << endl;
  REP(i, c) {
      REP(j, r) {
          DEBUG(candown[j][i]);
      }
      cout << endl;
  }
*/

  int res = 0;
  FOR(i, k-1, r-k+1) {
      FOR(j, k-1, c-k+1) {
          bool flag = false;
          FOR(l, j-k+1, j) {
              int num = l - (j-k+1) + 1;
              if(candown[i][l] < num || canup[i][l] < num) {
                  flag = true;
                  break;
              }
          }
          if(flag) continue;
          FOR(l, j, j+k) {
              int num = k - (l - j);
              if(candown[i][l] < num || canup[i][l] < num) {
                  flag = true;
                  break;
              }
          }
          if(flag) continue;
          // cout << "OK: " << i << " " << j << endl;
          res++;
      }
  }

  cout << res << endl;
  return 0;
}
