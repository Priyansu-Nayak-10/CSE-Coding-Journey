//Read and display matrix through function and diplay matrix by taking row or colunm default 
#include<iostream>
using namespace std;

void read(int matrix[][5], int m, int n){
for(int i=0;i<m;i++){
for(int j=0;j<n;j++){
cout<<"Enter element for "<<i+1<<j+1<<" :";
cin>>matrix[i][j];
}
}
}
void display(int matrix[][5], int m, int n){
for(int i=0;i<m;i++){
for(int j=0;j<n;j++){
cout<<matrix[i][j];
}
cout<<endl;
}
}
void rdisplay(int matrix[][5], int m, int n){
read(matrix,m,n);
cout<<"Matrix"<<"\n";
display(matrix,m,n);
}

void defaultrow(int matrix[][5], int m, int n=2){
read(matrix,m,n);
cout<<"Default Matrix"<<"\n";
display(matrix,m,n);
}

int main()
{
int matrix[5][5];
int n,m;

cout<<"Enter the number of rows: ";
cin>>m;
cout<<"Enter the number of columns: ";
cin>>n;
rdisplay(matrix,m,n);

defaultrow(matrix,m);


return 0;

}

