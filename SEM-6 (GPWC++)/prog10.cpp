//write a program to convert a lower case string to upper case without using any inbuilt function
#include <iostream>
using namespace std;

int main() {
    string input;
    cout << "Enter a string: ";
    cin>>input; 
    int length=input.length();
    for (int i = 0; i < length; i++) {
    
    input[i]=input[i]-32;
 }
 cout<<input<<endl;
}
