import random
import pandas as pd

# 导入数据
df = pd.read_excel("pythonBook//test_data.xlsx")

'''
使用pandas
DataFrame.sample(n=None, frac=None, replace=False, weights=None, random_state=None, axis=None)
n是要抽取的行数。（例如n=20000时，抽取其中的2W行）
frac是抽取的比列。（有一些时候，我们并对具体抽取的行数不关系，我们想抽取其中的百分比，这个时候就可以选择使用frac，例如frac=0.8，就是抽取其中80%）
replace：是否为有放回抽样，取replace=True时为有放回抽样。
weights这个是每个样本的权重，具体可以看官方文档说明。
random_state这个在之前的文章已经介绍过了。
axis是选择抽取数据的行还是列。axis=0的时是抽取行，axis=1时是抽取列（也就是说axis=1时，在列中随机抽取n列，在axis=0时，在行中随机抽取n行）
'''


# 简单随机抽样:使用DataFrame自带的简单随机抽样
def simple_sampling():
    df_simple = df.sample(n=20, replace=True)
    df_simple.to_excel("pythonBook//test_data_simple.xlsx")


# 简单随机抽样2:使用随机数的抽样
def simple_sampling2():
    samp_count = 20  # 抽样数
    df_count = df.index.values  # 整体样本的index，index在dataframe中作为每一行记录的索引
    data_index = random.sample(list(df_count), samp_count)  # 从整体样本中随机选取一定数量的样本的index
    df_sample = df.iloc[data_index]  # 通过index获得样本记录
    df_sample.to_excel("pythonBook//test_data_simple2.xlsx")  # 存储到指定路径的xlsx文件


# 等距抽样
def range_sampling():
    samp_count = 20  # 抽样数
    df_range = df.shape[0] // samp_count  # 抽样的隔离距离
    data_id = [random.randint(x * df_range, (x + 1) * df_range) for x in range(samp_count)]  # 在等距内随机选择序号
    data_index = [list(df.index.values)[x] for x in data_id]  # 根据序号选择dataframe的index
    df_sample = df.iloc[data_index]  # 通过index获得样本记录
    df_sample.to_excel("pythonBook//test_data_range.xlsx")  # 存储到指定路径的xlsx文件


# 分层抽样
def layer_sampling():
    # 可以自己定义分层规则，这里我们按照年龄分为五层，每层抽取四个
    layer_num = 5  # 层数
    single_sample_num = 4  # 每一层随机抽样样本数
    # 分层，根据age将index分层
    layers = [[] for i in range(layer_num)]
    for index, row in df.iterrows():
        age = row["age"]
        if age < 20:
            layers[0].append(index)
        elif age < 40:
            layers[1].append(index)
        elif age < 60:
            layers[2].append(index)
        elif age < 80:
            layers[3].append(index)
        else:
            layers[4].append(index)

    data_index = []  # 抽样的index
    for layer in layers:
        rand_index = random.sample(layer, single_sample_num)  # 从每一层中抽样指定数量的样本
        data_index.extend(rand_index)  # 将选择的index放入data_index中
    df_sample = df.iloc[data_index]  # 通过index获得样本记录
    df_sample.to_excel("pythonBook//test_data_layer.xlsx")  # 存储到指定路径的xlsx文件


# 整群抽样
# 整群抽样具有其适用性，并不是对所有数据都适用
def whole_sampling():
    # 划分整群，利用id结尾划分
    whole_num = 5  # 整群总数
    samp_num = 2  # 抽取整群数
    layers = [[] for i in range(whole_num)]
    for index, row in df.iterrows():
        suffix = row["id"] % 10  # 除以10的余数
        if suffix < 2:
            layers[0].append(index)
        elif suffix < 4:
            layers[1].append(index)
        elif suffix < 6:
            layers[2].append(index)
        elif suffix < 8:
            layers[3].append(index)
        else:
            layers[4].append(index)
    rand_index_list = random.sample(layers, samp_num)  # 随机抽取指定数量的整群index的list的集合
    data_index = sum(rand_index_list, [])  # 合并整群的index为一个list
    df_sample = df.iloc[data_index]  # 通过index获得样本记录
    df_sample.to_excel("pythonBook//test_data_whole.xlsx")  # 存储到指定路径的xlsx文件


if __name__ == "__main__":
    print("main start!")
    simple_sampling()
    range_sampling()
    layer_sampling()
    whole_sampling()
    simple_sampling2()
