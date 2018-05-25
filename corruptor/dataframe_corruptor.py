"""dataframe_corruptor.py"""
from random import choices, sample

class DataFrameCorruptor():
    """DataFrameCorruptor definition"""

    def __init__(self, mapping):
        self.population = [(k, mapping[k][1]) for k in mapping.keys()]
        self.weights = [mapping[k][0] for k in mapping.keys()]

    def corrupt(self, df, n):
        indices = sample(list(df.index), n)

        df_copy = df.copy()
        for i in indices:
            (column, corruption) = choices(self.population, self.weights, k=1)[0]
            df_copy.loc[i, column] = corruption.corrupt(df.loc[i, column])

        return df_copy
