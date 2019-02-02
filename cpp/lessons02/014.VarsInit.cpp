#include <iostream>
using namespace std;

void total(int x);
int main()	{
	cout << "Sum 1 to 5. \n";
	total(5);
	cout << "Sum 1 to 6. \n";
	total(6);

	return 0;
}

void total(int x)	{
	int sum = 0;
	int i,count;
	for (i=1; i<=x; i++)	{
		sum = sum + i;
		for(count=0; count<10; count++) cout << ".";
		cout << "Temporary sum = " << sum << "\n";
	}
}
