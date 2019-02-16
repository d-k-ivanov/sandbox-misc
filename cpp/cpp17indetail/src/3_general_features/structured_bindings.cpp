#include <iostream>
#include <random>
#include <string>
#include <map>
#include <set>

class Queue
{
public:
    std::pair<int, bool> insertInt(int i)
    {
        std::cout << "Inserting integer: " << i << '\n';
        std::pair<int, bool> ret;
        ret.first = i;

        std::mt19937 gen(std::random_device{}());
        bool rnd_bool = std::uniform_int_distribution<>{ 0, 1 }(gen);
        // std::cout << "rnd_bool: " << rnd_bool << '\n';
        ret.second = rnd_bool;

        return ret;
    }
};

template<typename T1, typename T2>
void print_pair(T1 fst, T2 scnd) {
    std::cout << "First: " << fst << " Second: " << scnd << '\n';

};


int main(int argc, char* argv[])
{
    {
        Queue q;
        auto[ins, inserted] = q.insertInt(10);
        if (inserted)
            std::cout << "Inserted value: " << ins << '\n';
        else
            std::cout << "Insertion failed!\n";
    }

    std::cout << "\n--------------------------------------------------------------------------------\n\n";
    {

        std::set<int> intSet;
        std::set<int>::iterator intSetIter;
        bool intSetInsertSuccess;
        int pos = 0;
        for (int i : {1, 2, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9, 9, 9, 9}) {
            std::tie(intSetIter, intSetInsertSuccess) = intSet.insert(i); // << Here the difference
            if (intSetInsertSuccess)
                std::cout << "Iserted value: " << pos << ": " << i << '\n';
            else
                std::cout << "Existed value: " << pos << ": "<< i << '\n';
            pos++;
        }
    }

    std::cout << "\n--------------------------------------------------------------------------------\n\n";
    {
        std::set<int> intSet;
        std::set<int>::iterator intSetIter;
        bool intSetInsertSuccess;
        int pos = 0;
        for (int i : {1, 2, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9, 9, 9, 9}) {
            auto[intSetIter, intSetInsertSuccess] = intSet.insert(i); // << Here the difference
            if (intSetInsertSuccess)
                std::cout << "Iserted value: " << pos << ": " << i << '\n';
            else
                std::cout << "Existed value: " << pos << ": " << i << '\n';
            pos++;
        }
    }

    std::cout << "\n--------------------------------------------------------------------------------\n\n";
    {
        std::pair a(5, 1.111f);
        std::cout << "First: " << a.first << " Second: " << a.second << '\n';
        const auto[x, y] = a;
        print_pair(x, y);
    }

    std::cout << "\n--------------------------------------------------------------------------------\n\n";
    {
        std::pair a(5, 1.111f);
        auto&[x, y] = a;
        print_pair(x, y);
        x = 10;
        print_pair(x, y);
    }

    std::cout << "\n--------------------------------------------------------------------------------\n\n";
    {
        std::pair a(5, 1.111f);
        auto&&[x, y] = a;
        print_pair(x, y);
    }

    std::cout << "\n--------------------------------------------------------------------------------\n\n";
    {
        struct Point {
            double x;
            double y;
            Point GetStartPoint() { return { 0.0, 0.0 }; }
        };
        Point p;
        auto[x, y] = p.GetStartPoint();
        print_pair(x, y);
    }

    {
        // constexpr auto[x, y] = std::pair(0, 0); -- This is the limitation
    }

    std::cout << "\n--------------------------------------------------------------------------------\n\n";
    {
        const std::map<std::string, int> mapCityPopulation{
            { "Tokyo", 38'001'000 },
            { "Delhi", 25'703'168 },
            { "Shanghai", 23'740'778 },
            { "Sao Paulo", 21'066'245 },
            { "Mumbai", 21'042'538 },
            { "Mexico City", 20'998'543 },
            { "Beijing", 20'383'994 },
            { "Osaka", 20'237'645 },
            { "Cairo", 18'771'769 }
        };
        for (auto&[city, population] : mapCityPopulation)
            std::cout << city << ": " << population << '\n';

    }

    std::cout << '\n';
    std::system("pause");
    return 0;
}
