# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.5
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# *Yurui Chang*\
# yuruic@umich.edu
#
# [link to the file](https://github.com/yuruic/Stats507/tree/main/pandas_notes)

import pandas as pd
import numpy as np

# ## Question 0 - Topics in Pandas

# ## Pandas.to_timedelta
#
# - To convert a recognized timedelta format / value into a Timedelta type
# - the unit of the arg
#   * 'W'
#   * 'D'/'days'/'day'
#   * ‘hours’ / ‘hour’ / ‘hr’ / ‘h’
#   * ‘m’ / ‘minute’ / ‘min’ / ‘minutes’ / ‘T’
#   * ‘S’ / ‘seconds’ / ‘sec’ / ‘second’
#   * ‘ms’ / ‘milliseconds’ / ‘millisecond’ / ‘milli’ / ‘millis’ / ‘L’
#   * ‘us’ / ‘microseconds’ / ‘microsecond’ / ‘micro’ / ‘micros’ / ‘U’
#   * ‘ns’ / ‘nanoseconds’ / ‘nano’ / ‘nanos’ / ‘nanosecond’ / ‘N’

# * Parsing a single string to a Timedelta
# * Parsing a list or array of strings
# * Converting numbers by specifying the unit keyword argument

time1 = pd.to_timedelta('1 days 06:05:01.00003')
time2 = pd.to_timedelta('15.5s')
print([time1, time2])
pd.to_timedelta(['1 days 06:05:01.00003', '15.5s', 'nan'])

pd.to_timedelta(np.arange(5), unit='d')

# ## pandas.to_datetime
#
# * To convert argument to datetime
# * Returns: datetime, return type dependending on input
#   * list-like: DatetimeIndex
#   * Series: Series of datetime64 dtype
#   * scalar: Timestamp
# * Assembling a datetime from multiple columns of a DataFrame
# * Converting Pandas Series to datetime w/ custom format
# * Converting Unix integer (days) to datetime
# * Convert integer (seconds) to datetime

s = pd.Series(['date is 01199002',
           'date is 02199015',
           'date is 03199020',
           'date is 09199204'])
pd.to_datetime(s, format="date is %m%Y%d")

time1 = pd.to_datetime(14554, unit='D', origin='unix')
print(time1)
time2 = pd.to_datetime(1600355888, unit='s', origin='unix')
print(time2)
