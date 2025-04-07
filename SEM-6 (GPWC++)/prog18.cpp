#include<iostream>

using namespace std;

class item{
int number;
float cost;
public:
void getdata(int a,float b);
void putdata(){
cout<<number<<" " <<cost<<endl;
}
int z;
};
void item:: getdata(int a, float b){
number =a;
cost=b;
}
int main(){
item x,y;
cout<<"object x:"<<endl;
x.getdata(1,100.8);
x.putdata();
}
