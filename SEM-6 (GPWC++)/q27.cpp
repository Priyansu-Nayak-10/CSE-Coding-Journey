#include<iostream>
using namespace std;
int count=0;
class test
{
public:
test( )
{
count++;
cout<<"\nConstructor Msg: Object number "<<count<<"created..";
}
~test( ) {
cout<<"\nDestructor Msg: Object number "<<count<<"destroyed..";
count--;
}
};
int main( )
{
cout<<"Inside the main block..";
cout<<"\n\nCreating first objectT1..";
test T1;
{
cout<<"\nInside Block 1..";
cout<<"\nCreating two more objects T2 and T3..";
test T2,T3;
cout<<"\nLeaving Block 1..";
}
cout<<"\nBack inside the main block..";
return 0;
}
