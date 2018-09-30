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
template <typename T>
ostream &operator<<(ostream &out, const vector<T> &v)
{
    if (!v.empty())
    {
        out << '[';
        copy(v.begin(), v.end(), ostream_iterator<T>(out, ", "));
        out << "\b\b]";
    }
    return out;
}

/* template end */

int main()
{
    cin.tie(0);
    ios::sync_with_stdio(false);
    cout.precision(16);

    int n, m, x, y;
    cin >> n >> m >> x >> y;
    vector<int> xs(n + 1);
    vector<int> ys(m + 1);
    for (int i = 0; i < n; i++)
    {
        cin >> xs[i];
    }
    xs[n] = x;
    for (int i = 0; i < m; i++)
    {
        cin >> ys[i];
    }
    ys[m] = y;
    int mx = *max_element(xs.begin(), xs.end());
    int my = *min_element(ys.begin(), ys.end());
#if DEBUG
    cout
        << "** RESULT **" << endl; // debug
#endif
    cout << ((mx < my) ? "No War" : "War") << endl;

    return 0;
}
