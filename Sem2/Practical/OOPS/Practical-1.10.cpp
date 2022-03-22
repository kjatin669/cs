// Practical 0.10

// Topic : Percentage

#include <iostream>
using namespace std;

int main(){
    int bs;
    float da, hra, ma, pf, gross, net;

    cout<<"Enter basic salary: ";
    cin>>bs;
    
    da = (30*bs)/100;
    hra = (70*bs)/100;
    ma = (10*bs)/100;
    pf = (5*bs)/100;
    gross = bs+da+hra+pf;
    net = gross-pf;

    /*cout<<"DA: "<<da<<endl;
    cout<<"HRA: "<<hra<<endl;
    cout<<"MA: "<<ma<<endl;
    cout<<"PF: "<<pf<<endl;
    cout<<"GROSS: "<<gross<<endl;
    cout<<"NET: "<<net<<endl;*/
	
    cout<<"DA: "<<da<<"\nHRA: "<<hra<<"\nMA: "<<ma<<"\nPF: "<<pf<<"\nGross Salary: "<<gross<<"\nNet Salary: "<<net<<endl;
    
    return 0;
}
