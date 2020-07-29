import os
from pyaxidraw import axidraw

prjct_root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


def svg_from_file(file_name = 'logoetiki' + '.svg'):
    f_path = os.path.join(prjct_root_path, file_name)
    svg_plot(f_path)


def svg_plot(svg_input, outp_name = 'gensvg.svg'):
    """
    0 - Do not render previews
    1 - Render pen-down movement only
    2 - Render pen-up movement only
    3 - Render all movement, both pen-up and pen-down [DEFAULT]

    """
    ad = axidraw.AxiDraw()
    ad.plot_setup(svg_input)
    ad.options.rendering = 3
    ad.options.preview = True

    ad.options.report_time = True
    ad.options.pen_pos_down = 40
    ad.options.pen_pos_up = 30
    output_svg = ad.plot_run(True)
    save_file(output_svg, outp_name)
    print("{0}".format(ad.pt_estimate))


def save_file(output_svg, n):
    outp_name = n
    save_f = os.path.join(prjct_root_path, outp_name)
    with open(save_f, 'w') as f:
        f.write(output_svg)


if __name__ == '__main__':
    file_name = 'logoetiki' + '.svg'
    svg_plot()