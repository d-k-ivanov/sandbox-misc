/*	Приведите 5 конструкций языка С++, смысл которых не определен.
 *	Приведите 5 конструкций языка С++, смысл которых зависит от реализации */

#include <iostream>

	int f() {
		std::cout << "F" << std::endl;
		return 3;
	}
 
	int g() {
		std::cout << "G" << std::endl;
		return 4;
	}
 
	int h(int i, int j) {
		return i + j;
	}

int main()
{
	

	// undefined behavior
	int i = 0;
	i = i++ + ++i;
	//printf("%d\n", i); // 3
	std::cout << i << std::endl;

	i = 1;
	i = (i++);
	//printf("%d\n", i); // 2 Should be 1, no ?
	std::cout << i << std::endl;

	volatile int u = 0;
	u = u++ + ++u;
	//printf("%d\n", u); // 1
	std::cout << u << std::endl;

	u = 1;
	u = (u++);
	//printf("%d\n", u); // 2 Should also be one, no ?
	std::cout << u << std::endl;

	register int v = 0;
	v = v++ + ++v;
	//printf("%d\n", v); // 3 (Should be the same as u ?)	
	std::cout << v << std::endl;

	//char* p = "hello!\n";   // yes I know, deprecated conversion
    //p[0] = 'y';
    //p[5] = 'w';
    //std::cout << p << std::endl;
	
	i = 5;
	i = ++i + ++i;
	std::cout << i << std::endl;
	
	
	char *p = "wikipedia"; // ill-formed C++11, deprecated C++98/C++03
	p[0] = 'W'; // undefined behavior
	
	int x = 1;
	return x / 0; // undefined behavior	
	
	int arr[4] = {0, 1, 2, 3};
	int *p = arr + 5;  // undefined behavior
	
	int f()
	{	
	}  /* undefined behavior: Reaching the end of a value-returning function (other than main()) without a return statement */

	
	//implementation-defined behavior
	
	std::cout << h(f(), g()) << std::endl;
	
	int a = 0;
	int b = 0;
	return &a < &b; /* unspecified behavior in C++, undefined in C */
	
	printf("%d %d\n", ++n, power(2, n));    /* WRONG */
	

	std::cout << "END\n";
	return 0;
}
