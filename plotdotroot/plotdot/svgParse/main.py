from plotdotproject.settings import _OUTPUT_DIR, PX_MM
from svgpathtools import svg2paths, wsvg, svg2paths2
import os

_DOC_UNIT_TO_MM = 1
_SCALE_F = _DOC_UNIT_TO_MM * PX_MM


def parse_svg():
    outp_name = 'paths.svg'
    file_path = os.path.join(_OUTPUT_DIR, outp_name)

    paths, attributes, svg_attributes = svg2paths2(file_path)
    #change_start_end(paths)

    lines = []
    for p in paths:
        lines_i = path_to_line(p)
        lines.extend(lines_i)
    return lines, _SCALE_F


def change_start_end(paths):
    kx = 1.2
    def scale(ele):
        ele.start = ele.start * kx
        ele.end = ele.end * kx #* i
        for seg in ele:
            pass
            #seg.start = seg.start * kx
            #seg.end = seg.end * kx
    for i, p in enumerate(paths):
        if i > 5:
            scale(p)
        #end_new = p.end
        for s in p[2:]:
            #s.start = end_new
            #end_new = s.end * 1.2
            #s.end = end_new
            try:
                print('')
                #s.control1 = s.control1 * (10 + i)/10
            except AttributeError:
                pass


def path_to_line(path):
    """returns several lines if path consists of several non-touching segments"""
    def imag_to_real(s):
        nonlocal end_b
        if end_b and s.start != end_b:
            return False

        x, y = s.start.real, s.start.imag
        line.append((x, y))
        x, y = s.end.real, s.end.imag
        line.append((x, y))
        end_b = s.end

    line = []
    lines = []
    end_b = None
    for p in path:
        if imag_to_real(p) is False:
            lines.append(line)
            line = []
            end_b = None
            imag_to_real(p)
    lines.append(line)
    return lines


if __name__ == '__main__':
    parse_svg()