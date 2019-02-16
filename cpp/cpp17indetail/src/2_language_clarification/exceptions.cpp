#include <iostream>
#include <array>

void(*p)();
void(**pp)() noexcept = &p; // error: cannot convert to pointer to noexcept function

struct S { typedef void(*p)(); operator p(); };
void(*q)() noexcept = S(); // error: cannot convert to pointer to noexcept

int main(int argc, char* argv[])
{
    std::cout << '\n';
    std::system("pause");
    return 0;
}
