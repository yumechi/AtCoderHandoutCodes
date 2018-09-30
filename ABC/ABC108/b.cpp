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

    int x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;
    int x3, y3, x4, y4;
    x3 = x2 - y2 + y1;
    y3 = y2 + x2 - x1;
    x4 = x1 - y2 + y1;
    y4 = y1 + x2 - x1;
#if DEBUG
    cout << "** RESULT **" << endl; // debug
#endif
    printf("%d %d %d %d\n", x3, y3, x4, y4);

    return 0;
}
