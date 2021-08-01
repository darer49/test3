import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
plt.rcParams['font.sans-serif']=['Fangsong']#如果要显示中文字体，则在此处设为：SimHei
plt.rcParams['axes.unicode_minus']=False#显示负号
x = np.array([3,5,7,9,11,13,15,17,19,21])
A = np.array([0.9708, 0.6429, 1, 0.8333, 0.8841, 0.5867, 0.9352, 0.8000, 0.9359, 0.9405])
B= np.array([0.9708, 0.6558, 1, 0.8095, 0.8913, 0.5950, 0.9352, 0.8000, 0.9359, 0.9419])
C=np.array([0.9657, 0.6688, 0.9855, 0.7881, 0.8667, 0.5952, 0.9361, 0.7848, 0.9244, 0.9221])
D=np.array([0.9664, 0.6701, 0.9884, 0.7929, 0.8790, 0.6072, 0.9352, 0.7920, 0.9170, 0.9254])
#label在图示(legend)中显示。若为数学公式，则最好在字符串前后添加"$"符号
plt.figure(figsize=(10,5))
ax = plt.gca()
plt.plot(x,A,color="black",label="A 算法",linewidth=1.5)
plt.plot(x,B,"k--",label="B 算法",linewidth=1.5)
plt.plot(x,C,color="red",label="C 算法",linewidth=1.5)
plt.plot(x,D,"r--",label="D 算法",linewidth=1.5)
group_labels=['1','2','3','4','5',' 6','7','8','9','10'] #x轴刻度的标识
plt.xticks(x,group_labels,fontsize=12,fontweight='bold') #默认字体大小为10
plt.yticks(fontsize=12,fontweight='bold')
# plt.title("样例",fontsize=12,fontweight='bold') #默认字体大小为12
plt.xlabel("数据集",fontsize=13,fontweight='bold')
plt.ylabel("精度",fontsize=13,fontweight='bold')
plt.xlim(3,21) #设置x轴的范围
 #显示各曲线的图例
plt.legend(loc=0, numpoints=1)
leg = plt.gca().get_legend()
ltext = leg.get_texts()
plt.setp(ltext, fontsize=12,fontweight='bold') #设置图例字体的大小和粗细
#解决中文显示问题，但最好不要用中文
plt.rcParams['font.sans-serif']=['Fangsong']
plt.rcParams['axes.unicode_minus'] = False
plt.show()
xb=np.vstack((A,B,C,D))   #vstack是使得列方向上叠加
test=pd.DataFrame(xb)
print('数组矩阵为：')
print(test)
# 简单相关系数计算
print('各变量之间的简单相关系数为：')
print(np.corrcoef(xb))
# 偏相关系数计算
# python中无模块可计算偏相关系数 ，自定义一个偏相关系数函数
def partial_corr(x, y, partial=[]):
    # x，y分别为考察相关关系的变量，partial为控制变量
    xy, xyp = stats.pearsonr(x, y)
    xp, xpp = stats.pearsonr(x, partial)
    yp, ypp = stats.pearsonr(y, partial)
    n = len(x)
    df = n - 3
    r = (xy - xp * yp) / (np.sqrt(1 - xp * xp) * np.sqrt(1 - yp * yp))
    if abs(r) == 1.0:
        prob = 0.0
    else:
        t = (r * np.sqrt(df)) / np.sqrt(1 - r * r)
        prob = (1 - stats.t.cdf(abs(t), df)) ** 2
    return r, prob
pcorrelation = []
# 选定数组D为控制变量，计算偏相关系数
for i in test[[0, 1]].columns:
    pcorrelation.append(partial_corr(test[i], test[2], partial=test[3]))
print('偏相关系数为：')
print(pcorrelation)
