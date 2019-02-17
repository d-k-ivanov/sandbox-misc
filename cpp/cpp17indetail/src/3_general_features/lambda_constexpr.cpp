#include <iostream>

int main(int argc, char* argv[])
{
    auto la1 = [](int n) { return n + n; };
    static_assert(la1(2) == 4, "");
    std::cout << la1(2) << '\n';

    auto la2 = [](int n) constexpr { return n + n; };
    static_assert(la2(3) == 6, "");
    std::cout << la2(3) << '\n';

    // Non-ConstExpr lambda:
    //auto NonConstExprLambda = []() constexpr { return new int(10);};
    auto NonConstExprLambda = []() { return new int(10); };

    std::cout << '\n';
    std::system("pause");
    return 0;
}
