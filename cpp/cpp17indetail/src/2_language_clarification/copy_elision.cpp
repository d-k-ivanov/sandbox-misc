#include <iostream>

struct TestElision
{
    TestElision() { std::cout << "TestElision()\n"; };
    TestElision(const TestElision&) { std::cout << "TestElision(&)\n"; };
    TestElision(TestElision&&) { std::cout << "TestElision(&&)\n"; };
    ~TestElision() { std::cout << "TestElision(~)\n"; };
};

TestElision Create()
{
    return TestElision();
}

int main(int argc, char* argv[])
{
    std::cout << "--------------------------------------------------\n\n";
    auto te1 = TestElision();
    std::cout << "--------------------------------------------------\n\n";
    auto te2 = Create();
    std::cout << "\n--------------------------------------------------\n";

    std::cout << '\n';
    std::system("pause");
    return 0;
}
