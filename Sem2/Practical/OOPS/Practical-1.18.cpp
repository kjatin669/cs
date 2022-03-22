//Write a program to print the sum of digits od a number using while loop:-

#include<iostream>
using namespace std;
int main(){
	int num,sum=0,i,a;
	cout<<"Enter any number";
	cin>>num;
	a=num;
	while(num>0){
		i=num%10; 
		sum=sum+i;
		num=num/10; 
	}
	cout<<"Sum of digits of "<<a<<" is "<<sum;
}

