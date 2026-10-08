import pandas as pd

age = pd.Series([30, 32, 28, 35], index=['p', 'q', 'r', 's'])
print("--- Pandas Series (1D) ---")
print(age)
print(f"DataType:" ,age.dtype)
print(f"Values: ",age.values)
print(f"Index: ",age.index)