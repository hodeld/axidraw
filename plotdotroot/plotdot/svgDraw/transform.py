import random


def scale(ele, sx, sy=None):
    if sy is None:
        sy = sx
    ele.scale(sx, sy)


def translate(ele, sx, sy=0):
    ele.translate(sx, sy)

_TRANSF_FN = {1: scale}

_SCALE_TRANS = {1: (1, 1)}


def transform_random(svg_ele):

    return svg_ele


def transform_cont(elemnts):
    sx, sy = random.randint(1, 10), random.randint(1, 10)
    trans_meth = random.randint(1, 4)
    x_f, y_f = _SCALE_TRANS[trans_meth]
    sx_b = sx * x_f
    sy_b = sy * y_f
    velo = 0.1  # float 0 ... 1

    dispatch_fn = _TRANSF_FN
    for k, ele in enumerate(elemnts):
        (sx, sy) = (sx_b, sy_b) * (1 + k * velo)
        dispatch_fn[trans_meth](ele, sx, sy)
        sx_b, sy_b = sx, sy



