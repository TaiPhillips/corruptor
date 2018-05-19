# Corruptor

Want to realistically corrupt your (textual) data? Use Corruptor!

```shell
pip install corruptor
```

The supported type of corruptions:

- Misspell
- OCR variation
- Phonetic variation
- Typing error
- Edit (insert, delete, replace, swap)

## Getting started
There are two different classes that can be used.

### `BasicCorruptor`
The basic corruptor provides methods for each type of corruption, using default configuration.

```python
>>> from corruptor import BasicCorruptor
>>> basic = BasicCorruptor()
>>> basic.misspell('johnson')
'johnston'
>>> basic.phonetic('johnson')
'johnzon'
>>> basic.typo('johnson')
'johhson'
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