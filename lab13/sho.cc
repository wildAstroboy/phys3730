#include <iostream>
#include <cmath>

using namespace std;

const double pi = acos(-1.0);
template<class T> T sqr(const T x) {return x*x;}

class particle {
	public:
		double x, v, m, k;
		void drift (const double dt){
			x += dt*v;
		}
		void kick (const double dt, const double k){
			v += dt*(-k/m*x);
			v -= 0.1*dt*v;
		}
		double energy(const double k) {
			return 0.5*m*v*v + 0.5*k*x*x;
		}
};

int main() {

	particle p;
	p.x = 1.0;
	p.v = 0.0;
	p.m = 1.0;

	double k = 1.0;
	double T = 2*pi*sqrt(p.m/k);

	cout << "# period T is: " << T << endl;
	cout << "# starting x,v: " << p.x << "   " << p.v << endl;
	cout << " Starting energy: " << p.energy(k) << endl;

	double dt = T/100;
	double t = 0.0;

	while(t <= 10*T) {
		if(true) {
			p.drift(0.5*dt);
			p.kick(dt,k);
			p.drift(0.5*dt);
		} else {
			double a = -k/p.m*p.x;
			p.x += dt*p.v;
			p.v += dt*a;
		}

		t = t + dt;
		cout << t << "   " << p.x << "   " << p.v << "   " << p.energy(k) << endl;
	}

	cout << "# final x,v: " << p.x << "   " << p.v << endl;
	cout << " final energy: " << p.energy(k) << endl;

	return 0;

}




/* NOTES

LOOP:

x_i+1 = x_i + del(t)*v_i

v_i+1 = v_i + del(t)*a_i where a_i = -(k/m)x_i

if we know velocity inbetween an interval:

x_i+1 = x_i + del(t)*v_i+(1/2)

v_i+(3/2) = v_i+(1/2) + del(t)*a_i+1

v_i+(1/2) = v_i-(1/2) + del(t)*a_i

You can go forward and backwards in the algo so it helps reduce the drift. SIMPLECTIC INTEGRATOR.

----------------

a = -(k*x)/m

w = sqrt(k/m)

d^2x/dt^2 = -(k/x)m

dx/dt = v --> del(x)/del(t) = v

del(x) = del(t)*v = (x_1 - x_0)

x_1 = x_0 + del(t)*v_0

del(v)/del(t) = a = -(k/m)x

v_1 = v_0 + del(t)*a_0

where a_0 = -(k/m)x_0

T = 2*pi * sqrt(m/k)

t needs to be as small as possible or the computer wont track with the equations well.



*/

