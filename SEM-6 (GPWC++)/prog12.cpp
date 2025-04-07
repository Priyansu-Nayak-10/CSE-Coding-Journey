
//Temperature conversion jan 29 
/*
#include<iostream>
using namespace std;

class temp{
public:
float cel;
float fah;
void funconv();
};
void temp::funconv(){
cout<<"Enter the celcius : ";
cin>>cel;
fah=cel*(9/5)+32;
cout<<"Temperature in Farenheit= "<<fah<<endl;
}
int main(){
temp t1;
t1.funconv();
return 0;
}
*/

#include<iostream>

using namespace std;
int &max(int &x,int &y){
if(x>y)
return x;
else
return y;
}
int main(){
int a,b;
cin>>a>>b;
max(a,b)-=1;
cout<<"Maximum is :"<<max(a,b)<<endl;
return 0;
}




















