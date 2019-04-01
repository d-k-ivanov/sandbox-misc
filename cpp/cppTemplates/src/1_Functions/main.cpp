#include <iostream>n
#include <string>

#include "max.hpp"

int main()
{
    std::cout << '\n' << std::string(80, '-') << '\n';

    std::cout << "max1(42,7): " << ::max1(42, 7) << '\n';
    std::cout << "max2(42,7): " << ::max2(42, 7) << '\n';
    std::cout << "max1(math,mathematica): " << ::max1(std::string("math"), std::string("mathematica")) << '\n';
    std::cout << "max1(3.14,3.141): " << ::max1(3.14, 3.141) << '\n';

    std::cout << '\n' << std::string(80, '-') << '\n';

    std::system("pause");
    return 0;
}
