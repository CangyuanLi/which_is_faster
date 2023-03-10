from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import perfplot

def with_len(df: pd.DataFrame):
    return len(df)

def with_len_index(df: pd.DataFrame):
    return len(df.index)

def with_shape(df: pd.DataFrame):
    return df.shape[0]

def main():
    perfplot.save(
        filename=Path(__file__).resolve().parents[0] / "num_rows_in_df.png",
        setup=lambda n: pd.DataFrame(np.arange(n * 3).reshape(n, 3)),
        n_range=[2**k for k in range(25)],
        kernels=[
            lambda a: len(a),
            lambda a: len(a.index),
            lambda a: a.shape[0],
        ],
        time_unit="auto",
        labels=["len()", "len(df.index)", "df.shape[0]",],
        xlabel="Number of rows",
    )


if __name__ == "__main__":
    main()
