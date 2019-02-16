#include <iostream>
#include <string>

int main(int argc, char* argv[])
{
    const std::string myString = "My Hello World Wow";
    {

        const auto pos = myString.find("Hello");
        if (pos != std::string::npos)
            std::cout << pos << " Hello\n";

        const auto pos2 = myString.find("World");
        if (pos2 != std::string::npos)
            std::cout << pos2 << " World\n";
    }

    std::cout << "\n--------------------------------------------------------------------------------\n\n";
    {
        {
            const auto pos = myString.find("Hello");
            if (pos != std::string::npos)
                std::cout << pos << " Hello\n";
        }

        {
            const auto pos = myString.find("World");
            if (pos != std::string::npos)
                std::cout << pos << " World\n";
        }
    }

    std::cout << "\n--------------------------------------------------------------------------------\n\n";
    {
        if (const auto pos = myString.find("Hello"); pos != std::string::npos)
            std::cout << pos << " Hello\n";
        if (const auto pos = myString.find("World"); pos != std::string::npos)
            std::cout << pos << " World\n";
    }

    std::cout << '\n';
    std::system("pause");
    return 0;
}
