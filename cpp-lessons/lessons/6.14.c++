/*  Напишите функцию cat(), которая принимает в качестве аргументов две C-строки и возвращает конкатенированную C-строку.
 *  Используйте операцию new для выделения памяти под пезультат*/

#include <iostream>
#include <new>
#include <cstring>

char *rev(char *s)
{
	int count=0;
	for(int i=0; s[i]!='\0'; i++) count++;
	std::cout << "Count: " << count << std::endl;
	char *sr;
	sr = new char[count+1];
	memset (sr, 0, (count+1) * sizeof (char));
	for(int i=0; count>=0; i++, count--) sr[i]=s[count-1];
	//std::cout << "Concetenated string: " << s3 << std::endl;
	//delete []s3;
	return sr;	
}

int main()
{
	char s1[255];
	char *s2;
	std::cout << "Enter string 1 (255 simbols max): ";
	std::cin >> s1;
	s2 = rev(s1);
	std::cout << "Reversing string: " << s2 << std::endl;
	//std::cout << sizeof(s1) << " " << sizeof(s2) << std::endl;
	delete []s2;
	std::cout << "END\n";
	return 0;
}
