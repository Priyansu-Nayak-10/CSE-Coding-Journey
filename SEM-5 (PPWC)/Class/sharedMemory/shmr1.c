#include<stdio.h>  
#include<stdlib.h>  
#include<unistd.h>  
#include<sys/shm.h>  
#include<string.h>  
int main()  
{  
int i;
char *str2 = "world";
char *str1, *str3;  
void *shared_memory;  
char buff[100];  
int shmid;  
shmid=shmget((key_t)2345, 1024, 0666);  
printf("Key of shared memory is %d\n",shmid);  
shared_memory=shmat(shmid,NULL,0); //process attached to shared memory segment  
printf("Process attached at %p\n",shared_memory); 
str1 = (char *)shared_memory;
str3 = strcat(str1, str2);
printf("%s", str3);
//printf("Data read from shared memory is : %s\n",(char *)shared_memory);  
} 
