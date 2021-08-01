import numpy as np

x1list = [1, 2, 3, 4]
x2list = [6, 5, 6, 8]
ylist = [7, 8, 9, 10]

y_mean = np.average(ylist)
x1_mean = np.average(x1list)
x2_mean = np.average(x2list)
yilist = np.array(ylist) - np.array([y_mean] * len(ylist))
x1ilist = np.array(x1list) - np.array([x1_mean] * len(x1list))
x2ilist = np.array(x2list) - np.array([x2_mean] * len(x2list))

yx1_muti_sum = sum(np.multiply(yilist, x1ilist))
x2_sqr_sum = sum(np.array(x2ilist) ** 2)
yx2_muti_sum = sum(np.multiply(yilist, x2ilist))
x1x2_muti_sum = sum(np.multiply(x1ilist, x2ilist))
x1_sqr_sum = sum(np.array(x1ilist) ** 2)

B1 = (yx1_muti_sum * x2_sqr_sum - yx2_muti_sum * x1x2_muti_sum) / (x1_sqr_sum * x2_sqr_sum - x1x2_muti_sum ** 2)
B2 = (yx2_muti_sum * x1_sqr_sum - yx1_muti_sum * x1x2_muti_sum) / (x1_sqr_sum * x2_sqr_sum - x1x2_muti_sum ** 2)
B0 = y_mean - B1 * x1_mean - B2 * x2_mean

e_sqr_sum = sum(np.array(yilist) ** 2) - B1 * sum(np.multiply(yilist, x1ilist)) - B2 * sum(np.multiply(yilist, x2ilist))
u = e_sqr_sum / (len(ylist) - 3)

if __name__ == "__main__":
    print("B0是：{:.3f}\nB1是{:.3f}\nB2是：{:.3f}\nu是：{:.3f}".format(B0, B2, B2, u))
