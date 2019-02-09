#include <iostream>
#include <array>
#include <string>

namespace local {
    template<class T>
    struct is_array:std::is_array<T> {};

    template<class T, std::size_t N>
    struct is_array<std::array<T, N>>:std::true_type {};

    template<class T>
    inline constexpr bool is_array_v = local::is_array<T>::value;
}

template<typename T> void PrintLine (const T& x)
{
    if constexpr (std::is_integral_v<T>)
        std::cout << "Int : " << x << '\n';
    else if constexpr (std::is_floating_point_v<T>)
    {
        const auto fraction = x - static_cast<long>(x);
        std::cout << "Float : " << x << " | Fraction : " << fraction << '\n';
    }
    else if constexpr (std::is_pointer_v<T>)
    {
        std::cout << "<ptr>\n";
        PrintLine(*x);
        std::cout << "</ptr>\n";
    }
    else if constexpr (local::is_array_v<T>)
    {
        std::cout << "Array : ";
        for (const auto &element : x)
            std::cout << element << ' ';
        std::cout << "\n";
    }
    else
        std::cout << "Default : " << x << '\n';

    //std::cout << "Default : " << x << '\n';
}

template<typename ... Args> void CheckVar(Args ... args)
{
    (PrintLine(args), ...);
}

int main()
{
    int i = 100;
    float f = 3.14f;
    std::array<int, 3> a = { 1, 2, 3 };
    std::string s = "Hello";
    CheckVar(i, &i, f, &f, 10, 22.2f, 'a', a, s);

    std::system("pause");
    return 0;
}
