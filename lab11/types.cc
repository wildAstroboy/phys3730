#include <iostream>
#include <string>
#include <math.h>

using namespace std;

int main()
{
  const double pi = acos(-1.0); // since arccos(-1) is pi
  char A;
  string s = "Hello, world.";
  int i = 1;
  //double d = 1.0/pi;
  //double d = 1/2;
  double d = 1.0;
  for (int j = 0; j < 310; j++){
    d *= 10.0;
    if (j>300){
      cout << "10^" << j << "  is " << d << endl;
    }
  }
 
  
  // cout << d << endl;
  return 0;
  
}
