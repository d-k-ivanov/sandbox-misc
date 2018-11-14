/*	Ведите последовательность возможно разделенных пробельными символами пар (имя, значение).
 *	Имя - единственное слово, ограниченное пробельными символами.
 *	Значение формируется целым числом или числом с плавающей запятой.
 *	Вычислите и выведите сумму и среднее как для каждого отдельного имени так и для всех имен.*/

#include <iostream>
#include <string>
#include <map>
#include <ctype.h>
#include <limits>


int main()
{
	std::multimap<std::string,float> pairs;
	while(true)
	{
		std::string s;
		float f;
		std::cout << "Enter KEY (enter \"quit\" to exit): ";
		std::cin >> s;
		if(s=="quit") break;
		std::cout << "Enter KEY-value: ";
		std::cin >> f;
		//if(std::cin.fail()) {std::cout << "Error, value have to be number. KEY-Value set to 0\n"; f=0; }
		while(std::cin.fail()) 
		{
			std::cout << "Error, value have to be a number, please set KEY-value again:"; 
			std::cin.clear(); 
			std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
			std::cin >> f;
		}
		
		pairs.insert(std::pair<std::string, float>(s,f));
	}
	
	for(std::multimap<std::string, float>::iterator it=pairs.begin(); it!=pairs.end();it++)
	{
		std::cout << "\t[" << (*it).first << ", " << (*it).second << "]" << std::endl;
	}

	std::cout << "Sum and average for each KEY:\n";
	//std::cout << "Size of pairs: " << pairs.size() << std::endl;
	std::cout << "\tKEY\t\tSUM\t\tAverage\n";
	for(std::multimap<std::string, float>::iterator it=pairs.begin(); it!=pairs.end();)
	{
		int count = pairs.count((*it).first);
		float sum = 0;
		for(int i=0; i<count;i++, it++)	
		{	
			sum+=(*it).second;
			if(i==count-1) std::cout << "\t" << (*it).first << "\t\t" << sum << "\t\t" << (sum/count) << std::endl;
		}
	}

	for(std::multimap<std::string, float>::iterator it=pairs.begin(); it!=pairs.end();it++)
    {
        static int count = 1;
		static float sum = 0;
        sum+=(*it).second;
        if(count==pairs.size()) std::cout << "\tTotal\t\t" << sum << "\t\t" << (sum/pairs.size()) << std::endl;
		count++;
    }
	
	std::cout << "END\n";
	return 0;
}
