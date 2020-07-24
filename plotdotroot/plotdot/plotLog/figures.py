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
    steps_b = 3

    
    def create_line():
        line_new = []
        # todo different enum -> use list and just sum
        for (x, y), k in np.ndenumerate(line_b):
            k = int(k)
            k_b = k - steps_b
            if k_b < 0:
                k_b = 0

            x_line_b = line_b.transpose()[0]
            x_line_val = x_line_b[k_b:k + 1]
            x_val = x_line_val.sum()/x_line_val.size
            randint = random.randint(0, random_stp)
            add_x = shift + (-1/2 + randint/random_stp) * rand_range
            try:
                line_new = np.append(line_new, [[x_val + add_x, y]],  axis=0)
            except ValueError:
                line_new = np.array([[x_val + add_x, y]])
        return line_new

    max_val = 10
    nr_steps = 100
    ratio_shift_range = 4
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
    shift = 2 * ratio_shift_range
    rand_range = ratio_shift_range
    for i in range(0, nr_steps):
        print('step', i)
        line_b = create_line()
        lines.append(line_b)
    return lines


