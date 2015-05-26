#include <stdio.h>
#include <stdlib.h>

int main(void) {
	int N = 0;
	int arr[4] = {0, 0, 0, 0};
	int i, t;
	int max = 0;
	int min = 99999999;	


	scanf("%d", &N);
	{
		char str[N];
		scanf("%s", str);
		for(i = 0; i < N; i++) {
			arr[str[i] - (int)('1')] += 1;
		}
	}

	for(i = 0; i < 4; i++) {
		if(max < arr[i]) {
			max = arr[i];
		}
		if(min > arr[i]) {
			min = arr[i];
		}
	}

	printf("%d %d\n", max, min);

	return 0;
}	
