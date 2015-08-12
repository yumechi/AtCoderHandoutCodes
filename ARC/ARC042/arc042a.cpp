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
  cout.precision(16);

  int n, m;
  cin >> n >> m;

  int thre[n];
  REP(i, n) thre[i] = i+1;

  int writecheck[m];
  REP(i, m) cin >> writecheck[i];

  int res[n];
  int counter = 0;
  RREP(i, m) {
      int current = writecheck[i];
      if(thre[current-1] > 0) {
          res[counter++] = current;
          thre[current-1] = 0;
      }
  }

  REP(i, n) {
      if(thre[i] > 0)  res[counter++] = thre[i];
  }

  REP(i, n) cout << res[i] << endl;

  return 0;
}
