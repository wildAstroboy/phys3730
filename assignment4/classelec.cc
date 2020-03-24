#include <iostream>
#include <cmath>

using namespace std;

template <class T> T sqr(const T x) { return x*x; }

const double pi = acos(-1.);
const double qelec = 1.60e-19;    // C   "e"
const double melec = 9.11e-31;    // kg  "m"
const double kCoul = 8.99e9;      // N*m^2/C^2   "k"
const double c3 = pow(2.998e8,3); // N*m^2/C^2   "c3"
const double RBohr = 5.29e-11;    // m "R0" the Bohr radius

class particle
{
  public:
  double x,y,r,vx,vy,v,m;
  particle(const double mm) {
    m = mm;
  }
  double energy(const double K) {
    return 0.5*m*(v*v) + 0.5*K*r*r;
  }
  void drift(const double dt)
  {
    x += dt*vx;
    y += dt*vy;
    r = sqrt(x*x + y*y);
  }
  void kick(const double dt, const double K)
  {
    double fx = -K * qelec*qelec/(melec*x*x);
    double fy = -K * qelec*qelec/(melec*y*y);
    double ax = fx * x/r + (-2*K*(qelec*qelec)*(fx*fx)/(3*melec*v*c3)) * vx/v;
    double ay = fy * y/r + (-2*K*(qelec*qelec)*(fy*fy)/(3*melec*v*c3)) * vy/v;
    vx += dt*ax;
    vy += dt*ay;
    v = sqrt(vx*vx + vy*vy);
  }
};

int main()
{
  double mass = melec;
  double K = kCoul;
  particle p(mass);
  p.x = RBohr;
  p.y = 0.0;
  p.vx = 0.0;
  p.vy = sqrt(K*qelec*qelec/(mass*p.x));
  p.r = sqrt(p.x*p.x+p.y+p.y);
  p.v = sqrt(p.vx*p.vx+p.vy*p.vy);
  double T = 2 * pi * RBohr * sqrt(RBohr*mass/(kCoul*qelec*qelec));
  int nsteps_per_orbit = 200;
  double dt = T/nsteps_per_orbit;
  double tmax = 10*T;
  double t = 0.0;
  double t_half = 0.0;

  cout  << "Starting r: " << p.r << ", v: " << p.v << ", Energy: " << p.energy(K) << endl;
  while (t < tmax) {
    if (p.r >= 0.5*RBohr) {
    p.drift(0.5*dt);
    p.kick(dt,K);
    p.drift(0.5*dt);
    t += dt;
    cout << "r: " << p.r << ", " << "v: " << p.v << ", Energy: " << p.energy(K) << endl;
    }
    t_half = t;
    break;
  }
  cout  << "Ending r: " << p.r << ", t_half: " << t_half << ", Energy: " << p.energy(K) << endl;
}
