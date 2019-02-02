/*	Расставьте скобки в следующих выражениях */

#include <iostream>
#include <string>

int main()
{
	
	std::cout << "(a=(((b+(c*d))<<2)&8))" << std::endl;
    std::cout << "(a&(077!=3))" << std::endl;
    std::cout << "(((a==b)||(a==c))&&(c<5))" << std::endl;
    std::cout << "(c=(x!=0))" << std::endl;
    std::cout << "((0<=i)<7)" << std::endl;
    std::cout << "((f(1,2))+3)" << std::endl;
    std::cout << "(a=((((-1)++)b--)5)) -- error?" << std::endl;
    std::cout << "(a=(b==(c++)))" << std::endl;
    std::cout << "(a=(b=(c=0)))" << std::endl;
    std::cout << "(a[4][2]*=(*((b)?(c):(d*2)))) -- error?" << std::endl;
    std::cout << "((a-b),(c=d))" << std::endl;

	std::cout << "END\n";
	return 0;
}
