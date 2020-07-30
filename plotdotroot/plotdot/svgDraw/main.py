import svgwrite
import os

# import svgutils.transform as st
prjct_root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
PX_MM = 3.543307


def text_svg_layer(dwg, inkscape, layer_name, txt_defs, unit_f= PX_MM):
    layer = inkscape.layer(label=layer_name, locked=True)

    css_name = 'svg' + '.css'
    mod_path = os.path.join(prjct_root_path, 'plotdot/svgDraw')
    css_path = os.path.join(mod_path, css_name)
    dwg.add_stylesheet(css_path, title="svg")  # same rules as for html files

    g_text = dwg.g(class_="quittung-text") #dwg.g(class_="quittung")
    for txt_def in txt_defs:
        (txt, (x, y)) = txt_def
        g_text.add(dwg.text(txt, insert=(x * unit_f, y * unit_f)))  # settings are valid for all text added to 'g'

    layer.add(g_text)
    dwg.add(layer)

    return layer


def polyline_svg_layer(dwg, inkscape, layer_name, plines, unit_f = PX_MM):
    layer = inkscape.layer(label=layer_name, locked=True)
    for pline in plines:
        p_unit = [(x * unit_f, y * unit_f) for (x, y) in pline]
        svg_pline = dwg.polyline(p_unit)
        layer.add(svg_pline)
    dwg.add(layer)
    return layer


def rect_layer(dwg, inkscape, layer_name, rect_shape, unit_f = PX_MM):
    layer = inkscape.layer(label=layer_name, locked=True)
    g_shape = dwg.g(class_="shape")  # (stroke="blue", fill='none')
    (x0, y0, w, h) = rect_shape
    g_shape.add(svgwrite.shapes.Rect(insert=(x0 * unit_f, y0 * unit_f),
                                     size=(w * unit_f, h * unit_f)))
    layer.add(g_shape)
    dwg.add(layer)


def make_svg(txt_defs):
    dwg = svgwrite.Drawing()

    css_name = 'svg' + '.css'
    mod_path = os.path.join(prjct_root_path, 'plotdot/svgDraw')
    css_path = os.path.join(mod_path, css_name)
    dwg.add_stylesheet(css_path, title="svg")  # same rules as for html files

    g_text = dwg.g(class_="quittung-text") #dwg.g(class_="quittung")
    for txt_def in txt_defs:
        (txt, (x, y)) = txt_def
        g_text.add(dwg.text(txt, insert=(x, y)))  # settings are valid for all text added to 'g'

    dwg.add(g_text)

    return dwg


def make_quittung_all():
    dwg = svgwrite.Drawing()

    css_name = 'svg' + '.css'  # 'logoetiki.svg' 'AxiDraw_trivial'
    mod_path = os.path.join(prjct_root_path, 'plotdot/svgDraw')
    css_path = os.path.join(mod_path, css_name)
    dwg.add_stylesheet(css_path, title="svg")  # same rules as for html files

    g_text = dwg.g(class_="quittung-text") #dwg.g(class_="quittung")
    txt_blk = text_blocks_svg()
    x0 = 25
    y0 = 100
    line_h = 5
    block_w = (180-4 * 5)/4
    for i in range(4):
        x = (x0 + i * block_w)
        #br = '\n'
        for j, txt in enumerate(txt_blk):
            y = (y0 + j * line_h)
            tc = txt.upper()
            g_text.add(dwg.text(tc, insert=(x, y)))  # settings are valid for all text added to 'g'

    dwg.add(g_text)

    file_name = 'svgdraw' + '.svg'
    file_path = os.path.join(prjct_root_path, file_name)
    dwg.saveas(file_path)


def text_blocks_svg():
    txt_blk = [
        'initialize plotdot',
        '2020.203 13.1478',  # seconds
        'commit 2384uhjsdf',
        'est. plot time: 544',
    ]
    return txt_blk




if __name__ == '__main__':
    make_quittung_all()