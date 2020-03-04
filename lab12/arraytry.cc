#include <iostream>
#include <math.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

double mag(double x[]) 
{
  return x[0];
}

int main() 
{

  char s[] = "hi";
  string spp = "hi again";
  cout << s << " " << spp << endl;
  cout << string(s)+" and "+spp << endl;

  double x[3] = { 0.0, 1.0, 2.0 };
  double y[2][2] = { {0,1}, {2,3} };
  x[500] = 2.0;
  cout << x[500] << endl;
  return 0;
  
  int n = 3;

  cout << "x, using indices: " << endl;
  for (size_t i=0; i<n; i++) {
    cout << x[i] << " ";
  }
  cout << endl;
  
  cout << " using pointers..." << endl;  
  double *xp = x;   // &x[0]
  for (size_t i=0; i<n; i++, xp++) {
    cout << *xp << " ";
  }
  cout << endl;
  
  vector<double> d(n);

  // set the vector
  for (size_t i=0; i<n; i++) {
    d[i] = n-x[i];
  }
  
  cout << " d, using indices:" << endl;
  for (size_t i=0; i<n; i++) {
    cout << d[i] << " ";  
  }
  cout << endl;
  
  cout << " d, using iterators:" << endl;
  for (vector<double>::iterator dp=d.begin(); dp != d.end(); ++dp) {
    cout << *dp << " ";  
  }
  cout << endl;
  
  sort(d.begin(),d.end());
  cout << "sorted vector:" << endl;
  for (size_t i=0; i<n; i++) {
    cout << d[i] << " ";
  }
  cout << endl;
  
  //  cout << d << endl;
  cout << " y (2-d) y00, y01: " << y[0][0] << " " << y[0][1] << endl;
}

