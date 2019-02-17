#include <iostream>
#include <string>

// Old way
namespace old_A {
    namespace old_B {
        namespace old_C {
            std::string hello_str = "OLD Hello world!\n";
        }
    }
}

namespace new_A::new_B::new_C {
            std::string hello_str = "NEW Hello world!\n";
}


int main(int argc, char* argv[])
{
    std::cout << old_A::old_B::old_C::hello_str;
    std::cout << new_A::new_B::new_C::hello_str;

    std::cout << '\n';
    std::system("pause");
    return 0;
}
