from matplotlib import pyplot as plt


def plot(xlist, ylist):
    plt.figure(1)  #
    plt.title("xy_scatter")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.plot(xlist, ylist, "*")
    plt.show()


if __name__ == "__main__":
    xlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ylist = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    plot(xlist, ylist)
