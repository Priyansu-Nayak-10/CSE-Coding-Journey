// using private class jan 22
#include<iostream>
using namespace std;

class person{
char name[20];
int age;

public:
void getdata(void);
void display(void);
};
void person :: getdata(void){
cout<<"Enter Name and age \n";
cin>>name>>age;
}
void person :: display(void){
cout<<"Name: "<<name<<"\n";
cout<<"Age: "<<age<<"\n";
}
int main(){
person p1;
p1.getdata();
p1.display();
}
