import random
import numpy as np
def square(x, y, size):
    path = [
        [x - size, y - size],
        [x + size, y - size],
        [x + size, y + size],
        [x - size, y + size],
    ]
    path.append(path[0])
    return path


def line_trace(max_w, max_h):
    random_stp = 50
    max_val = 10
    nr_steps = 100
    ratio_shift_range = 2
    steps_b_trace = 2
    steps_b_slugg = 3
    factor_slugg = 1.0152  # 0.35 for non-opposite, 1.0152 for opposite at 3 steps
    opposite = True

    if opposite:
        opp_dir = -1
    else:
        opp_dir = 1

    def create_line():
        def mean_val(line_i, start, end):
            line_arr = np.array(line_i)
            x_line_i = line_arr.transpose()[0]
            x_line_val = x_line_i[start:end]
            x_v = x_line_val.sum() / x_line_val.size
            return x_v

        line_new = []
        for k, (x, y) in enumerate(line_b):
            k_bt = k - steps_b_trace
            k_bs = k - steps_b_slugg
            if k_bt < 0:
                k_bt = 0
            if k_bs < 0:
                k_bs = 0

            if line_new:
                mean_before = mean_val(line_new, k_bs, k)
                val_b1 = line_new[k - 1][0]
                val_b2 = line_new[k - 2][0]
                if val_b1 > val_b2:
                    direct = 1
                elif val_b1 < val_b2:
                    direct = -1
                else:
                    direct = 0
            else:
                mean_before, val_b1, val_b2 = 0, 0, 0
                direct = 0

            val_slugg = direct * abs(mean_before-val_b1)

            val_trace = mean_val(line_b, k_bt, k+1)

            randint = random.randint(0, random_stp)
            rand_shift = (-1/2 + randint/random_stp) * rand_range
            calc_shift = factor_slugg * val_slugg * opp_dir

            x_new = val_trace + shift + rand_shift + calc_shift
            line_new.append([x_new, y])
        return line_new

    steps = max_val/nr_steps
    x0 = np.array([0]*nr_steps)
    yrange = np.array(range(nr_steps))
    y0 = yrange * steps
    line0 = np.column_stack((x0, y0))
    line_b = line0
    rand_range = 0
    shift = 0
    line_b = create_line()
    lines = [line_b]
    rand_range = 1
    shift = rand_range * ratio_shift_range

    for i in range(0, nr_steps):
        print('step', i)
        line_b = create_line()
        lines.append(line_b)
    return lines
