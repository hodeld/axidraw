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
    steps_b = 2
    max_val = 10
    nr_steps = 100
    ratio_shift_range = 2

    def create_line():
        line_new = []
        for k, (x, y) in enumerate(line_b):
            k = int(k)
            k_b = k - steps_b
            if k_b < 0:
                k_b = 0

            line_b_arr = np.array(line_b)
            x_line_b = line_b_arr.transpose()[0]
            x_line_val = x_line_b[k_b:k + 1]
            x_val = x_line_val.sum()/x_line_val.size
            randint = random.randint(0, random_stp)
            add_x = shift + (-1/2 + randint/random_stp) * rand_range
            line_new.append([x_val + add_x, y])
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


