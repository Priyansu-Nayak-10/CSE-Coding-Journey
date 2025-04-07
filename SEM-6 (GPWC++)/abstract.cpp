// Abstract

#include<iostream>

using namespace std;

class Abstract {
    protected:
    int a;
    public:
    virtual void vehicle() = 0;
};
class v1 : public Abstract {
    public:
    void vehicle() {
        cout << "vehicle 1" << endl;
    }
};
int main(){
    v1 obj;
    obj.vehicle();
    return 0;
}