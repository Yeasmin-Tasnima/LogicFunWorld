#include "Factorial.h"

Factorial::Factorial()
{

}

int Factorial::calculateFactorial(const int& n)
{
	cout << "This program is calculating Factorial(" << n << ")\n";
	if (n == 0)
	{
		cout << "Factorial(" << n << ") is " << 1 << "\n";
		return 1;
	}
	int f = n * calculateFactorial(n - 1);
	cout << "Factorial(" << n << ") is " << f << "\n";
	return f;
}
