#include <iostream>
#include <cstdlib>
using namespace std;

int main()	{
	int magic;
	int guess;
	magic = rand();
	cout << "Enter your answer: ";
	cin >> guess;
	cout << "\n";
	if(guess==magic)	{
	cout << "**RIGHT**" << "\n";
	cout << magic << " is the magic number";
	}
	else	{
	cout << "**WRONG**\n";
	if(guess > magic) cout << "Your answer greater than the magic number.\n";
	else cout << "Your answer lesser than the magic number.\n";
	}
return 0; }
