/* Выполните тестовые прогоны, чтобы на практике убедится в эквивалентности кода для случаем итерации по элементам массива с помощью указателей и с помощью индексации.
*	Если у компилятора есть разные степени оптимизации, убедитесь, влияет ли это (и как) на качество генерируемого машинного кода
*/

#include <iostream>
int main()	
{
	int arr[10] = {0,1,2,3,4,5,6,7,8,9};
	for (int* p = arr; *p<=9; ++p)
	{
	}
	return 0;

}
