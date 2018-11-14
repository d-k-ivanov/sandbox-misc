#include <iostream>
using namespace std;

bool aaa(bool a, bool b);

int main() {
	bool p,q;
	cout << "Enter P (0 or 1)";
	cin >> p;
	cout << "Enter Q (0 or 1)";
	cin >> q;

	cout << "P and Q: " << (p && q) << "\n";
	cout << "P or Q: " << (p || q) << "\n";
//	cout << "P xor Q: " << aaa(p,q) << "\n";
	cout << "P xor Q: " << (p ^ q) << "\n";

	return 0;

}

bool aaa(bool a, bool b) {
	return (a || b) && !(a && b);
}
