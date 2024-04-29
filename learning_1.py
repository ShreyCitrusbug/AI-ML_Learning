import numpy as np
import pandas as pd

list1 = [1, 2, 3,]
series1 = pd.Series(list1, index=["a", "b", "c"])
print(series1)
d = {'a': 1, 'c': 2, 'E': 3}
print(pd.Series(d, index=["A", "B", "V"]))


dataf = pd.DataFrame([
    ['John Smith', '123 Main St', 34],
    ['Jane Doe', '456 Maple Ave', 28],
    ['Joe Schmo', '789 Broadway', 51]
],
    columns=['name', 'address', 'age'])
print(dataf)
