#include <iostream>
#include <string>
#include <array>

using namespace std::string_literals;

template<typename T>
struct DeductedType
{
    T str;
public:
    friend std::ostream& operator<<(std::ostream& os, const DeductedType& dt) { return os << dt.str; };
};
// custom deduction guide
DeductedType(const char *)->DeductedType<std::string>;

int main(int argc, char* argv[])
{
    //Old way
    auto oldPair1 = std::make_pair<int, std::string>(42, "hello world");
    std::pair<int, std::string> oldPair2(42, "hello world");

    //New way
    auto newPair1 = std::make_pair(42, "hello world");
    std::pair newPair2(42, "hello world"s);

    std::array arr{ 1, 2, 3, 4 };
    for (int each : arr)
        std::cout << each << " ";
    std::cout << '\n';

    DeductedType type{ "Hello World" };
    std::cout << type << '\n';


    std::system("pause");
    return 0;
}
