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

int main(){
	cin.tie(0);
	ios::sync_with_stdio(false);
	cout.precision(16);
	
	int n, m;
	cin >> n >> m;
	vector< vector<int> > languages(n);
	
	REP(i, n) {
		int k;
		cin >> k;
		vector<int> language(k);
		REP(j, k) {
			cin >> language[j];
		}
		languages[i] = language;
	}

	set<int> languageStack;
	REP(i, languages[0].size()) {
		languageStack.insert(languages[0][i]);
	}
	languages.erase(languages.begin());
	while(!languageStack.empty() && !languages.empty()) {
		auto t = languageStack.begin();
		int targetLanguage = *t;
		languageStack.erase(targetLanguage);
		vector<int> idxs;
		int cnt = 0;
		for(vector<int> language : languages) {
			auto idx = find(language.begin(), language.end(), targetLanguage);
			if(idx != language.end()) {
				REP(i, language.size()) {
					languageStack.insert(language[i]);
				}
				idxs.push_back(cnt);
			}
			cnt++;
		}

		while(!idxs.empty()) {
			int t = idxs.back();
			idxs.pop_back();
			languages.erase(languages.begin() + t);
		}
	}

#if DEBUG
	cout << "** RESULT **" << endl; // debug
#endif
    if(languages.empty()) {
		cout << "YES" << endl;
	} else {
		cout << "NO" << endl;
	}

	return 0;
}
