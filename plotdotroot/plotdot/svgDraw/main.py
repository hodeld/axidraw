import svgwrite
from svgwrite import cm, mm
import os

prjct_root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


def make_quittung():
    dwg = svgwrite.Drawing()

    css_name = 'svg' + '.css'  # 'logoetiki.svg' 'AxiDraw_trivial'
    mod_path = os.path.join(prjct_root_path, 'plotdot/svgDraw')
    css_path = os.path.join(mod_path, css_name)

    dwg.add_stylesheet(css_path, title="svg")  # same rules as for html files

    g_text = dwg.g(class_="quittung-text") #dwg.g(class_="quittung")
    g_text.add(dwg.text('START', insert=(25*mm, 100*mm)))  # settings are valid for all text added to 'g'

    dwg.add(g_text)
    g_shape = dwg.g(class_="shape") # (stroke="blue", fill='none')
    g_shape.add(svgwrite.shapes.Rect(insert=(10*mm, 90*mm), size=(20*mm, 30*mm)))
    dwg.add(g_shape)
    file_name = 'svgdraw' + '.svg'
    file_path = os.path.join(prjct_root_path, file_name)
    dwg.saveas(file_path)


if __name__ == '__main__':
    make_quittung()