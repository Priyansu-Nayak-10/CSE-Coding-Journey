//Demonstrating namespace jan 24
#include<iostream>
using namespace std;
namespace reply1{
void reply(){
cout<<"Hey welcome\n";
}
};
namespace reply2{
void reply(){
cout<<"HEY WELCOME\n";
}
};
using namespace reply1;
int main(){
/*
reply1::reply();
reply2::reply();
*/
reply();
return 0;
}
