#include <cmath>
#include <cstdio>
#include <iostream>
#include <queue>
#include <vector>

#include <algorithm>
#include <functional>
#include <iterator>
#include <map>
#include <set>
#include <string>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define RFOR(i, a, b) for (int i = (b)-1; i >= (a); i--)
#define REP(i, n) for (int i = 0; i < (n); i++)
#define RREP(i, n) for (int i = (n)-1; i >= 0; i--)
#define INF (1 << 30)
#define ALEN(ARR) (sizeof(ARR) / sizeof((ARR)[0]))
#define MP make_pair
#define mp make_pair
#define pb push_back
#define PB push_back

#if DEBUG
#define _DEBUG(x) cout << #x << ": " << x << endl
#define _DDEBUG(x, y) cout << #x << ": " << x << ", " << #y << ": " << y << endl
#else
#define _DEBUG(x) ;
#define _DDEBUG(x, y) ;
#endif

#define ll long long
#define ull unsigned long long
#define MOD 1000000007

/** FOR VECTOR DEBUG */
template <typename T> ostream &operator<<(ostream &out, const vector<T> &v) {
  if (!v.empty()) {
    out << '[';
    copy(v.begin(), v.end(), ostream_iterator<T>(out, ", "));
    out << "\b\b]";
  }
  return out;
}

/* template end */

int main() {
  cin.tie(0);
  ios::sync_with_stdio(false);
  cout.precision(16);

  ll k, a, b;
  cin >> k >> a >> b;
  if (a >= b) {
    cout << (k + 1) << endl;
    return 0;
  }
  ll d = k / (a + 2);
  vector<ll> v(4);
  v[0] = 1 + b * d + k % (a + 2);
  v[1] = 1 + b * (d - 1) + (a + 2) + k % (a + 2);
  if (k > a) {
    v[2] = 1 + (a - 1) + ((k - a + 1) / 2) * (b - a);
    v[3] = 1 + (a - 1) + ((k - a + 1) / 2 - 1) * (b - a) + 2;
    if ((k - a + 1) % 2 == 1) {
      v[2] += 1;
      v[3] += 1;
    }
  }
  _DEBUG(v);
  ll ans = *max_element(v.begin(), v.end());
#if DEBUG
  cout << "** RESULT **" << endl; // debug
#endif
  cout << ans << endl;

  return 0;
}
