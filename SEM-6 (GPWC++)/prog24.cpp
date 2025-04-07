#include<iostream>
const int size=5;
using namespace std;

class array {
int a[size];
public:
void setval();
void display();
int sum();
int largest();
};

void array::setval() {
for(int i=0; i<size; i++) {
cin >> a[i];
}
}

void array::display() {
for(int i=0; i<size; i++) {
cout << a[i] << " ";
}
cout << endl;
}

int array::sum() {
int sum=0;
for(int i=0; i<size; i++) {
sum += a[i];
}
return sum;
}

int array::largest() {
int max = a[0];
for(int i=0; i<size; i++) {
if(a[i] > max) {
max = a[i];
}
}
return max;
}

int main() {
array a;
int choice;

do {
cout << "Menu:\n";
cout << "1.Enter elements\n";
cout << "2.Display elements\n";
cout << "3.Calculate sum\n";
cout << "4.Find largest element\n";
cout << "5.Exit\n";
cout << "Enter your choice: ";
cin >> choice;

        switch(choice) {
            case 1:
                cout << "Enter elements: ";
                a.setval();
                break;
            case 2:
                cout << "Elements: ";
                a.display();
                break;
            case 3:
                cout << "Sum: " << a.sum() << endl;
                break;
            case 4:
                cout << "Largest: " << a.largest() << endl;
                break;
            case 5:
                cout << "Exiting program." << endl;
                break;
            default:
                cout << "Invalid choice." << endl;
        }
    } while(choice != 5);
    return 0;
}
