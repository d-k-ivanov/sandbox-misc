#include <iostream>
#include <string>
#include <map>

int main()
{
    std::map<std::string, int> Users{ { "Dmitriy", 35 }, { "Ivan", 25 }, { "Alex", 38 } };
    std::cout << "Initial user map:\n";
    for (const auto&[key, value] : Users)
        std::cout << key << ", " << value << '\n';
    std::cout << "\n";

    std::cout << "Update user map #1:\n";
    std::map UsersUpdate{ Users };
    if (auto[iter, isAdded] = UsersUpdate.insert_or_assign("John", 19); !isAdded)
        std::cout << iter->first << " updated...\n";

    for (const auto&[key, value] : UsersUpdate)
        std::cout << key << ", " << value << '\n';
    std::cout << "\n";

    std::cout << "Update user map #2:\n";
    if (auto[iter, isAdded] = UsersUpdate.insert_or_assign("John", 20); !isAdded)
        std::cout << iter->first << " updated...\n";

    for (const auto&[key, value] : UsersUpdate)
        std::cout << key << ", " << value << '\n';
    std::cout << "\n";

    std::system("pause");
    return 0;
}
