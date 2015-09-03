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

  int N, A, B;
  cin >> N >> A >> B;

  ll S[N];
  int maxm = 0, minm = INF;
  double sum = 0;
  REP(i, N) {
      int t;
      cin >> t;
      S[i] = t;
      sum += t;
      maxm = max(maxm, t);
      minm = min(minm, t);
  }

  if(maxm == minm) {
      cout << "-1" << endl;
  } else {
      double D = maxm - minm;
      double E = sum / N;
      double p = B / D;
      double q = A - ((E * B) / D);
      cout << p << " " << q << endl;
  }

  return 0;
}
