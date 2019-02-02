/* Каков размер массива str в слудующим примере:
*	char str[] = "a short string";
*	Какова длинна строки "a short string"?
*/

#include <iostream>
#include <string.h>

int main(){
	char str1[] = "a short string";
	char str2[1000];
	std::cout << "Length of str1[] = " << str1 << " = " << strlen(str1) << std::endl; 
	std::cout << "Size of str1[] = " << sizeof(str1) << std::endl;
	int i = sizeof(str1);
	char c = str1[i];
	std::cout << "Last simbol: str1[" << c << "] = '" << int(c) << "'"<< std::endl;

	std::cout << "Введите строку в str2[1000]: ";
	std::cin.get(str2,1000);
	std::cout << "Length of str2[1000] = " << str2 << " = " << strlen(str2) << std::endl;
	std::cout << "Size of str2[1000] = " << sizeof(str2) << std::endl;
	int i2 = sizeof(str2);
	char c2 = str1[i2];
	std::cout << "Last simbol: str1[" << c2 << "] = '" << int(c2) << "'"<< std::endl;
	
	return 0;
}

