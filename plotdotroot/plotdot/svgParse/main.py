from plotdotproject.settings import _OUTPUT_DIR, PX_MM
from svgpathtools import svg2paths, wsvg, svg2paths2
import os

_DOC_UNIT_TO_MM = 1
_SCALE_F = _DOC_UNIT_TO_MM * PX_MM

def parse_svg():
    outp_name = 'paths.svg'
    file_path = os.path.join(_OUTPUT_DIR, outp_name)

    #mydoc = minidom.parse(file_path)
    #path_tag = mydoc.getElementsByTagName("path")
    #d_string = path_tag[0].attributes['d'].value
    #Path_elements = svgpathtools.parse_path(d_string)

    # Update: You can now also extract the svg-attributes by setting
    # return_svg_attributes=True, or with the convenience function svg2paths2
    paths, attributes, svg_attributes = svg2paths2(file_path)
    #change_start_end(paths)
    path_i = paths[1]  # random
    line_i = path_to_line(path_i)

    return paths, line_i, _SCALE_F
    #paths_sw = to_svgwrite(paths)


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
    def imag_to_real(s):
        x, y = s.start.real, s.start.imag
        line.append((x, y))

    line = []
    imag_to_real(path)

    for p in path:
        imag_to_real(p)

    return line


if __name__ == '__main__':
    parse_svg()