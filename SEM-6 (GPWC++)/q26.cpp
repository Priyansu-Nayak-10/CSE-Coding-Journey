#include<iostream>
using namespace std;
class A{
public:
int val;
A(int x){
val=x;
}
A(){
cout<<"Constructor"<<endl;
}
};
int main(){
A c;
A a(10);
cout<<a.val;
return 0;
}
