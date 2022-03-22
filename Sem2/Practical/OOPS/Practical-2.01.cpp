#include<iostream>
using namespace std;

class Employee{
	char empName[20];
	int empAge, empBasicSal;
	void getInfo(){
		cout<<"Enter Your Name: ";
		cin.getline(empName, 20);
		cout<<"Enter Your Age: ";
		cin>>empAge;
		cout<<"Enter Basic Salary: ";
		cin>>empBasicSal;
	}
	public:
		void displayInfo(){
			getInfo();
			cout<<"Employee Name: "<<empName<<endl;
			cout<<"Employee Age: "<<empAge<<endl;
			cout<<"Employee Basic Salary: "<<empBasicSal<<endl;
		}
};

int main(){
	Employee e;
	e.displayInfo();
}
