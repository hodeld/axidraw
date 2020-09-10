
def make_quittung(x0=25, y0=130, w_tot=180):
    """numbers in mm"""
    txt_lines = []
    txt_blk = text_blocks()

    line_h = 5
    block_w = (w_tot-4 * 5)/4
    for i in range(4):
        x = (x0 + i * block_w)
        #br = '\n'
        for j, txt in enumerate(txt_blk):
            y = (y0 + j * line_h)
            tc = txt.upper()
            txt_lines.append((tc, (x, y)))
    return txt_lines


def text_blocks():
    txt_blk = [
        'initialize plotdot',
        '2020.203 13.1478',  # seconds
        'commit 2384uhjsdf',
        'est. plot time: 544',
    ]
    return txt_blk