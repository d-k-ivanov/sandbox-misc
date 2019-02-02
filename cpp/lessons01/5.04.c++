/* Напишите функцию, которая обменивает значения двух целых чисел. 
 *	Используйте аргументы типа int*.
 *	Напишите другой вариант с аргументами типа int&.
 */

#include <iostream>
void sw1(int a, int b) {
	int tmp;
	tmp = a;
	a = b;
	b = tmp;
	std::cout << "A=" << a << " B=" << b << std::endl;
}

void sw2 (int& a, int& b) {
	int tmp;
	tmp = a;
	a = b;
	b = tmp;
}

int main() {
	int a1;
	int b1;

	std::cout << "Enter interger a : ";
	std::cin >> a1;
	std::cout << "Enter interger b : ";
	std::cin >> b1;
	std::cout << "A=" << a1 << " B=" << b1 << std::endl;
	std::cout << "Doing magic........." << std::endl;
	sw1(a1,b1);
	std::cout << "Print original A and B" << std::endl;
	std::cout << "A=" << a1 << " B=" << b1 << std::endl;
	std::cout << "Doing supermagic........." << std::endl;
	sw2(a1,b1);
	std::cout << "Print original A and B" << std::endl;
    std::cout << "A=" << a1 << " B=" << b1 << std::endl;
	std::cout << " WOOOOOOOOOOW......\n";
	return 0;
}
