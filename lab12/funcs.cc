#include <iostream>
#include <math.h>
using namespace std;

//Defining functions to be created and used later.
double sum(double a, double b);
//double sqr(double x);
template<class T> T sqr(const T x) { return x*x; }
double express(const double x, const double y);

// Program Execution
int main(){
  cout << "sum is: " << sum(1.3, 2.3) << "\nsquared is: " << sqr(express(1.0,1.0)) << endl;
  double x = 3;
  cout << "x squared is: " << sqr(x) << endl;
  
  return 0;
    }


// Function Definitions
double sum(double a, double b){
  double c = a+b;
  return c;
    }

// double sqr(double x){
//   x = x*x;
//   return x;
// }

double express(double x, double y){
  double z = ((x-1.123)+1/(x+0.99)/42.0+94*y*y*y*exp(-(x+4)/6.0));
  return z;
}
