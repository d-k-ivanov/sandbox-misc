#include <iostream>

template <char Delim = 0>
class PrimitiveStringRange
{
    char const* ptr;
public:
    PrimitiveStringRange(char const* c) : ptr{ c } {}
    auto& current() { return *ptr; }
    auto  done() const { return *ptr == Delim; }
    auto  next() { ++ptr; }
};

template <class Derived>
struct RangeAdaptor : private Derived
{
    using Derived::Derived;

    struct Sentinel {};

    struct Iterator
    {
        Derived*  rng;

        friend auto operator==(Iterator it, Sentinel) { return it.rng->done(); }
        friend auto operator==(Sentinel, Iterator it) { return it.rng->done(); }

        friend auto operator!=(Iterator lhs, Sentinel rhs) { return !(lhs == rhs); }
        friend auto operator!=(Sentinel lhs, Iterator rhs) { return !(lhs == rhs); }

        auto& operator*() { return rng->current(); }
        auto& operator++() { rng->next(); return *this; }
    };

    auto begin() { return Iterator{ this }; }
    auto end() { return Sentinel{}; }
};

int main()
{
    for (auto const& c : RangeAdaptor<PrimitiveStringRange<'W'>>{ "Hello World!" })
        std::cout << c << '\n';

    std::cout << '\n';
    std::system("pause");
    return 0;
}
