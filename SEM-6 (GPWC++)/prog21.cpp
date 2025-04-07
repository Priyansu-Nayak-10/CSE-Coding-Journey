#include<iostream>

using namespace std;

class sample{
int m;
void read(void);
public:
void update(void);
void write(void);
};
void sample :: read(){
cout<<"value read: "<<m<<endl;
}
void sample::update(void){
m=21;
read();
}
void sample::write(void){
cout<<"Value written: "<<m<<endl;
}
int main(){
sample s1;
s1.update();
s1.write();
return 0;
}
