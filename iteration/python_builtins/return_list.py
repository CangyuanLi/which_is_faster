# This file tests which method is the fastest way to return a list of results

import math
from pathlib import Path
import timeit
from typing import Iterable

import matplotlib.pyplot as plt
import pandas as pd

def with_map(func: callable, lst: Iterable):
    list(map(func, lst))

def with_while(func: callable, lst: Iterable):
    i = 0
    res = []
    while i < len(lst):
        res.append(func(lst[i]))
        i += 1

def with_for(func: callable, lst: Iterable):
    res = []
    for i in lst:
        res.append(func(i))

def with_list_comp(func: callable, lst: Iterable):
    [func(i) for i in lst]

def with_gen_comp(func: callable, lst: Iterable):
    list(func(i) for i in lst)

def is_even(i: int):
    return i % 2 == 0

def main():
    lst_range = range(3, 6)
    func_dct = {
        "while": with_while, 
        "for": with_for,
        "map": with_map,
        "list comp": with_list_comp,
        "generator comp": with_gen_comp
    }
    res = {k: [] for k in func_dct}
    for list_len in lst_range:
        lst = range(10 ** list_len)
        for func_nm, func in func_dct.items():
            times = timeit.repeat(lambda: func(is_even, lst), repeat=100, number=100)
            res[func_nm].append(math.log(min(times) + 1))

    plt.close()
    x_axis = [i for i in lst_range]
    for k, v in res.items():
        plt.plot(x_axis, v, label=k)
        plt.xticks(x_axis, [f"10^{i}" for i in lst_range])

    plt.ylabel("Log min time")
    plt.xlabel("List length")
    plt.legend(loc="upper left")
    plt.savefig(Path(__file__).resolve().parents[0] / "iterate_and_return_list.png")
    plt.close()


if __name__ == "__main__":
    main()