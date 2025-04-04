#include <stdio.h>
struct planet{
	char name[10];
	float rotat_time;
	int moon;
	double diameter;
};

int main(){
	struct planet p1 = {"Earth",61, 1,98.8}, p2;
	printf("Enter the planet name, rotation time, no.of moon, diameter:\n");
	for(int i = 0; i<10; i++){
		scanf("%c", &p2.name[i]);
	}
	scanf(" %f", &p2.rotat_time);
	scanf(" %d", &p2.moon);
	scanf(" %lf", &p2.diameter);
	printf("The planet name:");
	for(int i = 0; i<10; i++){
		printf("%c\n",p2.name[i]);
	}
	printf("The planet rotation time: %f No.of moon: %d Diameter: %lf\n",p2.rotat_time,p2.moon,p2.diameter);
}
