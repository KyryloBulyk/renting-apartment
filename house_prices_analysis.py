import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

train_data = pd.read_csv('house-prices-advanced-regression-techniques/train.csv')
test_data = pd.read_csv('house-prices-advanced-regression-techniques/test.csv')

print("Train Data Head:")
print(train_data.head())

print("\nTest Data Head:")
print(test_data.head())

print("\nTrain Data Info:")
print(train_data.info())

print("\nTest Data Info:")
print(test_data.info())

print("\nTrain Data Description:")
print(train_data.describe())

print("\nTest Data Description:")
print(test_data.describe())