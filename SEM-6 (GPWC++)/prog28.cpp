#include<iostream>

using namespace std;

class space{
    int x,y,z;
    public:
    void getdata(int a, int b, int c);
    void display();
    void operator -();
};
void space::getdata(int a, int b, int c){
    x=a;
    y=b;
    z=c;
}
void space::display(){
    cout<<"X="<<x<<" ";
    cout<<"Y="<<y<<" ";
    cout<<"Z="<<z<<" ";
}
void space::operator -(){
    x=-x;
    y=-y;
    z=-z;
}
int main(){
space s;
s.getdata(10,-20,30);
cout<<"s:";
s.display();
-s;
cout<<"\ns after :\n";
s.display();
return 0;

}