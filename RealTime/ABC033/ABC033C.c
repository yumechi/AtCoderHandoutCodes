#include <stdio.h>

int res = 0, i = 0;
int flag = 0;
char s[100002];
int lastidx = 0;

int main(void) {
	scanf("%s", s);

	for(i = 0; s[i] != '\0'; i++) {
		if(s[i] == '+') {
			int flag = 0;
			for( ; lastidx <= i ; lastidx++) {
				if(s[lastidx] == '0') flag = 1;
			}
			if(flag == 0) res++;
		}
	}

	for( ; lastidx < i ; lastidx++) {
		if(s[lastidx] == '0') break;
	}
	if(lastidx == i) res++;

	printf("%d\n", res);

	return 0;
}