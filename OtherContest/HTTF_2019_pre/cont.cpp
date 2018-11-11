#include <cmath>
#include <cstdio>
#include <iostream>
#include <queue>
#include <vector>

#include <algorithm>
#include <chrono>
#include <functional>
#include <iterator>
#include <map>
#include <random>
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
/* times lib */
chrono::system_clock::time_point time_start, time_end;
double time_limit = 2500;
void set_start() { time_start = chrono::system_clock::now(); }
bool is_over_limit() {
  time_end = chrono::system_clock::now();
  double diff_time = static_cast<double>(
      chrono::duration_cast<chrono::microseconds>(time_end - time_start)
          .count() /
      1000.0);
  return diff_time > time_limit;
}
/* times lib end */

int move_sx[4] = {0, 1, 0, -1};
int move_sy[4] = {1, 0, -1, 0};
int n, m, l;

int fix_position(int x) {
  int t = x;
  if (t >= m) {
    t = m - 1;
  }
  if (t < 0) {
    t = 0;
  }
  return t;
}

int calc_turn(vector<string> s, vector<string> tans) {
  int point = 0;

  int last_point[m][m];
  for (int i = 0; i < m; i++) {
    for (int j = 0; j < m; j++) {
      last_point[i][j] = 0;
    }
  }

  for (int i = 0; i < n; i++) {
    int x = m / 2, y = m / 2;
    int robo_mode = 0;

    for (int j = 0; j < l; j++) {
      char cmd = s[i][j];
      char panel = tans[y][x];
      int counter = 1;
      if (panel == 'D') {
        counter = 2;
      }
      if (panel == 'T') {
        counter = 3;
      }
      if (cmd == 'S') {
        int tx = x, ty = y;
        int nx = x + move_sx[robo_mode] * counter;
        int ny = y + move_sy[robo_mode] * counter;
        nx = fix_position(nx);
        ny = fix_position(ny);
        if (counter == 1) {
          if (tans[ny][nx] == '#') {
            x = tx, y = ty;
          } else {
            x = nx, y = ny;
          }
        } else if (counter == 2) {
          int dx = move_sx[robo_mode] * (counter - 1);
          int dy = move_sy[robo_mode] * (counter - 1);
          dx = fix_position(dx);
          dy = fix_position(dy);
          if (tans[ny][nx] == '#' || tans[dy][dx] == '#') {
            x = tx, y = ty;
          } else {
            x = nx, y = ny;
          }
        } else if (counter == 3) {
          int dx = move_sx[robo_mode] * (counter - 1);
          int dy = move_sy[robo_mode] * (counter - 1);
          int dx2 = move_sx[robo_mode] * (counter - 2);
          int dy2 = move_sy[robo_mode] * (counter - 2);
          dx = fix_position(dx);
          dy = fix_position(dy);
          dx2 = fix_position(dx2);
          dy2 = fix_position(dy2);
          if (tans[ny][nx] == '#' || tans[dy][dx] == '#' ||
              tans[dy2][dx2] == '#') {
            x = tx, y = ty;
          } else {
            x = nx, y = ny;
          }
        }
      } else if (cmd == 'R') {

        if (panel == 'L') {
          robo_mode = (4 + robo_mode - 1 * counter) % 4;
        } else {
          robo_mode = (robo_mode + 1 * counter) % 4;
        }
      } else if (cmd == 'L') {
        if (panel == 'R') {
          robo_mode = (robo_mode + 1 * counter) % 4;
        } else {
          robo_mode = (4 + robo_mode - 1 * counter) % 4;
        }
      } else {
        cerr << "illigal command: " << cmd << endl;
      }
    }
    last_point[y][x]++;
  }

  for (int i = 0; i < m; i++) {
    for (int j = 0; j < m; j++) {
      if (last_point[i][j] == 1) {
        point += 10;
      }
      if (last_point[i][j] == 2) {
        point += 3;
      }
      if (last_point[i][j] == 3) {
        point += 1;
      }
    }
  }

  return point;
}

int main() {
  cin.tie(0);
  ios::sync_with_stdio(false);
  cout.precision(16);

  cin >> n >> m >> l;
  vector<string> s(n);
  vector<string> ans(m);
  string header_line(m, '#');
  string middle_elem_str(m - 2, '.');
  string middle_line = "#" + middle_elem_str + "#";
  for (int i = 0; i < n; i++) {
    cin >> s[i];
  }
  for (int i = 0; i < m; i++) {
    if (i == 0 || i == m - 1) {
      ans[i] = header_line;
    } else {
      ans[i] = middle_line;
    }
  }

  vector<string> init_table = ans;
  vector<string> tans = init_table;
  int cnt = 0;
  int limit = 10;
  random_device rnd;
  mt19937 mt(rnd());
  uniform_int_distribution<> get_rand(0, 10000);

  set_start();
  // init score
  int max_score = calc_turn(s, tans);
  while (true) {
    // change tans table
    for (int i = 1; i < m - 1; i++) {
      for (int j = 1; j < m - 1; j++) {
        char panel = '.';
        int r = get_rand(mt);
        if (r <= 3000) {
          panel = 'R';
        } else if (r <= 6000) {
          panel = 'L';
        } else if (r <= 6350) {
          panel = '#';
        }
        tans[i][j] = panel;
      }
    }
    int score = calc_turn(s, tans);
    if (score > max_score) {
      max_score = score;
      ans = tans;
    }
    // cerr << "max: " << max_score << ", score: " << score << endl;
    if (cnt % limit == (limit - 1)) {
      if (is_over_limit()) {
        break;
      }
      cnt = 0;
    }
    cnt++;
    tans = init_table;
  }
#if DEBUG
  cout << "** RESULT **" << endl; // debug
#endif
  for (string elem : ans) {
    cout << elem << endl;
  }
  return 0;
}
