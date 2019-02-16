#include <iostream>
#include <string>

class UserEntry {
public:
    UserEntry(std::string name, unsigned age) {
        this->name = name;
        this->age = age;
    }
    std::string GetName() const { return name; }
    unsigned GetAge() const { return age; }
private:
    std::string name;
    unsigned age{ 0 };
    size_t cacheEntry{ 0 }; // not exposed
};

template <size_t I> auto get(const UserEntry& u) {
    // explicit
    // template<> string get<0>(const UserEntry &u) { return u.GetName(); }
    // template<> unsigned get<1>(const UserEntry &u) { return u.GetAge(); }
    // with if constexpr:
    if constexpr (I == 0) return u.GetName();
    else if constexpr (I == 1) return u.GetAge();
}
namespace std {
    template <> struct tuple_size<UserEntry> : std::integral_constant<size_t, 2> { };
    template <> struct tuple_element<0, UserEntry> { using type = std::string; };
    template <> struct tuple_element<1, UserEntry> { using type = unsigned; };
}



int main(int argc, char* argv[])
{
    UserEntry u("Dima", 35);
    auto[name, age] = u; // read access
    std::cout << name << ", " << age << '\n';

    std::cout << '\n';
    std::system("pause");
    return 0;
}
