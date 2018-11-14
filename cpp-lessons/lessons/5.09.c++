/* Продемонстрируйте пример, когда имеет смысл использовать объявляемое имя в инициализаторе*/

#include <iostream>
int main()	
{
	int i01 = { sizeof(i01) };
	
	std::cout << "END\n";
	return 0;

}
