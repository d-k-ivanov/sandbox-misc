#include <iostream>

class Queue
{
public:
    Queue& insertInt(int i)
    {
        std::cout << "Inserting integer: " << i << '\n';
        return *this;
    }
    Queue& insertFloat(float f)
    {
        std::cout << "Inserting float: " << f << '\n';
        return *this;
    }
    Queue& insertStr(char* c)
    {
        std::cout << "Inserting string: " << c << '\n';
        return *this;
    }
};

float getInt()
{
    std::cout << "<< Integer generator >> \n";
    return 42;
}

float getFloat()
{
    std::cout << "<< Floating generator >> \n";
    return 3.14159265359f;
}

char* getStr()
{
    std::cout << "<< String generator >> \n";
    return "Hello World!";
}

int main(int argc, char* argv[])
{
    Queue fifo;
    fifo.insertStr(getStr()).insertFloat(getFloat()).insertInt(getInt());

    std::cout << '\n';
    std::system("pause");
    return 0;
}
