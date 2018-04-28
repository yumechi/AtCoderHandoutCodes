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
#include <iterator>

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

/** FOR VECTOR DEBUG */
template <typename T>
ostream& operator<< (ostream& out, const vector<T>& v) {
  if ( !v.empty() ) {
    out << '[';
    copy (v.begin(), v.end(), ostream_iterator<T>(out, ", "));
    out << "\b\b]";
  }
  return out;
}


int main(){
	cin.tie(0);
	ios::sync_with_stdio(false);
	cout.precision(16);

    int n;
    cin >> n;
    ll arr[n];
    vector<long long> v(n + 1);
    v[0] = 0;
    REP(i, n) {
        cin >> arr[i];
        v[i + 1] = v[i] + arr[i];
    }

    sort(v.begin(), v.end());
    ll ans = 0;
    for(int i = 0; i < n; i++) {
        ans += distance(v.begin() + i, upper_bound(v.begin() + i, v.end(), v[i])) - 1;
#if DEBUG
        cout << "** DEBUG **" << endl; // debug
        cout << "# ans : " << ans << endl;
        cout << "# diff : " << distance(v.begin() + i, upper_bound(v.begin() + i, v.end(), v[i])) - 1 << endl;
        cout << v << endl;
#endif
   }

#if DEBUG
	cout << "** RESULT **" << endl; // debug
#endif
    cout << ans << endl;
	
	return 0;
}
