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

bool li[100005];

int main(){
  cin.tie(0);
  ios::sync_with_stdio(false);
  cout.precision(16);

  int N;
  cin >> N;

  if(N > 100001) {
      cout << "-1" << endl;
      return -1;
  }

  REP(i, N) {
      int counter = 0;
      int S, C;
      cin >> S >> C;
      while(C > counter) {
          if(!li[S]) {
              counter++;
              li[S] = true;
          } else {
              while(li[S]) S++;
          }
      }

      cout << S << endl;
  }

  return 0;

}
