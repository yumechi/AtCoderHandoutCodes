#include <stdio.h>
#include <string.h>

int arr[100000];

int calc(int n) {
    int i;
    int res = 0;

    for(i = 0; i < n; i++) {
        int inp = 0;
        scanf("%d", &inp);
        arr[inp-1]++;
    }

    for(i = 0; i < 100000; i++) {
        if(arr[i] > 1) res += arr[i] - 1;
    }

    return res;
}

int main() {
    int n;

    scanf("%d", &n);
    printf("%d\n", calc(n));

    return 0;
}
