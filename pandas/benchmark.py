import random
import string

import cutils
import pandas as pd

def generate_random_ascii_string(min_len: int=1, max_len: int=20) -> str:
    length = random.randint(min_len, max_len)

    return "".join(random.choices(string.printable, k=length))

def func_1(series: pd.Series):
    return len(series)

def func_2(series: pd.Series):
    return len(series.index)

def main():
    series = [generate_random_ascii_string() for _ in range(0, 800_000)]
    series = pd.Series(series)

    cutils.time_func(lambda: func_1(series), warmups=3, iterations=100)
    cutils.time_func(lambda: func_2(series), warmups=3, iterations=100)


if __name__ == "__main__":
    main()