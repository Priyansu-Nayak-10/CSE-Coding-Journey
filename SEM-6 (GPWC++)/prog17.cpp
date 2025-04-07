#include<iostream>
using namespace std;

class example{
int x;
int y;
public:
void getdata(){
cin>>x>>y;
cout<<"x: "<<x<<" y: "<<y<<endl;
}
};

int main(){
example ex;
ex.getdata();
return 0;
}
