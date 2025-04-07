//HYBRID INHERITANCE
#include <iostream>
using namespace std;

class A {
public:
    void displayA() {
        cout << "Class A is Base class" << endl;
    }
};

class B : public A {
public:
    void displayB() {
        cout << "Class B derived from class A" << endl;
    }
};

class C {
public:
    void displayC() {
        cout << "Class C is another base class " << endl;
    }
};

class D : public B, public C {
public:
    void displayD() {
        cout << "Class D derived from class B and C" << endl;
    }
};

int main() {
    D obj;
    obj.displayA();
    obj.displayB();
    obj.displayC();
    obj.displayD();

    return 0;
}
