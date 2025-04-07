#include<iostream>
#include<string>

using namespace std;

class binary{
string s;
public:
void read(void){
cout<<"Enter a binary number: \n";
cin>>s;
}
void check(void){
for(int i=0;i<s.length();i++){
if(s.at(i)!='0' && s.at(i)!='1'){
cout<<"Incorrect binary format---The program will quit"<<endl;
cin.get();
exit(0);
}
}
}
void complement(void){
check();
for(int i=0;i<s.length();i++){
if(s.at(i)=='0'){
s.at(i)='1';
}
else
s.at(i)='0';
}
}
void displayones(void)
{
complement();
cout<<"The ones complement of the binary number is "<<s<<endl;
}
};
int main()
{
binary b;
b.read();
b.displayones();

return 0;
}






