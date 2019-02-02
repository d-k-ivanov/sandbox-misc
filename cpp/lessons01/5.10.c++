/* Определите массив строк, содержащих названия месяцев.
*   Распечатайте эти строки. Для печати передайте этот массив в функцию.
*/

#include <iostream>
#include <string>

void print_array(std::string* arr, int number) {
	std::cout << "\033[0;36mMoving through array with indexes: \033[0m" << std::endl;
	for (int i=0; i<number; i++) std::cout << "\033[0;3" << (i%6)+1 << "m" << arr[i] << "; ";
	std::cout << "\033[0m" << std::endl;
	std::cout << "\033[0;36mMoving through array with pointers: \033[0m" << std::endl;
	for(std::string* p = arr; number!=0 ;number--, ++p) std::cout << "\033[0;3" << (number%6)+1 << "m" << *p << "; ";
	std::cout << "\033[0m" << std::endl;
}

int main()	{
	std::string	months[] = {"Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"};
// test array
//	for (int i=0; i<sizeof(months)/sizeof(*months); i++) std::cout << months[i] << std::endl;

	print_array(months, sizeof(months)/sizeof(*months));
	std::cout << "END\n";
	return 0;
}
