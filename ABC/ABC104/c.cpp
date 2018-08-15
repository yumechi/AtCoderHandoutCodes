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
#define INF 1 << 29
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

    int c, g;
    cin >> c >> g;
    int pc[c], pp[c];
    int ans = 0;
    REP(i, c)
    {
        cin >> pc[i] >> pp[i];
        ans += pc[i];
    }

    for (int j = 0; j < pow(2, c); j++)
    {
        ll tsum = 0;
        ll tans = 0;
        for (int k = 0; k < c; k++)
        {
            if ((j >> k) & 1)
            {
                tsum += ((k + 1) * 100) * pc[k] + pp[k];
                tans += pc[k];
            }
        }
        if (tsum < g)
        {
            continue;
        }

        for (int k = 0; k < c; k++)
        {
            int ttsum = tsum;
            int ttans = tans;
            if ((j >> k) & 1)
            {
                ttsum -= (((k + 1) * 100) * pc[k] + pp[k]);
                ttans -= pc[k];
            }
            for (int l = 0; l <= pc[k]; l++)
            {
                int ts = ttsum + l * ((k + 1) * 100);
                int ta = ttans + l;
                if (l == pc[k])
                {
                    ts += pp[k];
                }
                if (ts >= g)
                {
                    ans = min(ta, ans);
                    break;
                }
            }
        }
    }

#if DEBUG
    cout << "** RESULT **" << endl; // debug
#endif
    cout << ans << endl;

    return 0;
}
