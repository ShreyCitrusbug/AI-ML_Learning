import pandas as pd
import numpy as np

# Data Manipulation Technique using Pandas

data = pd.DataFrame({'Country': ['India', 'Nepal', 'Pakistan', 'Bangladesh', 'Bhutan',],
                    'Rank': [11, 40, 100, 130, 101]})
print(data, "-> ===== DataFrame =====")
print(data.describe(), "-> ===== DataFrame Describe=====")
# Categorized continuous variables
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
print(pd.cut(x=ages, bins=bins, labels=[
      'Youth', 'YoungAdult', 'MiddleAged', 'Senior']), "-> ===== Categorized continuous variables =====")
# Date range in pandas
dates = pd.date_range("20240101", periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('1234'))
print(df, "-> ===== Date Range =====")
# loc in pandas - Access the row column with use of name of index of data frame
print(data.iloc[1], "-> ===== iloc in pandas =====")
# loc in pandas - Access the row column with use of number of index of data frame
data.set_index(keys='Country', inplace=True)
print(data.loc['India'], "-> ===== loc in pandas =====")
data2 = data.copy()
data2["population in M"] = [150, 1, 120, 100, 5]
print(data2, "-> ===== data2 =====")
print(data, "-> ===== data =====")
# Drop duplicate data
duplicate_data = pd.DataFrame(
    {'k1': ['one']*3 + ['two']*4, 'k2': [3, 2, 1, 3, 3, 4, 4]})
print(duplicate_data, "-> ===== Duplicate data =====")
print(duplicate_data.drop_duplicates(), "-> ===== Drop duplicate data =====")
print(duplicate_data.drop_duplicates(subset="k1"),
      "-> ===== Drop duplicate data for column k1=====")
print(duplicate_data.drop_duplicates(subset="k2"),
      "-> ===== Drop duplicate data for column k2=====")
nan_array = pd.DataFrame({
    "Number": [1, 2, 3, 4, 5, 6], "Power": [1, 4, 9, 16, 25, np.nan]
})
print(nan_array, "-> ===== nan_array =====")
print(nan_array.dropna(), "-> ===== dropna =====")
