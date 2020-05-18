import pandas as pd

data = pd.read_csv('./demo_files/sales_records.csv')

sales = pd.DataFrame(data)
print(sales)