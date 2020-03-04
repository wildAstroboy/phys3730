#include <iostream>
#include <math.h>
using namespace std;

int main(){

  int n = 100000000;
  //cout << "enter n: ";
  //cin >> n;

  double answer = 0.0;
  for (int i = 1.0; i <= n; i++) {
    int sgn = (i%2) ? 1 : -1; // using modulo, alternates the signs
    answer += sgn * (1.0/i);
  }

  cout.precision(15); // sets the output to 15 digits of precision
  cout << " answer is: " << answer << ", log(2) is: " << log(2.0) << endl;
  return 0;
}
