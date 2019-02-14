#include <iostream>

template <char Delim = 0>
struct StringSentinel {};

struct StringIterator
{
    char const* ptr = nullptr;

    template <char Delim>
    friend auto operator==(StringIterator lhs, StringSentinel<Delim> rhs) {
        return *lhs.ptr == Delim;
    }

    template <char Delim>
    friend auto operator==(StringSentinel<Delim> lhs, StringIterator rhs) {
        return rhs == lhs;
    }

    template <char Delim>
    friend auto operator!=(StringIterator lhs, StringSentinel<Delim> rhs) {
        return !(lhs == rhs);
    }

    template <char Delim>
    friend auto operator!=(StringSentinel<Delim> lhs, StringIterator rhs) {
        return !(lhs == rhs);
    }

    auto& operator*() { return *ptr; }
    auto& operator++() { ++ptr; return *this; }
};

template <char Delim = 0>
class StringRange
{
    StringIterator it;
public:
    StringRange(char const* ptr) : it{ ptr } {}
    auto begin() { return it; }
    auto end() { return StringSentinel<Delim>{}; }
};

int main()
{
    for (auto const& c : StringRange<'W'>{ "Hello World!" })
        std::cout << c << '\n';

    std::cout << '\n';
    std::system("pause");
    return 0;
}
