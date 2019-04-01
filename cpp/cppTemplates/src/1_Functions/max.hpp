// cpp98
template<typename T>
T max1(T a, T b)
{
    return b < a ? a : b;
}

// pre cpp98
template<class T>
T max2(T a, T b)
{
    return b < a ? a : b;
}

