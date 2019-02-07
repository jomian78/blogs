import numpy as np
import math


def get_y(x):
    return 3*x + 5   # a line

def sample_data(n=3000, scale=1): # set scale = 1
    data = []

    x = scale*(np.random.random_sample((n,)))

    for i in range(n):
        yi = get_y(x[i])
        data.append([x[i], yi])

    return np.array(data)
