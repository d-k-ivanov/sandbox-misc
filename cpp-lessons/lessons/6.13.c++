/*  Напишите функцию cat(), которая принимает в качестве аргументов две C-строки и возвращает конкатенированную C-строку.
 *  Используйте операцию new для выделения памяти под пезультат*/

#include <iostream>
#include <new>
#include <cstring>

char *cat(char *s1, char *s2)
{
	int count=0;
	/*int i=0;
    while(s1[i]!='\0')
	{
		count++;
		i++;
	}
	i=0;
	while(s2[i]!='\0')
    {
        count++;
		i++;
    }*/
	for(int j=0; s1[j]!='\0'; j++) count++;
	for(int j=0; s2[j]!='\0'; j++) count++;
	std::cout << "Count: " << count << std::endl;
	char *s3;
	s3 = new char[count+1];
	memset (s3, 0, (count+1) * sizeof (char));
	for(int i=0; i<=count; i++)
	{
	for(int j=0; s1[j]!='\0'; j++, i++) s3[i]=s1[j];
	for(int j=0; s2[j]!='\0'; j++, i++) s3[i]=s2[j];
	}
	//std::cout << "Concetenated string: " << s3 << std::endl;
	//delete []s3;
	return s3;	
}

int main()
{
	char s1[255];
	char s2[255];
	char *s3;
	std::cout << "Enter string 1 (255 simbols max): ";
	std::cin >> s1;
	std::cout << "Enter string 2 (255 simbols max): ";
	std::cin >> s2;
	s3 = cat(s1,s2);
	std::cout << "Concetenated string: " << s3 << std::endl;
	//std::cout << sizeof(s1) << " " << sizeof(s2) << std::endl;
	delete []s3;
	std::cout << "END\n";
	return 0;
}
