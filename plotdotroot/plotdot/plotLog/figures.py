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


def line_trace(x0=6, x1=21, y0=5, y1=11, slope=.3):
    random_stp = 50
    nr_steps = 100
    ratio_shift_range = 2
    rand_range = 1 # 1

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
        line_norm = []
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
            x0_k = 0 #line0[k][0] # for bending
            x_new = x0_k + val_trace + shift + rand_shift + calc_shift
            x_new_norm = (x_new + k * norm_slope_x) * norm_len_x + x_0
            y_norm = (y + step_x * norm_slope_y) * norm_len_y + y_0
            line_new.append([x_new, y])
            line_norm.append([x_new_norm, y_norm])
        return line_new, line_norm

    shift = rand_range * ratio_shift_range
    max_w = x1-x0
    max_h = y1-y0

    steps = max_h/nr_steps
    range_steps = range(nr_steps)
    x0_line = np.array([0] * nr_steps)
    yrange = np.array(range_steps)
    #y0_line = yrange * steps
    y0_line = yrange

    norm_len_x = max_w / (ratio_shift_range * nr_steps)
    norm_slope_x = max_w / nr_steps
    x_0 = x0
    norm_len_y = max_h / (nr_steps)
    norm_slope_y = max_h / nr_steps
    y_0 = y0

    line0 = np.column_stack((x0_line, y0_line))
    line_b = line0

    step_x = 0
    line_b, line_norm = create_line()
    #lines = [line_b]
    lines = []

    for step_x in range(0, nr_steps):
        print('step', step_x)
        line_b, line_norm = create_line()
        lines.append(line_norm)
    return lines
