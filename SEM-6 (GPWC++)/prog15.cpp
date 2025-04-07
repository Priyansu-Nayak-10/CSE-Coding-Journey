//Function overloading
#include<iostream>
using namespace std;

int mul(int a, int b)
{
return a*b;
}

int mul(float a, int b)
{
return a*b;
}
float mul(float a, float b)
{
return a*b;
}
int mul(int a, int b, float c)
{
return a*b*c;
}
int main(){
cout<<mul(2,3)<<endl;
cout<<mul(2,3,4.5)<<endl;
return 0;
}


