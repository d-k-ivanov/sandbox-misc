#include <iostream>
#include <string>

// Struct to get string till delimiter
struct PrintTillW {
    std::string str;

    struct PrintIterator {
        bool operator()(std::string::iterator it) { return (*it) != '\0' && (*it) != 'W'; }
    };

    std::string::iterator begin() { return str.begin(); }

    PrintIterator end() { return PrintIterator(); }
};

// Comparison
bool operator!=(std::string::iterator it, PrintTillW::PrintIterator p) { return p(it); }

int main() {
    std::string str = "Hello World!";
    // Common Range
    for (auto c : "Hello World!") {
        if (c == 'W')
            break;
        std::cout << c;
    }
    std::cout << '\n';

    // Range with delimiter: C++17 Only
    for (auto c : PrintTillW{ "Hello World!"})
        std::cout << c;
    std::cout << '\n';

    std::system("pause");
    return 0;
}
