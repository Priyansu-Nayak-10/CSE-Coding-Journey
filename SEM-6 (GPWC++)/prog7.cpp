//Dynamially allocating memory for a varianle jan24
#include<iostream>
using namespace std;

int main(){
int *p;
p=new int;
*p=10;
cout<<"value: "<<*p<<"Address: "<<p<<endl;
delete p;
cout<<"value: "<<*p<<"Address: "<<p<<endl;
//dynamically allocating memory of an array
int *arr;
int size;
cout<<"Enter the size of the array: \n";
cin>>size;
cout<<"Creating an array of size"<<size<<endl;
arr=new int[size];
cout<<"dynamic memory allocation of memory for array is successful\n";
for(int i=0;i<size;i++){
arr[i]=i*10;
}
cout<<"values stored in allocated memory(before)\n";
for(int i=0;i<size;i++){
cout<<arr[i]<<" ";
}
cout<<"\n";
delete arr;
cout<<"values stored in allocated memory(after)\n";
for(int i=0;i<size;i++){
cout<<arr[i]<<" ";
}
cout<<"\n";

return 0;
}
