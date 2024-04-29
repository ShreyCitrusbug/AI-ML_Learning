import numpy as np
import pandas as pd

# load csv data
test_csv = pd.read_csv("train.csv")
print(test_csv.head(), "-> ===== load csv data =====")
print(test_csv.shape[0], "-> ===== shape csv data =====")
