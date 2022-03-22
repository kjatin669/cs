#include<iostream>
using namespace std;
int main(){
	int num;
	int i=1;
	int fact=1;
	cout<<"Enter any number: ";
	cin>>num;
	while(i<=num){
		fact=fact*i;
		i=i+1;
	}
	cout<<"Factorial of "<<num<<" is "<<fact;
}

