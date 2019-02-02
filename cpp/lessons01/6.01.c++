/*	Перепешите следующий цикл for в виде эквивалентного while цикла:
 *	for(i=0; i<max_length; i++)
 *		if(input_line[i]=='?') quest_count++;
 *	Перепешите так, чтобы проверяемой величиной был указатель и условие имело вид *p=='?'. */

#include <iostream>
#include <string>

int main()
{
	char ch[1000];
	//std::string s;
	std::cout << "Введите строку со зкаками вопроса: ";
	std::cin >> ch;
	//int max_length = s.length();
	int quest_count = 0;
	//std::string* p = s;
	char* p = ch;
	while(*p!=0) 
	{
		if(*p=='?') quest_count++; 
		p++;
	}
	std::cout << "Количество знаков вопроса: " << quest_count << std::endl;
	//std::cout << max_length;

	std::cout << "END\n";
	return 0;
}
