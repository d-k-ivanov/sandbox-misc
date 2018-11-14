/* Определите структуру Date для хранения дат. Напишите функции для чтения дат из потока ввода, для вывода дат и  дя их инициализации. */

#include <iostream>
#include <string>
struct Date
{
	int day;
	std::string month;
	int year;
};

void set_Date(Date* d)
{
	std::cout << "Input day: ";
	std::cin >> d->day;
	std::cout << "Input month: ";
	std::cin >> d->month;
	std::cout << "Input year: ";
	std::cin >> d->year;
}

void print_Date(Date* d)
{
	std::cout << "Date is: " << d->day << " " << d->month << " " << d->year << std::endl;
}

int main()
{
	Date today;
	set_Date(&today);
	print_Date(&today);
	
	std::cout << "END\n";
	return 0;

}
