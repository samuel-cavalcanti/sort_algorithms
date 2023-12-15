from data import load_data
from files import load_time_data

import numpy as np
from matplotlib import pyplot


def plot_benchmark():
    times = load_time_data()
    assert times is not None, 'You must run the benchmak before plot'

    t_1 = [s[1] for s in times]
    min_size = min(t_1)
    max_size = max(t_1)
    by_algorithm = {}

    for s in times:
        name, input_size, td = s
        by_algorithm[name] = by_algorithm.get(name, []) + [[input_size, td]]

    for name in by_algorithm:
        if name in ['Quick sort', 'Merge sort', 'Heap sort']:
            pyplot.figure(1)
        else:
            pyplot.figure(0)

        array = np.array(by_algorithm[name])
        time, n = array[:, 1], array[:, 0]

        pyplot.plot(n, time,  label=name,
                    linestyle='dotted', marker='.', linewidth=2.0, markersize=8.0)

    # n = np.linspace(min_size, max_size, 10)
    # n_2 = n*n
    # n_log_n = n*np.log2(n)
    # pyplot.plot(n, n_2/10_000_000, 'o', label='$n^2$')
    # pyplot.plot(n, n_log_n, 'o', label='$nlog_2n$')

    for i, fig_name in zip([1, 0], ['fast_algorithms.svg', 'slow_algorithms.svg']):
        fig =pyplot.figure(i)
        fig.set_size_inches(32, 18)
        pyplot.title('Sorting array')
        legend = pyplot.legend()
        legend.axes.xaxis.label.set_text('Input size')
        legend.axes.yaxis.label.set_text('time in seconds')
        pyplot.savefig(fig_name, bbox_inches='tight')

    #pyplot.show()


if __name__ == "__main__":
    plot_benchmark()
