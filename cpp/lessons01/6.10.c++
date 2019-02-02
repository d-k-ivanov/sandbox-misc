/*	Напишите следующие функции:
 *		strlen() - возвращает длинну строки в С-стиле
 *		strcpy() - копирует одну строку в другую
 *		strcmp() - сравнение содержимого двух строк */

#include <iostream>

int strlen(char *s)
{
	int i = 0;
	while(s[i]!='\0') i++;
	return i;
}

void strcpy(char *s1, char *s2)
{
	int i = 0;
    while(s1[i]!='\0')
	{
		s2[i]=s1[i];
		i++;
	}
}

bool strcmp(char *s1, char *s2)
{
	int i = 0;
    while(s1[i]!='\0' || s2[i]!='\0')
    {
        if(s2[i]!=s1[i]) return false;
		i++;
    }
	return true;
}

int main()
{
	std::cout << "1 - CString length" << std::endl;
	std::cout << "2 - Copy CString1 to CString2" << std::endl;
	std::cout << "3 - String comparsion" << std::endl;
	int choice;
	std::cout << "Choose tool: "; 
	std::cin >> choice; 
	switch(choice)
	{
		case 1:
		{
			char s[255];
			std::cout << "Enter string (255 simbols max): ";
			std::cin >> s;
			std::cout << "String length= " << strlen(s) << std::endl;
			break;
		}
		case 2:
		{
			char s1[255];
            char s2[255];
            std::cout << "Enter source string (255 simbols max): ";
            std::cin >> s1;
            std::cout << "Enter destination string (255 simbols max): ";
            std::cin >> s2;
            std::cout << "String source: " << s1 << std::endl;
            std::cout << "String destination " << s2 << std::endl;
			std::cout << "Transformation performing..." << std::endl;
			strcpy(s1,s2);
			std::cout << "String source: " << s1 << std::endl;
            std::cout << "String destination " << s2 << std::endl;
			break;
		}
		case 3:
		{
			char s1[255];
            char s2[255];
            std::cout << "Enter string 1 (255 simbols max): ";
            std::cin >> s1;
            std::cout << "Enter string 2 (255 simbols max): ";
            std::cin >> s2;
            std::cout << "String comparsion...." << std::endl;
			if(strcmp(s1, s2)) std::cout << "String 1 SAME as String 2" << std::endl;
			else std::cout << "String 1 NOT SAME as String 2" << std::endl;
			break;
		}
		default:
		{
			std::cout << "Wrong number" << std::endl;
			break;
		}
	}

	std::cout << "END\n";
	return 0;
}
