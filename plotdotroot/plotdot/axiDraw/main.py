import os
from pyaxidraw import axidraw
from plotdotproject.settings import _OUTPUT_DIR


def svg_plot(svg_input):
    ad = axidraw.AxiDraw()
    ad.plot_setup(svg_input)
    ad.plot_run()


def svg_from_file(file_name = 'logoetiki' + '.svg'):
    f_path = os.path.join(_OUTPUT_DIR, file_name)
    svg_plot_preview(f_path)


def svg_plot_layers(svg_input, outp_name='gensvg', nr_layers=1, preview=True):
    """
    0 - Do not render previews
    1 - Render pen-down movement only
    2 - Render pen-up movement only
    3 - Render all movement, both pen-up and pen-down [DEFAULT]
    """
    for k in range(1, nr_layers):
        n = '-'.join([outp_name, str(k)]) + '.svg'
        svg_plot_preview(svg_input, outp_name=n, layer=k)


def svg_plot_preview(svg_input, outp_name='gensvg.svg', layer=None):
    """
    """
    ad = axidraw.AxiDraw()
    ad.plot_setup(svg_input)
    ad.options.preview = True
    ad.options.report_time = True
    if layer:
        ad.options.mode = "layers"
        ad.options.layer = layer

    output_svg = ad.plot_run(True)
    save_file(output_svg, outp_name)
    print("{0}".format(ad.pt_estimate))


def save_file(output_svg, n):
    outp_name = n
    save_f = os.path.join(_OUTPUT_DIR, outp_name)
    with open(save_f, 'w') as f:
        f.write(output_svg)


if __name__ == '__main__':
    file_name = 'layers_all' + '.svg'
    #f_path = os.path.join(_OUTPUT_DIR, file_name)
    f_path = '/Users/daim/softwareDev/20_smallstuff/20_axidraw/plots/layers_all.svg'
    svg_plot(f_path)
    #svg_plot_preview(f_path, outp_name='gensvg.svg')