#include <iostream>
using namespace std;

void func1();
int main()
{
cout << "In MAIN\n";
func1();
cout << "Again in MAIN\n";

return 0;
}

void func1()
{
cout << "In FUNC1\n";
}

