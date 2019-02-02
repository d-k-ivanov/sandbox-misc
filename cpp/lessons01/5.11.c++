/* Читайте последовательность слов из потока ввода. Пусто слово Quit служит признаком конца ввода.
*   Печатайте слова в порядке, в каком они были введены, но не допускайте повторов. Модифицируйте программу так, чтобы перед печатью слова сортировались.
*/
#include <iostream>
#include <string>
#include <algorithm>
int main()	{
	std::string words[1000];
	std::cout << "Quit служит признаком конца ввода\nВеедите до " << (sizeof(words)/sizeof(*words)) << " слов:" << std::endl;
	int i=0;	
	int j;
	while (true) {
		std::cout << "Введите слово №" << i+1 << ": ";
		std::cin >> words[i];
		if(words[i]=="Quit") break;
		i++;
		if(i==sizeof(words)/sizeof(*words)) break;
	}

	std::cout << "Вы ввели следующие слова: ";	
	j=0;
	int final_index=0;
	while(words[j]!="Quit") {
		int same=0;
		for(int k=0; k<j; k++) if(words[k]==words[j]) same=1;
		if(same==1) {j++; continue;};
		std::cout << words[j] << " ";
		final_index++;
		j++;
	}
	std::cout << std::endl;
	std::cout << "J=" << j << "  " << "Final_index=" << final_index << std::endl;
	
	std::cout << "Отсортированые слова: ";
	std::string sorted[final_index];
	j=0;
	while(words[j]!="Quit") {
		static int m=0;
		int same=0;
		for(int k=0; k<j; k++) if(words[k]==words[j]) same=1;
		if(same==1) {j++; continue;};
		sorted[m]= words[j];
		m++;
		j++;
	}
	std::sort(sorted, sorted+(final_index-1));
	for(int k=0; k<final_index; k++) std::cout << sorted[k] << " ";
	std::cout << std::endl;
	
	std::cout << "END\n";
	return 0;
}
