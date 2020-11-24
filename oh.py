from numpy import *
from pylab import *

x = linspace(0,2*pi,1000)
y = sin(x)
z = cos(x)
q = 1/x

subplot(4,2,1)
plot(x,y)

subplot(4,2,2)
plot(x,z)

subplot(4,2,3)
plot(x,y+z)

subplot(4,2,4)
plot(x,q)
show()


