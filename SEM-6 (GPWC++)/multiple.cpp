//MULTIPLE INHERITANCE
#include<iostream>

using namespace std;

class X{
    protected:
    int x;
    public:
    void get_x(int);
};

class Y{
    protected:
    int y;
    public:
    void get_y(int);
};

void X::get_x(int a){
    x=a;
}

void Y::get_y(int b){
    y=b;
}

class result: public X, public Y{
    public:
    void display(void);
};

void result::display(void){
cout << "X = " << x << "\n";
cout << "Y = " << y << "\n";
cout << "X*Y = " << x*y << "\n";
cout << "X+Y = " << x+y << "\n";

}
int main()
{
result r;
r.get_x(15);
r.get_y(2);
r.display();
return 0;
}