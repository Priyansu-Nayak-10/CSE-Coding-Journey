#include<stdio.h>
int main(void)
{
	FILE *inp;
	FILE *outp;
	double item;
	int status;
	inp = fopen("x.txt","r");
	outp = fopen("y.txt","w");
	status =fscanf(inp, "%lf", &item);
	while(status==1){
	fprintf(outp, "%.2f\n", item);
	status = fscanf(inp, "%lf", &item);
	printf("printing input status %d\n", status);
	}
	fclose(inp);
	fclose(outp);
	return 0;
}
