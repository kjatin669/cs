// Practical 0.8

// Topic : Positive and Negative

#include <iostream>
using namespace std;

int main(){
    int x;
    cout<<"Enter the Number: ";
    cin>>x;

    if (x==0){
        cout<<"Zero can neither be Positive nor Negative";
    }
    else if(x<0){
        cout<<"Negative";
    }
    else{
        cout<<"Positive";
    }
}