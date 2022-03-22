#include<iostream>
using namespace std;

class Main{
	int n, nn;
	void getVal(){
		cout<<"Enter the Number: ";
		cin>>n;
		nn=n;
	}
	public:
		int factorial(){
			getVal();
			int fact = 1;
			while(n>0){
				fact = fact*n;
				n--;
			}
			return fact;
		}
		int reverse(){
			getVal();
			int reverse = 0, rem;
			while(n>0){
				rem = n%10;
				reverse = reverse*10+rem;
				n = n/10;
			}
			return reverse;			
		}
		int isPalindrome(){
			int result;
			result = reverse();
			if(n==result){
				return 1;
			}
			else{
				return 0;
			}
		}
		int isArmstrong(){
			getVal();
			int nn, remainder, result=0;
			nn = n;
			while(nn>0){
				remainder = nn%10;
				result = result+(remainder*remainder*remainder);
				nn = nn/10;
			}
			if(result == n){
				return 1;
			}
			else{
				return 0;
			}
		}
};

int main(){
	Main m;
	cout<<"Factorial\n";
	cout<<m.factorial()<<endl;
	
	cout<<"-----------------------"<<endl;
	cout<<"Reverse\n";
	cout<<m.reverse()<<endl;
	
	cout<<"-----------------------"<<endl;
	cout<<"Palindrome\n";
	if (m.isPalindrome()){
		cout<<"Number is Palindrome"<<endl;
	}
	else{
		cout<<"Number is Not Palindrome"<<endl;
	}
	
	cout<<"-----------------------"<<endl;
	cout<<"Armstong\n";
	if (m.isArmstrong()){
		cout<<"Number is Armstrong"<<endl;
	}
	else{
		cout<<"Number is Not Armstrong"<<endl;
	}
	
}
