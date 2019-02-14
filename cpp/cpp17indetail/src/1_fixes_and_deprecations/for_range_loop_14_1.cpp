#include <iostream>

template <char Delim = 0>
struct StringIterator
{
    char const* ptr = nullptr;

    friend auto operator==(StringIterator lhs, StringIterator rhs) {
        return lhs.ptr ? (rhs.ptr || (*lhs.ptr == Delim)) : (!rhs.ptr || (*rhs.ptr == Delim));
    }

    friend auto operator!=(StringIterator lhs, StringIterator rhs) {
        return !(lhs == rhs);
    }

    auto& operator*() { return *ptr; }
    auto& operator++() { ++ptr; return *this; }
};

template <char Delim = 0>
class StringRange
{
    StringIterator<Delim> it;
public:
    StringRange(char const* ptr) : it{ ptr } {}
    auto begin() { return it; }
    auto end() { return StringIterator<Delim>{}; }
};

int main()
{
    for (auto const& c : StringRange<'W'>{ "Hello World!" })
        std::cout << c << '\n';

    std::cout << '\n';
    std::system("pause");
    return 0;
}
