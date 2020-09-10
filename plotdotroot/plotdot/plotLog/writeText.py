from plotdotproject.settings import PX_MM

def make_quittung(x0=25, y0=130, w_tot=180):
    """numbers in mm"""
    txt_lines = []
    txt_blk = quittung_text_blocks()

    line_h = 5
    block_w = (w_tot - 4 * 5) / 4
    for i in range(4):
        x = (x0 + i * block_w)
        # br = '\n'
        for j, txt in enumerate(txt_blk):
            y = (y0 + j * line_h)
            tc = txt.upper()
            txt_lines.append((tc, (x, y)))
    return txt_lines


def quittung_text_blocks():
    txt_blk = [
        'initialize plotdot',
        '2020.203 13.1478',  # seconds
        'commit 2384uhjsdf',
        'est. plot time: 544',
    ]
    return txt_blk


def write_in_center(area_def, txt='hallo du hallo du gigel du gigle hallo'): # hallo du gigel du gigle hallo du gigel du gigle
    """write text in center of area"""

    def get_line_size(wrds_li):
        ls = len(wrds_li) - 1  # space between words
        for w in wrds_li:
            ls += len(w)
        return ls

    x_orig, y_orig, w_tot, h_tot = area_def
    words_per_line = 4
    txt = txt.upper()
    words = txt.split(' ')
    nr_w = len(words)
    nr_l = nr_w // words_per_line + (nr_w % words_per_line > 0)

    y_center = y_orig + h_tot / 2
    x_center = x_orig + w_tot/2
    l = 0
    wrd = 0
    ls_max = 0
    lines_w = []
    while l < nr_l:
        l += 1
        words_l = words[wrd:wrd + words_per_line]
        phrase = ' '.join(words_l)
        wrd += words_per_line
        line_size = get_line_size(words_l)
        ls_max = max(ls_max, line_size)
        lines_w.append(phrase)
    font_width = w_tot/ls_max
    font_size = font_width * 1.8  # ration size/width?
    font_gap = font_size * -0.3
    lh_untransf = (font_size + font_gap) #todo not exact yet
    l_height = h_tot / nr_l
    y0 = y_orig + l_height + font_gap # as text is above y #todo not exact yet

    text_def = (font_size, l_height)
    scale_y = l_height/lh_untransf
    trans_def = (scale_y, )

    txt_lines = []

    for j, txt in enumerate(lines_w):
        y_orig = y0 + j * l_height
        y_scaled = y_orig * scale_y
        trans = y_scaled - y_orig
        trans_scaled = trans/scale_y
        y = y_orig - trans_scaled
        txt_lines.append((txt, (x_center, y)))  # x=50% would work as well; text_anchor in svgwrite: "middle";
    return txt_lines, text_def, trans_def


