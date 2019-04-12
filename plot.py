# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import csv
import sys

def main():
    if len(sys.argv) < 2:
        print("Please enter filename.")
    else:
        data = map(read_csv(sys.argv[1]))
        plot(data)


def read_csv(filename):
    results = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            results.append(row)
    return results


def map(data):
    return zip(*[[row[0],
            int(row[1]),
            float(row[2]),
            row[3]] for row in data])


def plot(data):

    fig, axs = plt.subplots(3, 1, constrained_layout=True, figsize=(8, 10), dpi=80)
    multiplot(axs[0], data, 1, 2, 'Elements', 'Time (s)', 3, 'Best', 0, ['Merge', 'ParMerge', 'Quick', 'ParQuick', 'Rust'])
    multiplot(axs[1], data, 1, 2, 'Elements', 'Time (s)', 3, 'Typical', 0, ['Merge', 'ParMerge', 'Quick', 'ParQuick', 'Rust'])
    multiplot(axs[2], data, 1, 2, 'Elements', 'Time (s)', 3, 'Worst', 0, ['Merge', 'ParMerge', 'Quick', 'ParQuick', 'Rust'])
    fig.suptitle(u'Results - 256 Threads', fontsize=20)

    plt.savefig(sys.argv[1].split('.')[0] + '.png')


def multiplot(plotter, data, xidx, yidx, xlabel, ylabel, fidx, f, validx, vals):
    for i in range(len(vals)):
        d = where(where(data, fidx, f), validx, vals[i])
        plotter.plot(d[xidx], d[yidx], label=vals[i])
        plotter.set_title(f)
        plotter.set_xlabel(xlabel)
        plotter.set_ylabel(ylabel)
        plotter.legend()


def where(data, column, target):
    results = [[] for _ in range(len(data))]
    for i in range(len(data[column])):
        if data[column][i] == target:
            for j in range(len(data)):
                results[j].append(data[j][i])
    return results


if __name__ == '__main__':
    main()
