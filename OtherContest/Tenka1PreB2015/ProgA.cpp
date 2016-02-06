#include <iostream>

using namespace std;

int main() {
	long long a0 = 100, a1 = 100, a2 = 200;
	for(int i = 0; i < 17; i++) {
		long long t = a2;
		a2 = a0 + a1 + a2;
		a0 = a1;
		a1 = t;
	}
	
	cout << a2 << endl;
	return 0;
}