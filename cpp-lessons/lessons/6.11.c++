/*	Расставьте скобки в следующих выражениях */

#include <iostream>

void f(int a, int b)
{
	if(a=3) std::cout << "IF1" << std::endl;
	if(a&077==0) std::cout << "IF2" << std::endl;
	a:=b+1;
	std::cout << a << " --- " << b << std::endl;
}

int main()
{
	int a = 0;
	int b = 44;
	f(a, b);
	std::cout << "END\n";
	return 0;
}
