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

int main(){
  cin.tie(0);
  ios::sync_with_stdio(false);
  cout.precision(16);

  int n, t;
  cin >> n >> t;

  int A[n];
  int B[n];
  vector< vector<int> > D(n);
  int sa=0, sb=0;

  REP(i, n) {
      int a, b;
      cin >> a >> b;
      A[i]=a, B[i]=b;
      sa+=a, sb+=b;

      vector<int> delem(2);
      int d = a-b;
      delem[0] = d, delem[1] = i;
      D[i] = delem;
  }

  if(sa <= t) {
      cout << "0" << endl;
      return 0;
  } else if(sb > t) {
      cout << "-1" << endl;
      return 0;
  }

  sort(D.begin(), D.end());
  int res = 0;
  int l = D.size() - 1;
  while(sa > t) {
      vector<int> t = D.at(l);
      int idx = t[1];
      A[idx] = B[idx];
      sa -= t[0];
      res++; l--;
  }

  cout << res << endl;
  return 0;
}
