/*	Напишите функцию atoi(const char*), которая принимает С-строку, содержащую цифры и возвращает соответствующее число.
 *  Например, для atoi("123") должно получится целое 123. модифицируйте функцию так,  чтобы помимо дестяричных обрабатывались так же восьмиричные и шестнадцатиричные */

#include <iostream>
#include <new>
#include <cstring>
#include <cctype>

char *atoi(char *s)
{
	int count=0;
	for(int i=0; isdigit(s[i]) &&  s[i]!='\0'; i++) count++;
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
	std::cout << "Enter string 1 (255 simbols max): ";
	std::cin >> s1;
	char *s2;
	s2 = atoi(s1);
	std::cout << "Reversing string: " << s2 << std::endl;
	delete []s2;
	std::cout << "END\n";
	return 0;
}
