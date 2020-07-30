import os
from datetime import datetime
import subprocess

from plotdotproject.settings import _OUTPUT_DIR, BASE_DIR
from plotdot.axiDraw.main import svg_plot_layers, svg_plot, svg_plot_preview
from plotdot.plotLog.figures import line_trace
from plotdot.plotLog.patterns import linetraces
from plotdot.plotLog.quittung import make_quittung
from plotdot.svgDraw.main import make_svg, text_svg_layer, polyline_svg_layer, PX_MM, rect_layer, init_dwg
import svgwrite
from svgwrite.extensions import Inkscape


height_p = 230
width_p = 180
height_q = 100
mx = 10
my = 10
width_graph = width_p - 2 * mx
height_graph = height_p - height_q
x_graph = mx
y_graph = my

output_path = _OUTPUT_DIR
px_mm = PX_MM


def plot_order():
    f_in, f_out = file_def()
    create_svg(f_in)
    text_to_path(f_in, f_out)
    svg_plot(f_out)


def preview_plot():
    f_in, f_out = file_def()
    k = create_svg(f_in)
    text_to_path(f_in, f_out)
    svg_plot_layers(f_out, 'layers_gen', k)


def create_svg(path_svg):
    def layer_name():
        nonlocal k
        ln_k = ''.join([str(k), '-', ln])
        k += 1
        print(ln_k)
        return ln_k

    size = (width_p * px_mm, height_p * px_mm)
    dwg, inkscape = init_dwg(size)

    k = 1
    ln = 'layer'
    label_n = layer_name()
    txt_defs = make_quittung(x0=mx, y0=height_graph + my, w_tot=width_p)
    text_svg_layer(dwg, inkscape, label_n, txt_defs)

    text_defs_t = [('ztp: ' + datetime.now().strftime('%c'), (10, 10))]
    label_n = layer_name()
    text_svg_layer(dwg, inkscape, label_n, text_defs_t)

    x0, y0, = 100, 40
    xmax, ymax = 150, 100

    lines = line_trace(x0=x0, xw=xmax, xh=x0, y0=y0, yw=y0 + 3, yh=ymax, density=.2)  #
    label_n = layer_name()
    polyline_svg_layer(dwg, inkscape, label_n, lines)

    rect_shape = (x_graph, y_graph, width_graph, height_graph)
    label_n = layer_name()
    rect_layer(dwg, inkscape, label_n, rect_shape)

    dwg.saveas(path_svg)
    return k


def text_to_path(f_in, f_out):
    """export to f_out including layers and text to path"""
    pr_str = 'inkscape  %s --export-text-to-path  --export-filename=%s' % (f_in, f_out)  # --export-plain-svg
    subprocess.call(pr_str, shell=True)


def file_def():
    file_name = 'layers'
    f_path = os.path.join(output_path, file_name)
    f_in = f_path + '_all' + '.svg'
    f_out = f_path + 'all_txtpath' + '.svg'
    return f_in, f_out


if __name__ == '__main__':
    #plot_order()
    preview_plot()