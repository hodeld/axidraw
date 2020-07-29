import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

from plotdot.plotLog.figures import square, line_trace


def plot_lines(lines, autoscale=True):
    figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k',)
    if type(autoscale) == tuple:
        plt.xlim(0, autoscale[0])
        plt.ylim(0, autoscale[1])
        line_width = 10 / autoscale[0]
    else:
        line_width = 0.8
    plt_opts = {'color': 'black',
                'linewidth': line_width}
    for (x, y) in lines:
        plt.plot(x, y, **plt_opts)
        plt.grid(True)


    plt.show()


def transpose_lines(lines):
    lines_c = lines.copy()
    for i, l in enumerate(lines_c):
        l_arr = np.array(l)
        l_t = l_arr.transpose()
        lines[i] = l_t


def squares_plot():
    width = 100
    height = 100
    cx = width / 2
    cy = height / 2
    lines = []
    for i in range(1,4):
        margin = 0.25
        size = i + 1
        lines.append(square(cx, cy, size))
        lines.append(square(cx, cy, size + margin))
    transpose_lines(lines)
    plot_lines(lines)


def linetraces():
    lines = line_trace(x0=3, xw=10, xh=0, y0=1, yw=3, yh=18)
    #lines = line_trace()
    transpose_lines(lines)
    autoscale = (20, 20)
    autoscale = True
    #plot_lines(lines, autoscale)
    return lines


def inter_plot():  # no plot_run
    lines = []
    plt_opts = {'color': 'black',
                'linewidth': 1}
    for i in range(1, 50):
        y_arr = [1 + i, 2 * i, 3]
        x_arr = [3 + 1.5*i, 4, 6 * i/2]
        lines.append((x_arr, y_arr))
        plt.plot(x_arr, y_arr, **plt_opts)     # k=black
    plt.show()