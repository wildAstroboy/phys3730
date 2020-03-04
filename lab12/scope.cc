#include <iostream>
#include <cmath>
using namespace std;


const double pi = acos(-1.); // uncomment this!
extern int ctrmax;


void seta(double *ap, const double b) {  // *ap is the pointer to the address
  static int ctr;
  *ap = b;
  ctr ++;
  if(ctrmax < ctr){			//If the counter maximum is less then where the counter is currently, reset the counter to countermax
	ctrmax = ctr;
  }
  return;
}

int main() 
{
  ctrmax=0;
  int i;
  double a;
   int n = 10;
   for (int i=0; i<n; i++) {
     //double a;
     seta(&a,double(i)); // &a is the meaning of address that *ap is
     if (a > 2*pi) break;
   }
   cout << "i,a: " << i << " " << a << endl;
   cout << "Pi: " << pi << endl;
   cout << "ctrmax is: " << ctrmax << endl;
   return 0;
}

int ctrmax;
