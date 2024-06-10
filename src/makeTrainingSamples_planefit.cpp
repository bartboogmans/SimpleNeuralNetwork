#include <iostream>
#include <cmath>
#include <cstdlib>

using namespace std;

int main()
{
	// Random training sets for a plane fit -- two inputs and one output
	// if sqrt(x,y) < pi, output (cos(x)+1)/2
	// else output 0
	double pi = 3.14159265358979323846;
	double xlim = 6.0;
	double ylim = 6.0;
	int numsamples = 90000;

	cout << "topology: 2 6 6 1" << endl;

	for(int i = numsamples; i >= 0; --i)
	{
		int n1 = (int)(2.0 * rand() / double(RAND_MAX));
		int n2 = (int)(2.0 * rand() / double(RAND_MAX));

		double x = xlim * (2.0 * rand() / double(RAND_MAX) - 1.0);
		double y = ylim * (2.0 * rand() / double(RAND_MAX) - 1.0);

		double r = sqrt(x*x + y*y);
		if (r < pi)
		{
			cout << "in: " << x << " " << y << endl;
			cout << "out: " << (cos(r) + 1.0) / 2.0 << endl;
		}
		else
		{
			cout << "in: " << x << " " << y << endl;
			cout << "out: " << 0.0 << endl;
		}
	}
}
