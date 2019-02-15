#include <iostream>
#include <array>

struct NonMoveable
{
    NonMoveable(int x) : v(x) { std::cout << "Constructor()\n"; }
    NonMoveable(const NonMoveable&) = delete;
    NonMoveable(NonMoveable&&) = delete;
    std::array<int, 1024> arr;
    int v;
    ~NonMoveable() { std::cout << "Destructor(~)\n"; };
};

NonMoveable make(int val)
{
    if (val > 0)
        return NonMoveable(val);
    return NonMoveable(-val);
}

int main(int argc, char* argv[])
{
    {
        auto largeNonMoveableObj = make(90);
        std::cout << largeNonMoveableObj.v << '\n';
    }

    std::cout << '\n';
    std::system("pause");
    return 0;
}
