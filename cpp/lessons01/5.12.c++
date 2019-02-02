/* Напишите функцию, которая подсчитывает количество повтров пар букв в строке типа string, а так же в символьном массиве с терминальнам нулём (строка в С-стиле)
*   Например, пара букв "ab" входит в строку "xabaacbcxabb" дважды.
*/
#include <iostream>
#include <string>
#include <new>
//using namespace std;

void count_pairs(std::string s)
{
	int len = s.length()-1;
	std::string pairs[len];
	for(int i=0; i<len; i++) (pairs[i]+=s[i])+=s[i+1];
	
	std::cout << "Подсчет пар символов в строке: " << s << std::endl;
	for(int i=0; i<len; i++)
	{	
		int same=0;
		int count=0;
		for(int j=i-1; j>=0; j--) if(pairs[i]==pairs[j]) same=1;
		if (same!=0) continue;
		for(int k=i; k<len; k++) if(pairs[i]==pairs[k]) count++;
		std::cout <<  pairs[i] << "=" << count << "\t";
	}
	std::cout << std::endl;
}

/*void count_pairs(const char* ch, int len)
{
	std::string pairs[len];
	for(int i=0; i<len; i++) (pairs[i]+=ch[i])+=ch[i+1];
	for(int i=0; i<len; i++) std::cout << pairs[i] << " " ;
	std::cout << std::endl;

	std::cout << "Подсчет пар символов в строке: " << ch << std::endl;
	for(int i=0; i<len; i++)
	{
		
		int same=0;
		int count=0;
		for(int j=i-1; j>=0; j--) if((pairs[i]==pairs[j])) same=1;
		if (same==1) continue;
		for(int k=i; k<len; k++) if(pairs[i]==pairs[k]) count++;
		std::cout <<  pairs[i] << "=" << count << "\t";
	}
	std::cout << std::endl;
}*/

void count_pairs(const char* ch)
{
	count_pairs(static_cast<std::string>(ch));
}



int main()	
{
	
	//std::string str = "abracadabra";
	//std::string str = "kavavakatra";
	std::string str;
	std::cout << "Ведите строку и нажмите \"Enter\": ";
	std::cin >> str;
	count_pairs(str);
	
	const char* cha = "kavavakatra";
	/*std::cout << "Char  : ";
	int len;
	for(len=0;cha[len]!=0; len++);
	std::cout << len << std::endl;
	count_pairs(cha, len); */
	count_pairs(cha);
	
	std::cout << "END\n";
	return 0;

}
