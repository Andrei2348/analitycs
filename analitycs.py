import pandas as pd

#Код, генерирующий DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()

#Получаем уникальные значения из столбца 'whoAmI'
unique_values = data['whoAmI'].unique()

#Создаем пустой DataFrame
one_hot_data = pd.DataFrame()
'''Для каждого уникального значения создаем новый столбец
и заполняем его значениями 0 или 1'''
for value in unique_values:
    one_hot_data[value] = (data['whoAmI'] == value).astype(int)


one_hot_data.head()
