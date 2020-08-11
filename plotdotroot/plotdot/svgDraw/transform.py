import random


def scale(ele, sx, sy=None):
    if sy is None:
        sy = sx
    ele.scale(sx, sy)


def translate(ele, sx, sy=0):
    ele.translate(sx, sy)


def skew_x(ele, angle, sy=None):
    ele.skewX(angle)

def skew_y(ele, angle, sy=None):
    ele.skewX(angle)


def rotate(ele, angle, sy=None):
    ele.skewX(angle)

_TRANSF_FN = {1: scale,
              2: translate,
              3: skew_x,
              4: skew_y,
              5: rotate,

              }

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


def transform_allmeths(ele, trans_dic):
    dispatch_fn = _TRANSF_FN
    for k, (x, y) in trans_dic.items():
        dispatch_fn[k](ele, x, y)




