#include <iostream>

int main(int argc, char* argv[])
{
    auto x0 { 1 };
    auto x1 = { 1, 2, 3 };
    auto x2 {'a'};
    auto x3 { 1.0 };
    auto x4 = { "Hello!" };

    std::cout << "X0 type: " << typeid(x0).name() << '\n';
    std::cout << "X1 type: " << typeid(x1).name() << '\n';
    std::cout << "X2 type: " << typeid(x2).name() << '\n';
    std::cout << "X3 type: " << typeid(x3).name() << '\n';
    std::cout << "X4 type: " << typeid(x4).name() << '\n';

    std::system("pause");
    return 0;
}
