import numpy as np
import matplotlib.pyplot as plt

# 使用到了冒泡排序法
def maopao(xlist):
    for i in range(len(xlist)):
        # 找出前面最大的放在最后面，因此放在后面的可以不需要再次遍历
        for j in range(len(xlist) - i - 1):
            if xlist[j] > xlist[j + 1]:
                # 相邻两两之间相互比较交换位置，小的在前，大的在后
                xlist[j], xlist[j + 1] = xlist[j + 1], xlist[j]
    return xlist

# 限幅滤波法
def range_filter(arr, fudu):  # fudu为设定的限制幅度
    for i in range(1, len(arr)):
        if abs(arr[i] - arr[i - 1]) > fudu:
            arr[i] = arr[i - 1]
    return arr

# 中位值滤波法：
def mid_filter(arr, times):  # times为每次抽样的个数
    new_arr = np.zeros(len(arr))
    for i in range(len(arr)):
        rand_list = np.random.randint(len(arr), size=times)  # 随机从总体arr中抽取times个样本
        rand_num = maopao([arr[x] for x in rand_list])
        mid = rand_num[int((times - 1) / 2)]  # 样本的中位数为本次选择的有效值
        new_arr[i] = mid  # 存放到new_arr中
    return new_arr  # new_arr为最后的滤波结果

# 算术平均滤波法
def mean_filter(arr, mean_num):  # mean_num为每次取样进行算术平均的样本个数
    new_arr = np.zeros(len(arr))
    for i in range(len(arr)):
        rand_list = np.random.randint(len(arr), size=mean_num)
        new_arr[i] = np.array([arr[x] for x in rand_list]).mean()  # 进行算数平均
    return new_arr


# 递推平均滤波法
def recurrence_filter(arr, mean_num):  # 基于算数平均，mean_num为算术平均的样本数
    new_arr = np.zeros(len(arr))
    rand_list = np.random.randint(len(arr), size=mean_num)  # 取样出mean_num长度的队列
    for i in range(len(arr)):
        last_rand = np.random.randint(len(arr), size=1)[0]  # 放入队尾的样本数据
        rand_list = np.append(rand_list[1:], last_rand)  # 去除队首的数据，加入队尾的数据
        new_arr[i] = np.array([arr[x] for x in rand_list]).mean()  # 做算数平均
    return new_arr


# 中位值平均滤波法：中位值滤波法+算术平均滤波法
def mid_mean_filter(arr, times):  # times为取样次数
    new_arr = np.zeros(len(arr))
    for i in range(len(arr)):
        rand_list = np.random.randint(len(arr), size=times)
        rand_num = maopao([arr[x] for x in rand_list])[1:-1]  # 去掉排序之后的最大最小值
        mean = np.array(rand_num).mean()  # 取算术平均
        new_arr[i] = mean
    return new_arr


# 限幅平均滤波法：限幅滤波法+递推平均滤波法，先后执行
def limit_range_filter(arr, therange, mean_num):
    arr = range_filter(arr, therange)
    return recurrence_filter(arr, mean_num)


# 一阶滞后滤波法 以某一种滤波法为基础，结合滤波数据与实际数据，按照加权平均获得最后的抽样值
def one_lay_filter(arr, mean_num):
    weight = round(np.random.random(), 3)  # 滤波结果所占权重，可以自行设定
    # 以算术平均滤波为例
    new_arr = np.zeros(len(arr))
    for i in range(len(arr)):
        rand_list = np.random.randint(len(arr), size=mean_num)
        if i > 0:
            new_arr[i] = new_arr[i - 1] * weight + (1 - weight) * np.array([arr[x] for x in rand_list]).mean()  # 加权平均
        else:  # i=0，即一开始时没有上次滤波结果，直接取算术平均
            new_arr[i] = np.array([arr[x] for x in rand_list]).mean()
    return new_arr


# 加权递推平均滤波法：对递推平均滤波法的改进
# 不同时刻的权重通常是越接近现时刻越大
def weight_recurrence_filter(arr, mean_num):
    new_arr = np.zeros(len(arr))
    new_arr[0:mean_num] = arr[0:mean_num]
    weight = np.array(range(1, mean_num + 1))  # 假设权重与取样时刻的关系是线性
    weight = weight / weight.sum()  # 获得分配的加权权重
    for i in range(mean_num, len(arr)):
        new_arr[i] = sum(np.multiply(np.array(arr[i - mean_num:i]), weight))
    return new_arr


# 消抖滤波法设置一个滤波计数器  将每次采样值与当前有效值比较：
# 如果采样值＝当前有效值，则计数器清零
# 如果采样值<>当前有效值，则计数器+1，并判断计数器是否>=上限N(溢出)
# 如果计数器溢出,则将本次值替换当前有效值,并清计数器
def shakeoff_filter(arr, limit):  # limit代表计数器上限
    shake_value = arr[0]  # 当前有效值取第一个样本值
    shake_num = 0  # 计数器值，初始化为0
    for i, v in enumerate(arr):  # 对arr遍历，i代表从0开始的数组下标，v代表值
        if v != shake_value:  # 如果当前值与当前有效值不一致
            shake_num += 1
            if shake_num >= limit:  # 当计数器达到上限
                arr[i] = shake_value
                shake_num = 0
    return arr


# 限幅消抖滤波法：限幅滤波法”+“消抖滤波法”先后执行
def range_shakeoff_filter(arr, therange,limit):
    arr = range_filter(arr,therange)
    return shakeoff_filter(arr,limit)


if __name__ == "__main__":
    # arr = list(np.random.randint(10, size=100) + 20)
    from book.data import test_data
    plt.rcParams['font.sans-serif']=['SimHei']  # 用来正常显示中文标签
    plt.rcParams['figure.figsize'] = (12.0, 6.0)  # 设置figure_size尺寸
    plt.ylim(0, 35)
    arr = test_data
    plt.plot(arr,label="滤波前")

    new_arr = shakeoff_filter(arr,3)

    plt.plot(new_arr,label="滤波后")
    print(new_arr)
    plt.legend(loc=0)  # 图例位置自动
    plt.title("消抖滤波法")
    plt.show()

