# Corruptor
[![PyPI](https://img.shields.io/pypi/v/corruptor.svg)](https://pypi.org/project/corruptor)
[![PyPI - License](https://img.shields.io/pypi/l/corruptor.svg)](https://pypi.org/project/corruptor)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/corruptor.svg)](https://pypi.org/project/corruptor)

Want to realistically corrupt your (textual) data? Use Corruptor!

```shell
pip install corruptor
```

The supported type of corruptions:

- OCR variation
- Phonetic variation
- Typing error
- Edit (insert, delete, replace, swap)

## Getting started
There are three different classes that can be used.

### `BasicCorruptor`
The basic corruptor provides methods for each type of corruption, using default configuration.

```python
>>> from corruptor import BasicCorruptor
>>> basic = BasicCorruptor()
>>> basic.ocr('johnson')
'johnst0n'
>>> basic.phonetic('johnson')
'johnzon'
>>> basic.typo('johnson')
'johhson'
>>> basic.insert('johnson')
'johnsson'
>>> basic.delete('johnson')
'jhnson'
>>> basic.replace('johnson')
'johnsin'
>>> basic.swap('johnson')
'johnsno'
```

### `ProbabilisticCorruptor`
This class selects the type of corruption at random, based on provided weights.

```python
>>> from corruptor import ProbabilisticCorruptor
>>> prob = ProbabilisticCorruptor({'none': 0.33, 'phonetic': 0.33, 'typo': 0.33})
>>> prob.corrupt('conner')
'conner'
>>> prob.corrupt('conner')
'conneah'
>>> prob.corrupt('conner')
'conber'
```

### `DataFrameCorruptor`
In short, the DataFrame corruptor randomly corrupts `n` rows of a pandas DataFrame.

```python
>>> import pandas as pd
>>> from corruptor import DataFrameCorruptor
>>> df = pd.DataFrame({'firstname': ['frank', 'john'], 'lastname': ['johnson', 'conner']})
>>> dfc = DataFrameCorruptor({'firstname': (0.5, prob), 'lastname': (0.5, prob)})
>>> dfc.corrupt(df, n=2)
  firstname lastname
0     frahk  johnson
1      john   conber
```




