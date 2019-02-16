#include <iostream>
#include <random>
#include <string>

struct TestClass1
{
    std::string name;
    //inline static const int val = 1024;
    inline static int val;

    TestClass1(std::string name) { this->name = name; };

    void setVal(int i) { this->val = i; };
};

int main(int argc, char* argv[])
{
    TestClass1 cl1 = TestClass1("class 1");
    cl1.setVal(1024);
    TestClass1 cl2 = TestClass1("class 2");

    std::cout << "Class1: " << cl1.name << " Value: " << cl1.val << '\n';
    std::cout << "Class2: " << cl2.name << " Value: " << cl2.val << '\n';

    std::cout << '\n';
    std::system("pause");
    return 0;
}
