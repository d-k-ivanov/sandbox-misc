#include <iostream>

int main()
{
    int n = 1;
    for (std::cout << "INIT\n";
        std::cout << "ITERATION_CONDITION\n";
        std::cout << "EXPRESSION\n") {
        std::cout << "ITERATION " << n << "\n";
        n++;
        if (n == 5)
            break;
    }

    std::cout << '\n';
    std::system("pause");
    return 0;
}
