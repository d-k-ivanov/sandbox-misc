/* Каковы на вашей машине ограничения на значения указатeлей типа char*, int* и void*?
*	Например может ли int* иметь нечетное значение (подумайте о выравнивании)
*/

#include <iostream>
int main() {
	std::cout << "CHAR*\t:\tМожет быть расположен в любом доступном адресе, потому что размер типа char равер 1 байту\n";
	std::cout << "INT*\t:\t32-х битные процессоры требуют, чтобы 4-х байтные целые числа были расположены в ячейках памяти, кратных 4-м. Это называется выравниевание в памяти по типам. Таким образом, 4-х байтные целые могут быть распложены в яейках с адресами: 0x2000, 0x2004, 0x2008 и т.д., но немогут быть  расположены в 0x2001 или 0x2003.\n";
	std::cout << "VOID*\t:\tТип VOID* имеет размер 4 байта, поэтому имеет те же ограничеия, что и INT.*\n";
	std::cout << "\n ====== \nНа большинстве Unix систем, попытка использовать невыровненные данные вызовет ошибку шины, которая аварийно завершит приложение. На процессорах фирмы интел использование невыровненных данных будет являться причиной серьезной потери производительности. Поэтому большинство компиляторов автоматически выравниваю данные, исходя из их типов и типа процессора. Выравнивание памяти является причиной того, что структуры и классы фактически занимают больше места чем сумма их членов.\n ====== \n";
	
	return 0;

}
