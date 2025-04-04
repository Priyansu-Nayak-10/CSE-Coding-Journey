#include<stdio.h>
void main(){
int x[5][2]={
	      {1234, 70},
	      {1234, 80},
	      {1234, 40},
	      {1234, 85},
	      {1234, 60}, 
	      };
int i,j;
for(i=0;i<5; i++){
for(j=0;j<2; j++){
printf("x[%d][%d]=%d and address: %p\n", i, j,x[i][j],&x[i][j]);
}

}

}
