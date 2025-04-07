/*
#include<iostream>
int a=10;
int &func(){
return (a);
}
using namespace std;
int main(){
func()=20;
cout<<"Value of a is  :"<<a<<endl;
return 0;
}
*/

#include<iostream>
using namespace std;

float Addition(float a,float b, float r=0.5){
float sum=a+b+r;
cout<<"Sum"<<sum<<endl;
return sum;
} 

int main(){
Addition(1.5,2.5);
return 0;

}
