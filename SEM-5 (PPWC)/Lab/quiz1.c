#include<stdio.h>
int main(){
	int bs;
	int hra;
	int da;
	float gross;
	printf("Enter the basic salary: ");
	scanf("%d",&bs);
	if(bs<=10000){
	hra=0.2*bs;
	da=0.8*bs;
	gross=bs+hra+da;
	printf("Basic salary %lf",gross);
	}
	else if(bs>=10001 && bs<=20000){
	hra = 0.25*bs;
	da=0.9*bs;
	gross=bs+hra+da;
	printf("Basic salary %lf",gross);
	}
	else{
	hra = 0.3*bs;
	da=0.95*bs;
	gross=bs+hra+da;
	printf("Basic salary %lf",gross);
	
	}
	return 0;


}
