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
#define MOD 1000000007

ll add_m(ll a, ll b) { return (a%MOD + b%MOD) % MOD; }
ll sub_m(ll a, ll b) { return (a%MOD - b%MOD + MOD) % MOD; }
ll mul_m(ll a, ll b) { return (a%MOD * b%MOD) % MOD; }

ll calcmod(ll a, int m) {
    ll res = 1;
    while(m > 0) {
        if(m % 2 == 1) {
            res = (a * res) % MOD;
        }
        a = (a * a) % MOD;
        m >>= 1;
    }

    return res % MOD;
}

int main(){
  cin.tie(0);
  ios::sync_with_stdio(false);
  cout.precision(16);

  ll a, b, c;
  cin >> a >> b >> c;

  ll de = calcmod(sub_m(add_m(a*c, a*b), b*c), MOD - 2) % MOD;
  ll rc = mul_m(sub_m(b*c, b*a), de);
  ll rr = mul_m(sub_m(c*b, c*a), de);

  cout << rr << " " << rc << endl;

  return 0;
}
