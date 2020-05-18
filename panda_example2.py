import pandas as pd

#data = pd.read_csv('./demo_files/sales_records.csv')

#sales = pd.DataFrame(data)
#print(sales)


data = pd.read_csv('./demo_files/sales_records.csv', index_col=0)
#sales = pd.DataFrame(data[['Country']])
#sales = pd.DataFrame(data[['Country','Total Profit']])

## use loc & iloc
#sales = data.loc[['Asia']]
sales = data.iloc[[5]]

print(sales)