import pandas as pd


# read dataset
df = pd.read_csv("small.csv", )

# print it and print the types
print(df)
print(df.dtypes)


# define the columns we want to keep
colums_we_want = ['time','Dishwasher [kW]','Furnace 1 [kW]','Microwave [kW]']

#filter for these columns and print
df_filter = df.filter(items = colums_we_want )
print(df_filter)


# add a column with a predefined value and print
df_filter["House_ID"] = 1
print(df_filter)


# turn the columns and values into variable and value column
df_melted = df_filter.melt(id_vars = ['time','House_ID'])
print(df_melted)

