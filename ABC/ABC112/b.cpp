#include<iostream>
#include<algorithm>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    
    int ans = 8910016;
    for(int i = 0; i < n; i++) {
        int c, t;
        cin >> c >> t;
        if(m >= t) {
            ans = min(ans, c);
        }
    }

    cout << (ans <= 1000 ? to_string(ans) : "TLE") << endl;
    return 0;
}
