import pandas as pd

# countries = pd.Series(
#     data = ['Англия', 'Канада', 'США', 'Россия', 'Украина', 'Беларусь', 'Казахстан'],
#     index = ['UK', 'CA', 'US', 'RU', 'UA', 'BY', 'KZ'],
#     name = 'countries'
# )
# print(countries)
# print()
# print(countries.loc['US'])
# print()
# print(countries.loc[['US', 'RU', 'UK']])
# print()
# print(countries.iloc[4])
# print(countries.iloc[1:4])
# print()
# print(countries.iloc[[1, 2, 4]])

countries_df = pd.DataFrame({
    'country': ['Англия', 'Канада', 'США', 'Россия', 'Украина', 'Беларусь', 'Казахстан'],
    'population': [56.29, 38.05, 322.28, 146.24, 45.5, 9.5, 17.04],
    'square': [133396, 9984670, 9826630, 17125191, 603628, 207600, 2724902]
})

# print(countries_df)
# print()
countries_df.index = ['UK', 'CA', 'US', 'RU', 'UA', 'BY', 'KZ']
print(countries_df)
print()

# print(countries_df.mean(axis=0))
# print()
# print(countries_df.mean(axis=1))
print(countries_df.loc[['UA', 'BY', 'KZ'], ['population', 'square']])
print(countries_df.iloc[4:8, 1:3])


# countries_df.to_csv('data/countries.csv', index=False, sep=';')
countries_data = pd.read_csv('data/countries.csv', sep=';')
print(countries_data)
# def create_companyDF(income, expenses, years):
#     """
#     Создайте функцию create_companyDF(income, expenses, years), которая  возвращает DataFrame, 
#     составленный из входных данных со столбцами “Income” и “Expenses” и индексами, соответствующим годам рассматриваемого периода.
#     """
#     df = pd.DataFrame({
#         'income': income,
#         'expenses': expenses
#     })
#     df.index = years
    
#     return df

# expenses = [156, 130, 270]
# income = [478, 512, 196]
# years = [2018, 2019, 2020]
# scienceyou = create_companyDF(income, expenses, years)
# scienceyou.loc[2021] = [555, 777]

# print()
# print(scienceyou)
# print()
# print(scienceyou.loc[2021, 'income'])