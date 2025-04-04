#include <stdio.h>
struct planet{
	char name[10];
	float rotate;
	int moon;
	double diameter;
};
int main(){
	struct planet p1={"Mars",85.4,2,923.4};
	struct planet p2;
	printf("Enter the planet name, rotation time, no.of moon, diameter:\n");
	for(int i = 0; i<10; i++){
		scanf("%c", &p1.name[i]);
	}
	scanf(" %f", &p1.rotate);
	scanf(" %d", &p1.moon);
	scanf(" %lf", &p1.diameter);
	printf("The planet name:");
	for(int i = 0; i<10; i++){
		printf("%c\n",p1.name[i]);
	}
	printf("The planet rotation time: %f No.of moon: %d Diameter: %lf\n",p2.rotate,p2.moon,p2.diameter);
	
	return (strcmp(p1.name,p2.name)==0 &&
	p1.rotate==p2.rotate && p1.moon==p2.moon && p1.diameter==p2.diameter);
}

