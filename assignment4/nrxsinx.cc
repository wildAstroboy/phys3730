#include <iostream>
#include <cmath>

using namespace std;

// find the root of f(x) = x*sin(x)-c

double errtol = 1e-6;
double delx, xnext, xlast = 1;
double x = 1;
double xroot;
const double c = 0.1;

//Our f(x)
double f(double a){
  return a * sin(a) - c;
}
//Our f'(x)
double f_prime(double a){
  return sin(a) + a*cos(a);
}

int main(){
  do
  { //Newton-Raphson Algorithm
    //Find xroot using starting x position which was guessed.
    xroot = x - f(x)/f_prime(x);
    cout << "xroot is: " << xroot << " and delx is: " << delx << endl;
    //Update xlast with current x used.
    xlast = x;
    //set the next guess to the xroot.
    x = xroot;
    //check to see if delx is within our error tolerance, if so, break out of do-while loop.
    delx = xroot - xlast;
  } while (fabs(delx)>errtol);
}
