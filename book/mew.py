import numpy as np
from scipy import interpolate
import pylab as pl
x=np.linspace(0,10,11)
y=np.sin(x)
xnew=np.linspace(0,10,101)
pl.plot(x,y,'ro')
list1=['linear','nearest']
list2=[0,1,2,3]
for kind in list1:
    print(kind)
    f=interpolate.interp1d(x,y,kind=kind)
    #f是一个函数，用这个函数就可以找插值点的函数值了：
    ynew=f(xnew)
    pl.plot(xnew,ynew,label=kind)
pl.legend(loc='lower right')
pl.show()
