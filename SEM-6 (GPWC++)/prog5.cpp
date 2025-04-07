//Enumeration jan 24
#include<iostream>
using namespace std;

enum shape{circle,square,rectangle,triangle};

int main(){
int code;
cout<<"Enter the shape code:";
cin>>code;
switch(code){
case circle:
cout<<"This is a circle\n";
break;
case square:
cout<<"This is a square\n";
break;
case rectangle:
cout<<"This is a rectangle\n";
break;
case triangle:
cout<<"This is a triangle\n";
break;
default:
cout<<"Not in shape list\n";
}
return 0;

}


/*
int main(){

//colour background=blue;
shape background=(shape)7;
cout<<"Background"<<background<<endl;

return 0;
}*/
