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

  int n, m, s;
  cin >> n >> m >> s;

  map<int, int> comedata;
  REP(i, n) {
      int t, k;
      cin >> t >> k;
      comedata[t] = k;
  }

  int res = 0;
  int current = 0;
  REP(i, s+1) {
      if(current >= m) {
          res++;
      }

      if(comedata.count(i) != 0) {
          current += comedata[i];
      }
  }

  cout << res << endl;
  return 0;
}
