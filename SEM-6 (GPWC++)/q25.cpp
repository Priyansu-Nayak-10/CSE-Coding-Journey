#include<iostream>
using namespace std;
class sample
{
public:
 int a;
 void indata(int x);
 void display();
friend sample update(sample obj);
};
void sample::indata(int x)
{
a=x;
}
void sample::display(){
cout<<"Value of a="<<a<<endl;
}
sample update(sample obj){
sample obj1;
obj.a=obj.a+10;
return(obj1);
}
int main(){
sample t1,t2;
t1.indata(10);
cout<<"Before update"<<endl;
t1.display();
t2=update(t1);
cout<<"After update"<<endl;
t2.display();
return 0;
}
