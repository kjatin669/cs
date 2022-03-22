#include<iostream>
using namespace std;

class Student{
	int stuRollNo;
	char stuName[20], stuClass[5], stuAddress[50];
	
	void getData(){
		cout<<"Enter Name: ";
		cin.getline(stuName, 20);
		cout<<"Enter Roll No: ";
		cin>>stuRollNo;
		cout<<"Enter Class: ";
		cin.ignore();
		cin.getline(stuClass, 5);
		cout<<"Enter Address: ";
		cin.getline(stuAddress, 50);
	}
	public:
		void displayData(){
			getData();
			cout<<"Name: "<<stuName<<endl;
			cout<<"Roll No: "<<stuRollNo<<endl;
			cout<<"Class: "<<stuClass<<endl;
			cout<<"Address: "<<stuAddress<<endl;
		}
};

int main(){
	Student s;
	s.displayData();
}
