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

    layers = []
    for k in range(1, nr_layers):
        ad = axidraw.AxiDraw()
        ad.plot_setup(svg_input)
        ad.options.mode = "layers"
        ad.options.preview = preview
        layers.append(k)
        ad.options.layer = k #layers
        output_svg = ad.plot_run(True)
        n = '-'.join([outp_name, str(k)]) + '.svg'
        save_file(output_svg, n)


def svg_plot_preview(svg_input, outp_name='gensvg.svg'):
    """
    """
    ad = axidraw.AxiDraw()
    ad.plot_setup(svg_input)
    ad.options.preview = True
    ad.options.report_time = True
    ad.plot_run()

    output_svg = ad.plot_run(True)
    save_file(output_svg, outp_name)
    print("{0}".format(ad.pt_estimate))


def save_file(output_svg, n):
    outp_name = n
    save_f = os.path.join(_OUTPUT_DIR, outp_name)
    with open(save_f, 'w') as f:
        f.write(output_svg)


if __name__ == '__main__':
    file_name = 'logoetiki' + '.svg'