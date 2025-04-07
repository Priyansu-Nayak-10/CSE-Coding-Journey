#include<iostream>
const int size=5;
using namespace std;

class array{
aint a[size];
public:
void setval();
void display();
int sum();
int largest();
};
void array:: setval(){
for(int i=0;i<size;i++){
cin>>a[i];
}
}
void array:: display(){
for(int i=0;i<size;i++){
cout<<a[i]<<" ";
}
cout<<endl;
}
int array::sum(){
int sum=0;
for(int i=0;i<size;i++){
sum+=a[i];
}
return sum;
}
int array:: largest(){
int max=a[0];
for(int i=0;i<size;i++){
if(a[i]>max){
max=a[i];
}
}
return max;
}
int main(){
array a;
cout<<"Enter elements: ";
a.setval();
cout<<"elements: ";
a.display();
cout<<"sum "<<a.sum()<<endl;
cout<<"Largest "<<a.largest()<<endl;
return 0;
}

