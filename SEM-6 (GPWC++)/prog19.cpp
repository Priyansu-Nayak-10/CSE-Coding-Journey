#include<iostream>
using namespace std;

class fac{
private:
int f;
public:
void fact(int f){
cout<<"Factorial of a number is : "<<facto(f)<<endl;
}
int facto(int n){
if(n==0||n==1)
return 1;
else
return n*facto(n-1);
}
};
int main(){
int num;
fac f1,f2;
f1.fact(2);
f2.fact(5);
return 0;
}


