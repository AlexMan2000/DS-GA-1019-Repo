import time
import threading
import multiprocessing as mp
import numpy as np

def func(t, x):
    return np.power(t, x-1) * np.exp(-1 * t)




def multiprocessing_calculate_gamma(x, bound_1, bound_2, number_of_steps, num_of_process):
    # Init
    t_segs = np.linspace(bound_1, bound_2, number_of_steps + 1)
    step_size = (bound_2 - bound_1) / (number_of_steps)
    parameter_list = [(t, x) for t in t_segs[:-1]]

    # Open Pools
    pool = mp.Pool(num_of_process)
    results_mp = pool.starmap(func, parameter_list)
    pool.close()

    return np.trapz(results_mp, dx=step_size)



if __name__ == '__main__':
    # arr = np.random.randint(0, 10, size=[5000])
    # data = arr.tolist()
    # results = []
    # for x in data:
    #     results.append(func(x))

    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('-n', type=int)

    args = parser.parse_args()

    start = time.time()
    result = multiprocessing_calculate_gamma(6, 0, 100, 10000000, args.n)
    error = 120 - result
    print(f"Result: {result}, Time Lapsed: {time.time() - start}, error is {error}")

