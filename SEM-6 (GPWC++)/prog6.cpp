///////////////jan 24?/////////////

#include<iostream>
using namespace std;
/*
void fun(int &x){
x=x+10;
}
*/
void swap(int &x, int &y){
x=x+y;
y=x-y;
x=x-y;
}
int main(){
//////////swap 2 numbers///////////////////
int a=10;
int b=20;
swap(a,b);
cout<<"A"<<a<<endl<<"B"<<b<<endl;
return 0;

}
/*
int total=10;
int &sum=total;
sum+=total;
cout<<"Total: "<<total<<endl<<"Sum: "<<sum<<endl;
int m=10;
fun(m);
cout<<"M"<<m<<endl;
return 0;
*/
