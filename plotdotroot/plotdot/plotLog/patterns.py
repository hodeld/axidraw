import numpy as np
import random
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

from plotdot.plotLog.figures import square, line_trace, add_points, line_trace_from_p
from plotdot.svgDraw.main import group_elements, polylines
from plotdot.svgDraw.transform import translate, transform_allmeths


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


def line_by_line(dwg, lines, scale_f):
    (x_transl, y_transl) = 0, 0
    skew_angle = 0
    scale_t = [1, 1]
    transl_t = [0, 0]
    skew_x_t = [0, None]
    skew_y_t = [0, None]
    rotate_t = [0, None]
    trans_dic = {1: scale_t,
                 2: transl_t,
                 3: skew_x_t,
                 4: skew_y_t,
                 5: rotate_t,
                 }
    scale_steps_x = -1 #.1 # .1 #2
    scale_steps_y = .1
    shift = [0, 0]
    def make_line_trace():
        line_n = add_points(l)
        lines_traced, shift = line_trace_from_p(line_n, density=1)
        #plines = polylines(dwg, lines_traced)
        plines = polylines(dwg, lines_traced, trans_dic)
        g_pline = group_elements(dwg, plines, class_n='polyline')
        return g_pline, shift

    groups = []
    rand_int = random.randint(1, 5)
    rand_ints = [i * rand_int for i in [1, 3, 4, 5, 8, 11]]
    #rand_ints = [5]
    for k, l in enumerate(lines):
        x_scale = k * scale_steps_x
        y_scale = k * scale_steps_y
        #scale_t[0] = 1 + x_scale
        scale_t[1] = 1 + y_scale
        #skew_x_t[0] = 1 + x_scale
        rotate_t[0] = 1 + x_scale
        if k in rand_ints:
            g, shift = make_line_trace()
            if transl_t[0] > 100:
                print('big trans', transl_t[0])

        else:
            if (k % 2) == 0:
                line_n = add_points(l)
                lines_n, shift_not = line_trace_from_p(line_n, nr_lines=1)
            else:
                lines_n = [l]
            plines = polylines(dwg, lines_n, trans_dic)
            #plines = polylines(dwg, lines_n)
            g = group_elements(dwg, plines, class_n='polyline')


        #transform_allmeths(g, trans_dic)
        #transl_t[0] = transl_t[0] + shift[0] #* scale_f
        #transl_t[1] = transl_t[1] + shift[1] #* scale_f
        shift = [0, 0]


            #translate(g, sx=x_shift*scale_f, sy=y_shift*scale_f)
        groups.append(g)
    return groups