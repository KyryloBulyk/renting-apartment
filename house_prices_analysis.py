import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

train_data = pd.read_csv('house-prices-advanced-regression-techniques/train.csv')
test_data = pd.read_csv('house-prices-advanced-regression-techniques/test.csv')

missing_values = train_data.isnull().sum()
missing_values = missing_values[missing_values > 0]


missing_values_test = test_data.isnull().sum()
missing_values_test = missing_values_test[missing_values_test > 0]

train_data['LotFrontage'] = train_data['LotFrontage'].fillna(train_data['LotFrontage'].mean())
test_data['LotFrontage'] = test_data['LotFrontage'].fillna(test_data['LotFrontage'].mean())

# Приклад: заповнення модою для категоріальних даних
train_data['Electrical'] = train_data['Electrical'].fillna(train_data['Electrical'].mode()[0])
test_data['Electrical'] = test_data['Electrical'].fillna(test_data['Electrical'].mode()[0])

# Видалення стовпців з великою кількістю пропущених значень
train_data = train_data.drop(columns=['Alley', 'PoolQC', 'Fence', 'MiscFeature'])
test_data = test_data.drop(columns=['Alley', 'PoolQC', 'Fence', 'MiscFeature'])

# Конвертація категоріальних даних у числові за допомогою one-hot encoding
train_data = pd.get_dummies(train_data)
test_data = pd.get_dummies(test_data)

# Вирівнювання кількості стовпців у тренувальному та тестовому наборах даних
train_data, test_data = train_data.align(test_data, join='inner', axis=1)

correlation_matrix = train_data.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, vmax=0.8, square=True)
plt.title('Correlation Matrix')
plt.show()

corr_with_target = correlation_matrix['SalePrice'].sort_values(ascending=False)
print("Features most correlated with SalePrice:")
print(corr_with_target.head(10))

plt.figure(figsize=(10, 6))
sns.histplot(train_data['SalePrice'], kde=True)
plt.title('Distribution of SalePrice')
plt.show()

important_features = corr_with_target.index[1:11]
for feature in important_features:
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=train_data[feature], y=train_data['SalePrice'])
    plt.title(f'SalePrice vs {feature}')
    plt.show()

X = train_data.drop(columns=['SalePrice'])
y = train_data['SalePrice']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Data prepared for modeling:")
print(f"Training data shape: {X_train.shape}")
print(f"Testing data shape: {X_test.shape}")