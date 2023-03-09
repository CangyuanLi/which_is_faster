import random
import string
import timeit

import cutils
import matplotlib.pyplot as plt
import pandas as pd

import sys
sys.path.append(".")
from butils import utils

def generate_ascii(min_len: int=1, max_len: int=20):
    length = random.randint(min_len, max_len)

    return "".join(random.choices(string.printable, k=length))

def generate_int(min: int=-100, max: int= 100):
    return random.randint(min, max)

def generate_float(min: int=-100, max: int=100):
    return random.uniform(min, max)

def raw_series(series: pd.Series):
    for _ in series:
        pass

def to_list(series: pd.Series):
    for _ in series.to_list():
        pass

def to_numpy(series: pd.Series):
    for _ in series.to_numpy():
        pass

def to_arr(series: pd.Series):
    for _ in series.array:
        pass

def to_list_no_create(lst: list):
    for _ in lst:
        pass

def to_numpy_no_create(arr):
    for _ in arr:
        pass

def main():
    series_lens = list(range(0, 8))
    res = []
    for i in series_lens:
        series_len = 10 ** i

        for series_type in ("string", "int", "float"):
            if series_type == "string":
                series = pd.Series(utils.generate_ascii() for _ in range(0, series_len))
            elif series_type == "int":
                series = pd.Series(generate_int() for _ in range(0, series_len))
            elif series_type == "float":
                pd.Series(generate_float() for _ in range(0, series_len))

            series_lst = series.to_list()
            series_numpy = series.to_numpy()

            raw = cutils.time_func(lambda: raw_series(series), warmups=3, iterations=100)
            lst = cutils.time_func(lambda: to_list(series), warmups=3, iterations=100)
            numpy = cutils.time_func(lambda: to_numpy(series), warmups=3, iterations=100)
            arr = cutils.time_func(lambda: to_arr(series), warmups=3, iterations=100)
            lst_no_create = cutils.time_func(lambda: to_list_no_create(series_lst), warmups=3, iterations=100)
            numpy_no_create = cutils.time_func(lambda: to_numpy_no_create(series_numpy), warmups=3, iterations=100)

            res.append({"category": "s", "type": series_type, "mean": raw.avg})
            res.append({"category": "s.to_list()", "type": series_type, "mean": lst.avg})
            res.append({"category": "s.to_numpy()", "type": series_type, "mean": numpy.avg})
            res.append({"category": "s.arr", "type": series_type, "mean": arr.avg})
            res.append({"category": "list", "type": series_type, "mean": lst_no_create.avg})
            res.append({"category": "np.array()", "type": series_type, "mean": numpy_no_create.avg})

    res = pd.DataFrame(res)
    res.to_csv("results.csv")


if __name__ == "__main__":
    a = timeit.repeat(lambda: raw_series([utils.generate_ascii() for _ in range(100)]), repeat=10, number=10)
    print(a)
    a = cutils.time_func(lambda: raw_series([utils.generate_ascii() for _ in range(100)]), iterations=10)
    print(a.raw_times)