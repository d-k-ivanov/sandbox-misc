#include <iostream>
using namespace std;

int mul(int x, int y);
int main()
{
int answer;
answer = mul(10,11);
cout << "Answer: " << answer << "\n";

return 0;
}

int mul(int x, int y)
{
return x * y;
}
