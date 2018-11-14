/* Определите таблицу имен месяцев и количества дней в них. Выведите эту таблицу.
*	Проделайте это дважды: первый раз воспользуйтесь массивом типа char для названия месяца и массивом типа int для количества дней.
*	второй раз примените массив структур, которые содержат и названия месяцев и число дней.
*/

#include <iostream>
#include <string>
int main()	
{
	int ch;
	std::cout << "Months and days count output.\nChoose the way:\n\t1) Arrays (char*=names, int=days)\n\t2) Structure\n";
	std::cin >> ch;
	switch(ch) 
	{
		case 1:	
		{
			const char* names[12] = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "Decemder"};
			int days[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
			// std::cout << "Names = " << sizeof(names) << " Days = " << (sizeof(days)/sizeof(*days)) << " ---" << sizeof(*days) << "-----" << std::endl;	
			for (int i=0; i < (sizeof(days)/sizeof(*days)); i++) {
				std::cout << names[i] << " = " << days[i] << std::endl;
			}
			break;
		}
		
		case 2:	
		{
			struct MTH 
			{
				std::string name;
			//	const char* name;
				int days;
			};
			//for (int i=0; i<12; i++) year[0].name[0] = '\0';
			MTH year[12] = {{"January", 31},{"February", 28},{"March", 31},{"April", 30},{"May", 31},{"June", 30},{"July", 31},{"August", 31},{"September", 30},{"October", 31},{"November", 30},{"Decemder", 31}};

			//MTH year[12] = {{"Jan", 31},{"Feb", 28},{"Mar", 31},{"Apr", 30},{"May", 31},{"Jun", 30},{"Jul", 31},{"Aug", 31},{"Sep", 30},{"Oct", 31},{"Nov", 30},{"Dec", 31}};

			/*	
 			year[0] = {"January", 31};
            year[1] = {"February", 28};
            year[2] = {"March", 31};
            year[3] = {"April", 30};
            year[4] = {"May", 31};
            year[5] = {"June", 30};
            year[6] = {"July", 31};
            year[7] = {"August", 31};
            year[8] = {"September", 30};
            year[9] = {"October", 31};
            year[10] = {"November", 30};
            year[11] = {"Decemder", 31};
			*/
			std::cout << "YEAR[] = " << sizeof(year) << " " << sizeof(*year) << " " << (sizeof(year)/sizeof(*year)) << std::endl;
			
			for (int i=0; i<12; i++) 
			{
				std::cout << year[i].name << " = " << year[i].days << std::endl;
			}
			
			break;
		
		}	
	
		default: 
		{
			std::cout << "Wrong number!\n";
			return 1;
		}
    }
    std::cout << "END\n";
	return 0;

}
