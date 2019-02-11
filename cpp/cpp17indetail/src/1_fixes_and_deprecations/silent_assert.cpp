#include <iostream>

template <class T>
struct simple_struct1
{
    static_assert(std::is_integral_v<T>, "Type must be integer");
};

template <class T>
struct simple_struct2
{
    static_assert(std::is_integral_v<T>); // Allowd since C++17
};

int main(int argc, char* argv[])
{
    simple_struct1<int> x11;
    simple_struct2<int> x12;
    simple_struct1<double> x21;
    simple_struct2<double> x22;

    std::system("pause");
    return 0;
}
