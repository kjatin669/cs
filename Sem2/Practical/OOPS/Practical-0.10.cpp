// Practical 0.10

// Topic : Percentage

#include <iostream>
using namespace std;

int main(){
    int bs;
    float da, hra, ma, pf, gross, net;

    cout<<"Enter the Basic Salary: ";
    cin>>bs;
    
    da = (30*bs)/100;
    hra = (70*bs)/100;
    ma = (10*bs)/100;
    pf = (5*bs)/100;
    gross = bs+da+hra+pf;
    net = gross-pf;

    cout<<"DA: "<<da;
    cout<<"HRA: "<<hra;
    cout<<"MA: "<<ma;
    cout<<"PF: "<<pf;
    cout<<"GROSS: "<<gross;
    cout<<"NET: "<<net;
    
    return 0;
}