#include <iostream>
#include <string>

int main()	{
  //	using namespace std;
  int choice;
  std::cout << " 1 - Pointers and Arrays declarations\n";
  std::cout << " 2 - char*, int*, void* restrictions\n";
  std::cout << " 3 - typedef\n";
  std::cout << " 4 - int a <=> int b switching\n";
  std::cout << " 5 - \"a short string\" size\n";
  std::cout << " 6 - functions (links)\n";
  std::cout << " 7 - Months and days count\n";
  std::cout << " 8 - Arrays iteration with pointers and indexes\n";
  std::cout << " 9 - Пример, когда имеет смысл использовать объявляемое имя в инициализаторе\n";
  std::cout << "10 - Months from function \n";
  std::cout << "11 - Cin, sort, repetitions, quit\n";
  std::cout << "12 - Count simbol pair in string\n";
  std::cout << "13 - Date struct\n";
  std::cout << "Enter from 1 to 7: ";
  std::cin >> choice;
  std::cout << "\n";
  
  switch(choice) {
    case 1:	{
    /* Напишите следующие объявления и инициализируйте объекты: 
    * 	+указатель на символ
    * 	+массив из 10 целых
    * 	+ссылка на массив из 10 целых
    * 	+указатель на массив строк
    * 	+указатель на указатель на символ
    * 	целая константа
    * 	указатель на целую константу
    * 	константный указатель на целое.
    */
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
    break;
    }

    case 2:	{
    /* Каковы на вашей машине ограничения на значения указатeлей типа char*, int* и void*?
    *	Например может ли int* иметь нечетное значение (подумайте о выравнивании)
    */
	std::cout << "CHAR*\t:\tМожет быть расположен в любом доступном адресе, потому что размер типа char равер 1 байту\n";
	std::cout << "INT*\t:\t32-х битные процессоры требуют, чтобы 4-х байтные целые числа были расположены в ячейках памяти, кратных 4-м. Это называется выравниевание в памяти по типам. Таким образом, 4-х байтные целые могут быть распложены в яейках с адресами: 0x2000, 0x2004, 0x2008 и т.д., но немогут быть  расположены в 0x2001 или 0x2003.\n";
	std::cout << "VOID*\t:\tТип VOID* имеет размер 4 байта, поэтому имеет те же ограничеия, что и INT.*\n";
	std::cout << "\n ====== \nНа большинстве Unix систем, попытка использовать невыровненные данные вызовет ошибку шины, которая аварийно завершит приложение. На процессорах фирмы интел использование невыровненных данных будет являться причиной серьезной потери производительности. Поэтому большинство компиляторов автоматически выравниваю данные, исходя из их типов и типа процессора. Выравнивание памяти является причиной того, что структуры и классы фактически занимают больше места чем сумма их членов.\n ====== \n";
	break;
    }
    
	case 3: {
    /* Используйте typedef для определениея типов:
    *	unsigned char, const unsigned char, указатель на целое, 
    *	указатель на указатель на char, указатель на массив char, 
    *	массив из 7ми указателей на int, указатель на массив из 7ми указателей на int,
    *	массив из 8ми масивов по 7 указателей на целые.
    */
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
	break;
    }
	
	case 4: {
    /* Напишите функцию, которая обменивает значения двух целых чисел. 
    * 	Используйте аргументы типа int*.
    * 	Напишите другой вариант с аргументами типа int&.
    */
	int sw1(int a, int b) 
	{
		int tmp;
		tmp = a;
		a = b;
		b = tmp;
		std::cout << "A=" << a << " B=" << b << std::endl;
	}
	
	int a1;
	int b1;
	
	std::cout << "Enter interger a : ";
	std::cin >> a1;
	std::cout << "\n";
	std::cout << "Enter interger b : ";
	std::cin >> b1;
	std::cout << "\n";
	
	std::cout << "A=" << a1 << " B=" << b1 << std::endl;
	std::cout << "Doing magic........." << std::endl;
	sw1(a1,b1);
	
	break;
    }
    
	case 5: {
    /* Каков размер массива str в слудующим примере:
    *	char str[] = "a short string";
    *	Какова длинна строки "a short string"?
    */
    
	break;			
    }
    
	case 6: {
    /* Определите функции f(char), g(char&) и h(const char&).
    *	Вызовите их с аргументами: 'a', 49, 3300, c, uc и sc, где с - char, uc - insigned char, sc - signed char.
    *	Какие из этих вызовов допустимы?
    */
    
	break;
    }
    
	case 7: {
    /* Определите таблицу имен месяцев и количества дней в них. Выведите эту таблицу.
    *	Проделайте это дважды: первый раз воспользуйтесь массивом типа int для количества элементов типа char для названия месяца и массивом типа int для количества дней.
    *	второй раз примените массив структур, которые содержат и названия месяцев и число дней.
    */
    
	break;
    }
    
	case 8: {
    /* Выполните тестовые прогоны, чтобы на практике убедится в эквивалентности кода для случаем итерации по элементам массива с помощью указателей и с помощью индексации.
    *	Если у компилятора есть разные степени оптимизации, убедитесь, влияет ли это (и как) на качество генерируемого машинного кода
    */
    
	break;
    }
    
	case 9: {
    /* Продемонстрируйте пример, когда имеет смысл использовать объявляемое имя в инициализаторе*/
    
    break;
    }
    
	case 10: {
    /* Определите массив строк, содержащих названия месяцев.
    *	Распечатайте эти строки. Для печати передайте этот массив в функцию.
    */
    
	break;
    }
    
	case 11: {
    /* Читайте последовательность слов из потока ввода. Пусто слово Quit служит признаком конца ввода.
    *	Печатайте слова в порядке, в каком они были введены, но не допускайте повторов. Модифицируйте программу так, чтобы перед печатью слова сортировались.
    */
    
	break;
    }
    
	case 12: {
    /* Напишите функцию, которая подсчитывает количество повтров пар букв в строке типа string, а так же в символьном массиве с терминальнам нулём (строка в С-стиле)
    *	Например, пара букв "ab" входит в строку "xabaacbcxabb" дважды.
    */
    
	break;
    }
    
	case 13: {
    /* Определите структуру Date для хранения дат. Напишите функции для чтения дат из потока ввода, для вывода дат и  дя их инициализации. */
    
	break;
    }
    
	default:
      std::cout << "Wrong number! Exit...\n";
      return 1;
    }
std::cout << "\n";
std::cout << "END\n";
return 0;
}
