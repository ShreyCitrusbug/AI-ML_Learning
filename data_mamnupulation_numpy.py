import numpy as np

# Data Manipulation Technique using Numpy

#  - Shape is dimensions of an array like 1D, 2D or 3D
# - For 1D array shape = (3,)
# - For 2D array shape = (3, 3)
# - For 3D array shape = (3, 3, 3)
# 1. Create a 1D array
one_arrays = np.zeros(shape=(3), dtype=int)
print(one_arrays, "-> ===== 1D Array =====")
# 2. Create a 2D array
two_arrays = np.zeros(shape=(3, 3), dtype=int)
print(two_arrays, "-> ===== 2D Array =====")
# 3. Create a 3D array
three_arrays = np.zeros(shape=(3, 3, 3), dtype=int)
print(three_arrays, "-> ===== 3D Array =====")
# Zeroes in Numpy
zeroes_arrays = np.zeros(shape=(3), dtype=int)
print(zeroes_arrays, "-> ===== 0's Array =====")
# Ones in Numpy
ones_arrays = np.ones(shape=(3, 3), dtype=int)
print(ones_arrays, "-> ===== 1's Array =====")
# Full in Numpy
full_arrays = np.full(shape=(3, 3, 3), fill_value=5, dtype=int)
print(full_arrays, "-> ===== Full Array =====")
# A range with specified range of data
a_range_array = np.arange(start=5, stop=20, step=5, dtype=int)
print(a_range_array, "-> ===== A Range Array =====")
# Line space creates array of values for given space
line_space_array = np.linspace(0, 1, 5, dtype=float)
print(line_space_array, "-> ===== Line Space Array =====")
# Normal distribution value
normal_distribution_value = np.random.normal(0, 1, (2,))
print(normal_distribution_value, "-> ===== Normal Distribution Value =====")
# Identity matrix - diagonal values sets as 1
identity_matrix = np.eye(2)
print(identity_matrix, "-> ===== Identity Matrix =====")
# Array
#  - Size of matrix = row * column
#  - Shape will be (row, column)
#  - ndim will be 1D 2D 3D likewise
print(np.random.randint(10, size=4), "...")
