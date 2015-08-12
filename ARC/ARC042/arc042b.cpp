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

int main(){
    cin.tie(0);
    ios::sync_with_stdio(false);
    cout.precision(16);

    int x, y, n;
    cin >> x >> y >> n;

    double res = 300.0;

    int tx[n], ty[n];
    REP(i, n) {
        cin >> tx[i];
        cin >> ty[i];
    }

    REP(i, n) {
        int tx1, ty1, tx2, ty2;
        int cx, cy;

        tx1 = tx[i]; ty1 = ty[i];
        if(i < n-1) {
            tx2 = tx[i+1]; ty2 = ty[i+1];
        } else {
            tx2 = tx[0]; ty2 = ty[0];
        }
        cx = x; cy = y;

        // y - y1 = ((y2 - y1) / (x2 - x1)) * (x - x1)
        // (y1 - y2) x + (x2 - x1) y - y1 * (x2 - x1) + x1 * (y2 - y1) = 0
        // (y1 - y2) x + (x2 - x1) y - y1 * x2 + x1 * y2= 0
        double a = ty1 - ty2;
        double b = tx2 - tx1;
        double c = -(tx2 * ty1) + tx1 * ty2;
        double cres = fabs(a * cx + b * cy + c) / sqrt(a * a + b * b);

        res = min(res, cres);
    }

    cout << res << endl;
    return 0;
}
