#include <iostream>
#include <string>
#include <iomanip>
#include <limits>

int main()	{
	//	using namespace std;
	int choice;
	std::cout << "1 - Hello World\n";
	std::cout << "2 - Vars definition and declarations\n";
	std::cout << "3 - Size of different types\n";
	std::cout << "4 - a-z,0-9 - Dec code - Hex code\n";
	std::cout << "5 - Limits of fundamental types\n";
	std::cout << "6 - Limits of names and spec simbols\n";
	std::cout << "7 - Graf of fundamental types\n";
	std::cout << "Enter from 1 to 7: ";
	std::cin >> choice;

	switch(choice) {
		case 1:	{
			// 	4.1	Hello, World!
			std::cout << "Hello, world!\n";
			return 0;
		}
		case 2:	{
			//	4.2 Для каждого объявления из $4.9 выполните следующее:
			//  	если объявление не является определением, переделайте его в определение;
			//  	если объявление является опреелением, напишите для него соответствующее объявление, не являющееся одновременно и определением.
			char ch;
			std::string s;
			int count;
			ch='c';
			std::cout << ch << "\n";
			s="String here\n";
			std::cout << s;
			count=1;
			std::cout << count << "\n";
			return 0;
		}
		case 3: {
			//  4.3	Напишите программу, которая выводит размеры (используйте операцию sizeof):
			//  	фундаментальных типов
			//  	нескольких указателей
			//  	нескольких перечислений
			bool b1 = false;
			char c1 = 'c';
			int i1 = 1;
			double d1 = 1;
			enum e1 {dark, light};
			enum e2 {ee1 = 3,ee2 = 9};
			enum e3 {min = -10,max = 1000000};
			int* i2 = &i1;
			char* c2 = &c1;
			char c4[] = "Hello, World!";
			std::cout << "Size of different types (bytes):\n";
			std::cout << "bool = " << sizeof(b1) << std::endl << "char = " << sizeof(c1) << std::endl << "int = " << sizeof(i1) << std::endl;
			std::cout << "double = " << sizeof(d1) << std::endl << "enum1  = " << sizeof(e1) << std::endl << "enum2 = " << sizeof(e2) << std::endl << "enum3 = " << sizeof(e3) << std::endl;
			std::cout << "pointer int = " << sizeof(i2) << std::endl << "pointer char = " << sizeof(c2) << std::endl;
			std::cout << "Char[Hello, World!] = " << sizeof(c4) << std::endl;
			return 0;
		}
		case 4: {
			//  4.4	Напишите программу, которая выводит буквы 'a' - 'z' и цифры '0' - '9' и их десятичные коды. 
			//  	Повторите всё для иных символов, имеющих зрительные	образы.
			//  	Выведите числовые коды в шестнадцатиричном виде
			char c;
			int i;
			std::cout << "Char\t=\tDec\t=\tHex\n";
			/*
			for (i = '0'; i <= '9'; i++)
            {
                std::cout << i << "\t=\t" << std::dec << int(i) << "\t=\t" << std::hex << int(i) <<  std::endl;
            }
			for (i = 'A'; i <= 'Z'; i++)
			{
				std::cout << i << "\t=\t" << std::dec << int(i) << "\t=\t" << std::hex << int(i) <<  std::endl;
			}
			for (i = 'a'; i <= 'z'; i++)
            {
                std::cout << i << "\t=\t" << std::dec << int(i) << "\t=\t" << std::hex << int(i) <<  std::endl;
            }
			*/
			for (i = 33; i <= 126; i++)
            {
				c = i;
                std::cout << c << "\t=\t" << std::dec << int(c) << "\t=\t" << std::hex << int(c) <<  std::endl;
            }
			return 0;
		}
		case 5: {
			//  4.5	Каковы на вашей машине минимальные и максимальные значения для следующих типов:
			//  	char, short, int, long, float, double, long double, unsigned
			std::cout << "type\tminimum\tmaximum\n";	
			std::cout << "bool\t" 			<< std::numeric_limits<bool>::min() 			<< "\t" << std::numeric_limits<bool>::max() 			<< std::endl;
			std::cout << "char\t" 			<< std::numeric_limits<char>::min() 			<< "\t" << std::numeric_limits<char>::max() 			<< std::endl;
			std::cout << "signed char\t" 	<< std::numeric_limits<signed char>::min() 		<< "\t" << std::numeric_limits<signed char>::max() 		<< std::endl;
			std::cout << "unsigned char\t" 	<< std::numeric_limits<unsigned char>::min() 	<< "\t" << std::numeric_limits<unsigned char>::max() 	<< std::endl;
			std::cout << "wchar_t\t" 		<< std::numeric_limits<wchar_t>::min() 			<< "\t" << std::numeric_limits<wchar_t>::max() 			<< std::endl;
            std::cout << "short int\t" 		<< std::numeric_limits<short>::min() 			<< "\t" << std::numeric_limits<short>::max() 			<< std::endl;
            std::cout << "int\t" 			<< std::numeric_limits<int>::min() 				<< "\t" << std::numeric_limits<int>::max() 				<< std::endl;
            std::cout << "long int\t" 		<< std::numeric_limits<long>::min() 			<< "\t" << std::numeric_limits<long>::max() 			<< std::endl;
            std::cout << "long long\t" 		<< std::numeric_limits<long long>::min() 		<< "\t" << std::numeric_limits<long long>::max() 		<< std::endl;
            std::cout << "float\t" 			<< std::numeric_limits<float>::min() 			<< "\t" << std::numeric_limits<float>::max() 			<< std::endl;
			std::cout << "double\t" 		<< std::numeric_limits<double>::min() 			<< "\t" << std::numeric_limits<double>::max() 			<< std::endl;
			std::cout << "long double\t" 	<< std::numeric_limits<long double>::min() 		<< "\t" << std::numeric_limits<long double>::max() 		<< std::endl;	
			return 0;			
		}
		case 6: {
			//  4.6	Какова максимальная длинна локальных имён на Вашей машине?
			//  	Какова максимальная длинна внешних имён на Вашей машине?
			//  	Есть ли ограничения на символы, которые можно использовать в именах?
			std::cout << "This is no c++ question, but OS restrictions can have been made." << "\n";	
			return 0;
		}
		case 7: {
			//  4.7	Нарисуйте граф для фундаментальных типов, поддерживаемых любой стандартной реализацией 
			//  	(стрелка указывает направление от первого типа ко второму, если все значения первого типа представимы переменными второго типа)
			//  	Нарисуйте тот же граф, но для вашей любимой реализации
			std::cout << "bool -> char -> short -> int -> float -> double\n";
			std::cout << "bool -> char -> int -> double\n";
			return 0;
		}
		default:
			std::cout << "Wrong number! Exit...\n";
			return 1;
	}
}















