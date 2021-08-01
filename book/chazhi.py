import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate


# 定义函数
def func(x, y):
    return (x + y) * np.exp(-5 * (x ** 2 + y ** 2))


x, y = np.mgrid[-1:1:8j, -1:1:8j]  # 生成8*8的矩阵
# a:b:cj，cj表示步长，为复数表示点数，在区间[a,b]中取三个值
z = func(x, y)
# x,y,z为示例值，采用这些值进行插值
func = interpolate.interp2d(x, y, z, kind='cubic')

xnew = np.linspace(-1, 1, 100)
ynew = np.linspace(-1, 1, 100)
znew = func(xnew, ynew)  # xnew, ynew是一维的，输出znew是二维的
# xnew,ynew,znew为插值完成的函数中取得的值
xnew, ynew = np.mgrid[-1:1:100j, -1:1:100j]  # 统一变成二维，便于下一步画图

# 绘图
ax = plt.subplot(111, projection='3d')
ax.plot_surface(xnew, ynew, znew)
ax.scatter(x, y, z, c='r', marker='^')
plt.show()
