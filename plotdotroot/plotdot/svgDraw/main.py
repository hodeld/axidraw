import svgwrite
from svgwrite.path import Path
from svgwrite.mixins import Transform
# import svgutils.transform as st
from svgwrite.extensions import Inkscape
import os
from plotdotproject.settings import BASE_DIR, PX_MM

prjct_root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


def add_layer(dwg, inkscape, layer_name, group, unit_f=PX_MM):
    layer = inkscape.layer(label=layer_name, locked=True)
    group.scale(sx=unit_f)
    layer.add(group)
    dwg.add(layer)
    return layer


def text_svg_layer(dwg, txt_defs, pos_f=PX_MM):
    g_text = dwg.g(class_="quittung-text")  # defines font-size -> should not be scaled afterwards
    for txt_def in txt_defs:
        (txt, (x, y)) = txt_def
        g_text.add(dwg.text(txt, insert=(x * pos_f, y* pos_f)))  # settings are valid for all text added to 'g'
    return g_text


def polylines(dwg, lines):
    plines = []
    for pline in lines:
        p_unit = [(x, y) for (x, y) in pline]
        svg_pline = dwg.polyline(p_unit)
        plines.append(svg_pline)
    return plines


def group_elements(dwg, eles, class_n='polyline'):
    group = dwg.g(class_=class_n)
    for ele in eles:
        group.add(ele)
    return group


def rect_layer(dwg, rect_shape):
    g_shape = dwg.g(class_="shape")  # (stroke="blue", fill='none')
    (x0, y0, w, h) = rect_shape
    g_shape.add(svgwrite.shapes.Rect(insert=(x0, y0),
                                     size=(w, h)))
    return g_shape


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


def make_svg_from_paths(dwg, paths_parsed):
    g_shape = dwg.g(class_="path")
    for p in paths_parsed:
        ps = Path(p.d())
        print(p.d())
        g_shape.add(ps)
    return g_shape


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


def init_dwg(size):
    dwg = svgwrite.Drawing(profile='full', size=size)
    inkscape = Inkscape(dwg)
    css_name = 'svg' + '.css'
    mod_path = os.path.join(BASE_DIR, 'plotdot/svgDraw')
    css_path = os.path.join(mod_path, css_name)
    with open(css_path, 'r') as file:
        data = file.read().replace('\n', '')

    style_def = svgwrite.container.Style(data)
    dwg.defs.add(style_def)
    return dwg, inkscape


if __name__ == '__main__':
    make_quittung_all()