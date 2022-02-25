// Practical 0.4

// Topic : Minimum of 3 Number

#include <iostream>
using namespace std;

int main(){
    int a, b, c;
    cout<<"Enter the First Number: ";
    cin>>a;
    cout<<"Enter the Second Number: ";
    cin>>b;
    cout<<"Enter the Third Number: ";
    cin>>c;

    if (a<b && a<c){
        cout<<"Minimim: "<<a;
    }
    else if (b<a && b<c){
        cout<<"Minimum: "<<b;
    }
    else{
        cout<<"Minimum: "<<c;
    }
}