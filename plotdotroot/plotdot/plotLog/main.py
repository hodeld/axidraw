from pyaxidraw import axidraw
import os
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np

from plotdot.plotLog.figures import square

prjct_root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


def svg_plot():
    """

    0 - Do not render previews
    1 - Render pen-down movement only
    2 - Render pen-up movement only
    3 - Render all movement, both pen-up and pen-down [DEFAULT]

    :return:
    """
    ad = axidraw.AxiDraw()
    file_name = 'logoetiki' + '.svg'  # 'logoetiki.svg' 'AxiDraw_trivial'

    f_path = os.path.join(prjct_root_path, file_name)
    ad.plot_setup(f_path)
    ad.options.rendering = 3
    ad.options.preview = True

    ad.options.report_time = True
    ad.options.pen_pos_down = 40
    ad.options.pen_pos_up = 30
    output_svg = ad.plot_run(True)
    outp_name = 'gensvg.svg'
    save_file(output_svg, outp_name)
    print("{0}".format(ad.pt_estimate))


def save_file(output_svg, n):
    outp_name = n
    save_f = os.path.join(prjct_root_path, outp_name)
    with open(save_f, 'w') as f:
        f.write(output_svg)


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


def plot_lines(lines):
    figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
    plt_opts = {'color': 'black',
                'linewidth': 1}
    for (x, y) in lines:
        plt.plot(x, y, **plt_opts)
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


if __name__ == '__main__':
    #svg_plot()
    squares_plot()

