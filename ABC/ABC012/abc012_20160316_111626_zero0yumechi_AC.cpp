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
#define DEBUG(x) cout<<#x<<": "<<x<<endl
#define DDEBUG(x,y) cout<<#x<<": "<<x<<", "<<#y<<": "<<y<<endl
#define ll long long
#define ull unsigned long long
#define MOD 1000000007
 
// refer:
// http://www.deqnotes.net/acmicpc/dijkstra/
 
struct Node {
    // このノードから伸びるエッジの情報
    vector<int> edges_to;    // 各エッジの接続先のノード番号
    vector<int> edges_cost;  // 各エッジのコスト
 
    // ダイクストラ法のためのデータ
    bool done;  // 確定ノードか否か
    int cost;   // このノードへの現時点で判明している最小コスト
 
	bool operator> (const Node  &) const;
	bool operator< (const Node  &) const;
};
 
bool Node::operator> (const Node  &n) const {return cost >  n.cost;}
bool Node::operator< (const Node  &n) const {return cost <  n.cost;}
 
typedef priority_queue <Node, vector<Node>, greater<Node> > dijk_p_que;
 
int main(){
	cin.tie(0);
	ios::sync_with_stdio(false);
	cout.precision(16);
 
	int n, m;
	cin >> n >> m;
 
	vector<Node> nodes(n);
	// init
	REP(i, n) {
		nodes[i].done = false;
		nodes[i].cost = -1;
	}
 
	// connect
	REP(i, m) {
		int from, to, cost;
		cin >> from >> to >> cost;
		from--; to--;
		nodes[from].edges_to.pb(to);
		nodes[from].edges_cost.pb(cost);
		nodes[to].edges_to.pb(from);
		nodes[to].edges_cost.pb(cost);
	}
 
	nodes[0].cost = 0;
	int res = INF;
	REP(s, n) {
		nodes[s].cost = 0;
		dijk_p_que p_que;
		p_que.push(nodes[s]);
 
		while(!p_que.empty()) {
			Node donenode = p_que.top();
			p_que.pop();
			// DDEBUG(s, donenode.edges_to.size());
			if(donenode.done) continue;
 
			// 確定フラグを立てる
			donenode.done = true;
			REP(i, donenode.edges_to.size()) {
				int to = donenode.edges_to[i];
				int cost = donenode.edges_cost[i] + donenode.cost;
				if(nodes[to].cost < 0 || cost < nodes[to].cost) {
					nodes[to].cost = cost;
					if(!nodes[to].done) p_que.push(nodes[to]);
				}
			}
		}
 
		int maxcost = 0;
		REP(i, n) {
			if(nodes[i].cost > 0) maxcost = max(maxcost, nodes[i].cost);
			// DDEBUG(i, nodes[i].cost);
			// reset node
			nodes[i].cost = -1;
			nodes[i].done = false;
		}
		res = min(res, maxcost);
	}
 
	// cout << "** RESULT **" << endl; // debug
	cout << res << endl;
}
