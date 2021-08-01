import numpy as np

# 冒泡排序：主要手段是多次比较多次交换位置，从而把最值交换到固定位置
def maopao(xlist):
    for i in range(len(xlist)):
        # 找出前面最大的放在最后面，因此放在后面的可以不需要再次遍历
        for j in range(len(xlist) - i - 1):
            if xlist[j] > xlist[j + 1]:
                # 相邻两两之间相互比较交换位置，小的在前，大的在后
                xlist[j], xlist[j + 1] = xlist[j + 1], xlist[j]
    return xlist


# 选择排序：主要手段是多次比较，选择出最值，放在固定位置
def xuanze(xlist):
    for i in range(len(xlist)):
        # 本次循环的最值最终所在的位置一定是i，首先假定当前在i位置的值为最值
        min_index = i
        for j in range(i + 1, len(xlist)):
            if xlist[i] > xlist[j]:
                # 如果假定的最值不符合，则定位最值此时所在的位置
                min_index = j
        # 在本次遍历中将最终确定的最值放到位置i上
        xlist[i], xlist[min_index] = xlist[min_index], xlist[i]


# 插入排序
def charu(xlist):
    for i in range(1, len(xlist)):
        # 需要进行插入的值
        insert_num = xlist[i]  # 不能直接用xlist[i]，因为之后xlist[j+1]==xlist[i],会改
        # 从0~j是进行比较的数组
        j = i - 1
        # 让insert_num和前面的j数组，从后往前依次比较，直到insert_num>=xlist[j]
        # 此时的insert_num一定小于xlist[j+1]
        """
        举例来说，insert_num<xlist[5],则令xlist[6]=xlist[5]
        下一次循环insert_num>=xlist[4]，xlist[5]的原来的值已经给了xlist[6]
        因此把insert_num的值赋予xlist[5]
        """
        while insert_num < xlist[j] and j >= 0:
            xlist[j + 1] = xlist[j]
            j -= 1
        xlist[j + 1] = insert_num

# 快速排序
def quicksort(arr):
    # 递归终止条件
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # 基准值
    # 将数组分为两部分，比基准值小的放左边，比基准值大的放右边
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


if __name__ == "__main__":
    xlist = np.random.randint(10, size=10)
    maopao(xlist)
    xuanze(xlist)
    charu(xlist)
    quicksort(xlist)