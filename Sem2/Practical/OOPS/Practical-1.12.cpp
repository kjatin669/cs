#include<iostream>
using namespace std;
int main(){
	char a;
	cout<<"Enter your grade: ";
	cin>>a;
	a=toupper(a);
	switch(a){
		case 'O':
			cout<<"Outstanding";
			break;
		case 'A':
			cout<<"Excellent";
			break;
		case 'B':
			cout<<"Good";
			break;
		case 'C':
			cout<<"Average";
			break;
		case 'D':
			cout<<"Below Average";
			break;
		case 'F':
			cout<<"Fail";
			break;
		default:
			cout<<"No such grade";
	}
}

