#include<iostream>
using namespace std;

class complex{
float real,img;
public:
void getData()
{
cout<<"Enter real number: ";
cin>>real;
cout<<"Enter imaginary number: ";
cin>>img;
}
void showData()
{
cout<< real <<" + i"<< img ;
}
 friend complex sum(complex, complex);
};
complex sum(complex c1, complex c2)
{
complex c3;
c3.real=c1.real+c2.real;
c3.img=c1.img+c2.img;
return c3;
}
int main()
{
complex obj1, obj2, obj3;
cout<<"\nEnter Data for 1st Complex Number \n";
cout<<"---------------------------------"<<endl;
obj1.getData();
cout<<"\nEnter Data for 2nd Complex Number \n";
cout<<"---------------------------------"<<endl;
obj2.getData();

obj3=sum(obj1,obj2);

cout<<"\nComplex Number1: ";
obj1.showData();
cout<<"\nComplex Number2: ";
obj2.showData();
cout<<"\nComplex Number3: ";
obj3.showData();
}

