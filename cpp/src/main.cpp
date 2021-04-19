#include <iostream>

#include "header.h"

using namespace std;

class MyClass
{
public:
	MyClass();

private:
	int m_member;
};

int main(int argc, char const *argv[])
{
	int a = CONST;

	cout << "Hello World" << endl;

	MyClass myobj = MyClass();

	return 0;
}
