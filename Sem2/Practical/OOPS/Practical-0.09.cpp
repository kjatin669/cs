// Practical 0.9

// Topic : Sum Average and Grade

#include <iostream>
using namespace std;

int main(){
    int m1, m2, m3, sum;
    float average;

    cout<<"Enter the Marks of First Subject: ";
    cin>>m1;
    cout<<"Enter the Marks of Second Subject: ";
    cin>>m2;
    cout<<"Enter the Marks of Third Subject: ";
    cin>>m3;

    sum = m1+m2+m3;
    average = sum/3;
	cout<<"Sum of All Marks is "<<sum<<endl;
	cout<<"Average: "<<average<<endl;
    if (average>=75 && average<100){
        cout<<"Distinction";
    }
    else if (average>=60 && average<75){
        cout<<"First Class";
    }
    else if (average>=50 && average<60){
        cout<<"Second Class";
    }
    else if (average>=40 && average<50){
        cout<<"Third Class";
    }
    else{
        cout<<"Fail";
    }
}
