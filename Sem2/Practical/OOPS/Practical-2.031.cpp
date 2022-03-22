#include<iostream>
using namespace std;

class Demo{
	int n,nn;
	void readNo(){
		cout<<"\nEnter a number: ";
		cin>>n;
	}
	public:
		int factorial(){
			readNo();
			int f=1;
			while(n>0){
 				f=f*n;
 				n--;
 			}
 		return f;
		}
 		int reverse(){
 			readNo();
 			int d,num=0;
 			nn=n;
 			while(n>0){
 				d=n%10;
 				num=num*10+d;
 				n=n/10;
 			}
 			return num;
 		}
 		int isPalindrome(){
 			int revnum=reverse();
 			if(nn==revnum){
 				return 1;
			}
 			else{
 				return 0;
		 	}
		}
 		int isArmstrong(){
 			readNo();
 			int nn=n,sum=0,d;
 			while(n>0){
 				d=n%10;
 				sum=sum+(d*d*d);
 				n=n/10;
 			}
 			if(nn==sum){
 				return 1;
			}			
			else{
				return 0;
			}
		}
};


int main(){
	Demo d;
	cout<<"Factorial";
	cout<<d.factorial()<<endl;
	
	cout<<"-----------------------"<<endl;
	cout<<"Reverse";
	cout<<d.reverse()<<endl;
	
	cout<<"-----------------------"<<endl;
	cout<<"Palindrome";
	if (d.isPalindrome()){
		cout<<"Number is Palindrome"<<endl;
	}
	else{
		cout<<"Number is Not Palindrome"<<endl;
	}
	
	cout<<"-----------------------"<<endl;
	cout<<"Armstong";
	if (d.isArmstrong()){
		cout<<"Number is Armstrong"<<endl;
	}
	else{
		cout<<"Number is Not Armstrong"<<endl;
	}
	
}
