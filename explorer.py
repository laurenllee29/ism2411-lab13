# What the boolean filter does is that it creates a new DataFrame for rows that are only True. 
# The difference is df["revenue"] returns a Series, while df[df["revenue"]] returns a DataFrame. The distinction matters when you want to use something tht expects a particular structure. 
# If a colleague would ask why I would use pandas instead of Excel, I would say pandas is more efficient because it has reproducible code, identical results, and can handle millions of rows of data. 

print("---Exercise 1---")
import pandas as pd

df = pd.read_csv('data/retail_sales.csv')

#Inspection Commands
print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

print("---Exercise 2---")
south = df[df['region'] == 'South']

print(len(south))
print(south.head())

print("---Exercise 3---")
top_5 = df.sort_values('revenue',
                       ascending=False).head(5)
print(top_5)

print("---Exercise 4---")
big_south = df[(df['region'] == 'South') &
   (df['revenue'] > 1000)]

print("---Exercise 5---")
df['per_unit'] = df['revenue'] / df['quantity']

print(df.head())

print("---Exercise 6---")

print(df['region'].unique())
print(df['region'].value_counts())

print("---Exercise 7---")
df_subset = df[['region', 'product', 'revenue']]
print(df_subset.shape)

print("---Exercise 8---")
df.to_csv('data/retail_sales_subset.csv', 
          index=False)