# Practical 2.2.0

# Topic : 

import numpy as np

num = np.arange(36)
arr1 = np.reshape(num, [4,9])
print("Original Array")
print(arr1)
result = arr1.sum(axis=0)
print("Sum of Columns: ")
print(result)
