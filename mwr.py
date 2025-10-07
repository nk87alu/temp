import math
import matplotlib.pyplot as plt

v = [.6,1.2,2.4,4.8,9.6,22]
a = [2.0e-4,4.0e-4,8.0e-4,1.6e-3,3.2e-3,7.0e-3]
b = [1.15,1.18,1.20,1.23,1.26,1.30]
d = [.0025,.0027,.0030,.0033,.0036,.0040]
FObserved = [7.59342e-21,6.15189e-20,3.90419e-19,1.86758e-18,8.12656e-18,4.14506e-17]
depths = [0, 50, 100, 170, 250, 375]
i=0

def myfunc (v, a, b, d, T) :
    vHz= v * 1e9
    F = ((2*(1.3807*10**-23)*(vHz**2))/(299792458**2))*(T/(1+d*(T**(1/2))))*(1-(math.e)**(-a*T**b))
    return (F)

Temps =[]

while i <= 5:
    Tlow = 100
    Thigh = 500
    if (myfunc(v[i], a[i], b[i], d[i], Tlow) - FObserved[i]) * (myfunc(v[i], a[i], b[i], d[i], Thigh) - FObserved[i]) >= 0:
        print("NOT BRACKETED")
        break
    else:
        print("BRACKETED")
        while abs(myfunc(v[i], a[i], b[i], d[i], ((Tlow+Thigh)/2)) - FObserved[i]) > 1e-25:
            Tnext = (((Tlow+Thigh))/2)
            if (myfunc(v[i], a[i], b[i], d[i], Tlow)-FObserved[i]) * (myfunc(v[i], a[i], b[i], d[i], \
Tnext)-FObserved[i]) < 0:
                Thigh =Tnext
            else:
                Tlow = Tnext
        Temps.append((Tlow+Thigh)/2)
    i+=1
print(Temps)

plt.plot(Temps,depths)
plt.xlabel('Tempurature (K)')
plt.ylabel('Depth From 1 Bar Level (km)')
plt.grid(True)
plt.savefig('mwrTempurature.png')  
