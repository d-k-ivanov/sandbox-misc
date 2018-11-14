 /* Напишите следующие объявления и инициализируйте объекты: 
*	+указатель на символ
*	+массив из 10 целых
*	+ссылка на массив из 10 целых
*	+указатель на массив строк
*	+указатель на указатель на символ
*	целая константа
*	указатель на целую константу
*	константный указатель на целое.
*/

#include <iostream>
#include <string>

int main() {
    std::cout << "----------------------Char pointers: ----------------------\n";
    char c1 = 'a';
    char* p1 = &c1;
    char** p2 = &p1;
    std::cout << "Char= '" << c1 << "'; Char address= '" << static_cast <const void *>(&c1) <<"'; ";
    std::cout << "Pointer to char= '" << static_cast <const void *>(p1) << "'; Pointer address = '" << static_cast <const void *>(&p1) << "'; ";
    std::cout << "Pointer pointer= '" << static_cast <const void *>(p2) << "'; Pointer pointer address= '" << static_cast <const void *>(&p2) << "'" << std::endl;
    std::cout << "\n";

    std::cout << "----------------------INT array and pointers: ----------------------\n";
    int arr1[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
    int* p3 = arr1;
    std::cout << "Array 1 = '" << arr1[10] << "'; Array address = '" << p3 << "'; Adress arr1[10] = '" << &arr1[10] << "'" << std::endl;
    std::cout << "\n";

    std::cout << "----------------------String array anf pointers: ----------------------\n";
    std::string arr2[5] = {"One", "Two", "Three", "Four", "Five" };
    void* p4 = &arr2;
    std::cout << "String array = " << arr2[0] << " " <<  arr2[1] << " " << arr2[2] << " " << arr2[3] << " " << arr2[4] << " " << std::endl;
    std::cout << "Pointer  = '" << p4 << "';" << std::endl;
    std::cout << "Pointer to arr2[0] = '" << &arr2[0] << "'; Pointer to arr2[1] = '" << &arr2[1] << "'; Pointer to arr2[2] = '" << &arr2[2] << "'; ";
    std::cout << "Pointer to arr2[3] = '" << &arr2[3] << "'; Pointer to arr2[4] = '" << &arr2[4] << "'" << std::endl;
    std::cout << "\n";

    std::cout << "---------------------- Constant and pointers: ----------------------\n";
    const int ci = 1000;
    int i1 = 1001;
    const int* p5 = &ci;
    int* const p6 = &i1;
    std::cout << "Constant: '" << ci << "'; Constant addr: '" << &ci << "';Pointer to contstant: '" << p5 << "'; Pointer to constant addr: '" << &p5 << "'; " << std::endl;
    std::cout << "Int: '" << i1 << "'Int addr: '" << &i1 << "'; Constant pointer to Int: '" << p6 << "'; Pointer to int addr: '" << &p6 << "'; " << std::endl;

	return 0;
}
