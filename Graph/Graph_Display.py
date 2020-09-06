import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)


def plot_results(x_1: list, y_1: list,
                 x_2: list, y_2: list,
                 x_3: list, y_3: list):
    plt.plot(x_1, y_1)
    plt.plot(x_2, y_2)
    plt.grid()
    plt.show()


def graph_append(name_file, info_vab):

    file = open(str(name_file), "a")
    file.write(info_vab)

    file.close()


def graph_show():
    """
    Use to show on the screen the graphs
    """
    graph_data = open('Graph\Population.txt', 'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    # looping for each lines
    for line in lines:
        if len(line)>1:
            x, y = line.split(',')

            xs.append(float(x))
            ys.append(float(y))
    ax1 .clear()
    ax1.plot(xs, ys)

