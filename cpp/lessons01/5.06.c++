/* Определите функции f(char), g(char&) и h(const char&).
*	Вызовите их с аргументами: 'a', 49, 3300, c, uc и sc, где с - char, uc - insigned char, sc - signed char.
*	Какие из этих вызовов допустимы?
*/

#include <iostream>
void f(char ch) {
std::cout << "Arg = '" << ch << "'" << std::endl; 
}

void g(char& ch) {
std::cout << "Arg = '" << ch << "'" << std::endl;
}

void h(const char& ch) {
std::cout << "Arg = '" << ch << "'" << std::endl;
}

int main()	{
	
	char ch1;
	unsigned char ch2;
	signed char ch3;

	ch1 = 'c';
	ch2 = 'u';
	ch3 = 's';

	std::cout << "Funcrion #1\n";
	f('a');
	f(49);		//49 - Конвентируется в char согласно таблице ASCII, 49 = '1'
	//f(3300);  //3300 - не может быть конвентировано в char, выходит за рамки из 256-символов
	f(ch1);
	f(ch2);
	f(ch3);	
	
	std::cout << "\nFunction #2\n";
	//g('a');
	//g(49);
	//g(3300);
	g(ch1);
    //g(ch2);
    //g(ch3);	

	std::cout << "\nFunction #3\n";
    h('a');
    h(49);
    //h(3300);
    h(ch1);
    h(ch2);
    h(ch3);

	
	return 0;
}
