import os
from datetime import datetime

from plotdot.plotLog.figures import line_trace
from plotdot.plotLog.patterns import linetraces
from plotdot.plotLog.quittung import make_quittung
from plotdot.svgDraw.main import make_svg, text_svg_layer, polyline_svg_layer, PX_MM, rect_layer
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

prjct_root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
px_mm = PX_MM


def plot_order():
    def layer_name():
        nonlocal k
        ln_k = ''.join([str(k), '-', ln])
        k += 1
        return ln_k
    file_name = 'layer' + '.svg'
    f_path = os.path.join(prjct_root_path, file_name)
    dwg = svgwrite.Drawing(f_path, profile='full', size=(width_p*px_mm, height_p*px_mm))
    inkscape = Inkscape(dwg)

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
    dwg.save()





if __name__ == '__main__':
    plot_order()