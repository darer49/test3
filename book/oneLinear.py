import numpy as np

A = 0
B = 0
xlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ylist = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def get_a():
    xy_muti_sum = sum(np.multiply(np.array(xlist), np.array(ylist)))
    xy_sum_muti = sum(xlist) * sum(ylist)
    x_sqr_sum = sum(np.array(xlist) ** 2)
    x_sum_sqr = sum(xlist) ** 2
    n = len(xlist)
    return (n * xy_muti_sum - xy_sum_muti) / (n * x_sqr_sum - x_sum_sqr)


def get_b(a):
    y_sum = sum(ylist)
    x_sum = sum(xlist)
    n = len(xlist)
    return y_sum / n - a * x_sum / n


def get_yt(xt):
    return A * xt + B


def SSE():
    return sum((np.array(ylist) - get_yt(np.array(xlist))) ** 2)


def SSR():
    y_mean = np.average(ylist)
    return sum((get_yt(np.array(xlist)) - np.array([y_mean] * len(ylist))) ** 2)


def SST():
    y_mean = np.average(ylist)
    return sum((np.array(ylist) - np.array([y_mean] * len(ylist))) ** 2)


# 取值范围在[0,1]之间：r^2 越趋近于1回归方程拟合地越好
def R2():
    return SSR() / SST()


def r_relate(r_alpha):
    r = np.sqrt(R2())
    if abs(r) > r_alpha:
        return "test pass!"
    else:
        return "test fail!"


if __name__ == "__main__":
    A = get_a()
    B = get_b(A)
    xt = 12
    yt = get_yt(xt)

