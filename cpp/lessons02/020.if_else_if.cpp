#include <iostream>
using namespace std;

int main()	{
	int x;
	for(x=0;x<6;x++)	{
		if(x==1) cout << "X = 1.\n";
		else if (x==2) cout << "X = 2.\n";
		else if (x==3) cout << "X = 3.\n";
		else if (x==4) cout << "X = 4.\n";
		else cout << "X - doesn't belong 1-4 range.\n";
	}
return 0;	}
