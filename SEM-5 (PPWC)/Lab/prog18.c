#include<stdio.h>
void inc(void);
void dec(void);
int i;
int main(void){
	printf("\ni=%d",i);
	inc();
	inc();
	dec();
	dec();
	return 0;
	}
void inc(void){
i=i+1;
printf("\non incrementing i=%d",i);
}
void dec(void){
i=i-1;
printf("\non decrementing i=%d",i);
}

