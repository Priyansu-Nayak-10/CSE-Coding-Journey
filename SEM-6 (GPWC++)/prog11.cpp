
//jan 29 
#include<iostream>

using namespace std;

int main(){
string name;
cout<<"Enter the name of the user: ";
cin>>name;
int unit;
cout<<"Enter the units consumed: ";
cin>>unit;
float total_amount;
float charge;
if(unit<=100){
total_amount=unit*60;
}
else if(unit>100 && unit<=300){
total_amount=100*60+(unit-100)*80;
}
else{
total_amount=100*60+200*80+(unit-300)*90;
}
total_amount=total_amount/100;
if(total_amount<50){

total_amount=50;
}
if(total_amount>300){
charge=total_amount+total_amount*0.15;
}
cout<<"Total Amount: "<<total_amount<<endl;
return 0;
}
