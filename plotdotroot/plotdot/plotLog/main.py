import os
from datetime import datetime
import subprocess

from plotdot.svgDraw.transform import translate
from plotdotproject.settings import _OUTPUT_DIR, PX_MM
from plotdot.svgParse.main import parse_svg
from plotdot.axiDraw.main import svg_plot_layers, svg_plot, svg_plot_preview
from plotdot.plotLog.figures import line_trace, line_trace_from_p, add_points
from plotdot.plotLog.patterns import linetraces, line_by_line
from plotdot.plotLog.writeText import make_quittung, write_in_center
from plotdot.svgDraw.main import make_svg, text_svg_layer, rect_layer, init_dwg, \
    make_svg_from_paths, add_layer, group_elements, polylines, text_size_svg_layer
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

    def quittung():
        label_n = layer_name()
        txt_defs = make_quittung(x0=mx, y0=height_graph + my, w_tot=width_p)
        g_text = text_svg_layer(dwg, txt_defs)
        add_layer(dwg, inkscape, label_n, g_text, unit_f=1)

    def graph_text():
        label_n = layer_name()
        mx_add = 10
        my_add = 10
        x = x_graph + mx_add
        y = y_graph + my_add
        width = width_graph - 2 * mx_add
        height = height_graph - 2 * my_add
        area_def = (x, y, width, height)  # x0, y0, w_tot, h_tot = area_def
        txt_defs, font_def, trans_def = write_in_center(area_def=area_def)
        g_text = text_size_svg_layer(dwg, txt_defs, size_def=font_def, trans_def=trans_def)
        add_layer(dwg, inkscape, label_n, g_text, unit_f=1)

    def time_text():
        text_defs_t = [('ztp: ' + datetime.now().strftime('%c'), (10, 10))]
        label_n = layer_name()
        g_text = text_svg_layer(dwg, text_defs_t)
        add_layer(dwg, inkscape, label_n, g_text, unit_f=1)

    def rectangle():
        rect_shape = (x_graph, y_graph, width_graph, height_graph)
        label_n = layer_name()
        g_rect = rect_layer(dwg, rect_shape)
        add_layer(dwg, inkscape, label_n, g_rect, unit_f=PX_MM)

    def art_text():
        lines, scale_f = parse_svg()
        groups = line_by_line(dwg, lines, scale_f)
        for g in groups:
            label_n = layer_name()
            add_layer(dwg, inkscape, label_n, g, unit_f=scale_f)


    size = (width_p * px_mm, height_p * px_mm)
    dwg, inkscape = init_dwg(size)

    k = 1
    ln = 'layer'

    # elements:
    #quittung()
    graph_text()
    #time_text()
    rectangle()
    #art_text()

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