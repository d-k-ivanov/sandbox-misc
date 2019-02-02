/* Используйте typedef для определениея типов:
*	unsigned char, const unsigned char, указатель на целое, 
*	указатель на указатель на char, указатель на массив char, 
*	массив из 7ми указателей на int, указатель на массив из 7ми указателей на int,
*	массив из 8ми масивов по 7 указателей на целые.
*/
#include <iostream>

int main()	{
    typedef unsigned char UC;
	typedef const unsigned char CUC;
	typedef int PI;
	typedef int* PPI;
	typedef char** PPC;
	typedef char* PCA;
	PI i1 = 10;
	PI i2 = 11;
	PI i3 = 12;
	PI i4 = 13;
	PI i5 = 14;
	PI i6 = 15;
	PI i7 = 16;
	PI* arr1[7] = {&i1, &i2, &i3, &i4, &i5, &i6, &i7};
	PPI* pai = &arr1[0];
	PI* arr2[8][7];
    std::cout << "Array PI: '" << &arr1[0] << "' '" << &arr1[1] << "' '" << &arr1[2] << "' '" << &arr1[3] << "' '" << &arr1[4] << "' '" << &arr1[5] << "' '" << &arr1[6] << std::endl;
	std::cout << "Array PI: ";
	
	for (int i=0; i<7; i++) {
		std::cout << "'"<< *arr1[i] <<"' ";
	}
	std::cout << std::endl;
	
	return 0;
}
