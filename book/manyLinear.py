import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

X= np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]])
y = np.array([sum(x) for x in X])

# 多元线性回归分析，其中X和Y分别为自变量数据集和因变量数据集
def muti_linear_regre(X, Y):
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=2, random_state=1)
    reg = LinearRegression(copy_X=True)
    reg.fit(X_train, y_train)
    print(reg.predict(X_test))  # 利用训练的神经网络进行预测/检验


if __name__ == "__main__":
    muti_linear_regre(X, y)
