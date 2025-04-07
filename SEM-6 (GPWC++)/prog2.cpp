// using public class jan 22
#include<iostream>
using namespace std;

class fruits{
public:
string name;
string color;
float price;
void display(){
cout<<"Mangoes are rich in fibre \n";
}
};
/*
int main(){
fruits f1;
f1.name="Mango";
f1.color="Yellow";
f1.price=200;
cout<<"Detail of mango:\n";
cout<<"Name: "<<f1.name<<"\n"<<"Colour: "<<f1.color<<"\n"<<"Price: "<<f1.price<<"\n";
return 0;

}
*/
int main(){
fruits f1;
cout<<"Enter the name colour and price of fruits: \n";
cin>>f1.name>>f1.color>>f1.price;
cout<<"Detail of mango:\n";
f1.display();
cout<<"Name: "<<f1.name<<"\n"<<"Colour: "<<f1.color<<"\n"<<"Price: "<<f1.price<<"\n";
return 0;
}
