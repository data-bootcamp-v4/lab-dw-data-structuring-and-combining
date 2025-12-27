
Data transformation
concatenation
add more rows or columns
do merge / join (with rowlabels)
reshapping df

To combine 2 or more DF we use concat  # keep in mind that it can be differnce number of rows or columns, (the left will be add by missing values (na)

# To display a DF we should use display(df) instead of print(df)

pd.concat([df1, df2], axis=0)  # we have duplicate index and reset modify the index
pd.concat([df1, df2], axis=0).reset_index(drop=True)  # reset modify the index 

df-all = pd.concat([df1, df2], axis=0).reset_index(drop=True)   # 0 = rows extension / 1 = columns extension

#axis=0 : EXTEND/COMBINE THE ROWS OF DF1 and df2 in column mean  and axis=1 :EXTEND/COMBINE THE ROWS OF DF1 and df2 in column

combine dfs with differents columns  -
pd.concat([df_sales, df_revenue, df_costs], axis=0)  => combine verticaly and  na are add when there is not value define in the initial DF 

pd.concat([df_sales, df_revenue, df_costs], axis=1) => the matcheing ref is  rowlabel. that why the dates are not matching.


### `merge`
pd.merge(df_sales, df_revenue, on='Date')  : combine only the common column;  INNER JOIN. combining df1 and df2  and define the ref here is "Data". it only cobine only the common columns. and don't join the row or column non present in the other df.

# Merge the sales and revenue DataFrames on the 'Date' column (outer join)
pd.merge(df_sales, df_revenue, on='Date', how='outer')      how = outer  - add all the columns of both df
pd.merge(df_sales, df_revenue, [on='Date', "product"], how='outer')  how = outer  - add all the 

pd.merge(df_sales, df_revenue, on='Date', how='left') #how=left - add all the rows of the left(the first df) and only the row of second df that are common with left df
# Merge the sales and revenue DataFrames on the 'Date' column (right join)
pd.merge(df_sales, df_revenue, on='Date', how='right') #how = right  - add the the column or rows non common to the df. with ref the df of the right(the second df). remember : we can't merge more than 2 df. if 3 df we combine the result of the first merge (df1 and df2 ) with the 3rd df

join is done base on rows labels
we use the common column as the index
df_sales.set_index('Date', inplace=True)
df_revenue.set_index('Date', inplace=True)
df_costs.set_index('Date', inplace=True)

df_sales.join([df_revenue, df_costs])  we can join more than 2 df

df_sales.join([df_revenue, df_costs], how='inner')  -L all the row in common 
outer : all the rows of the dfs
left base on the row of the left or the first one


1.2. Structuring Data with Pivot, Stack/Unstack, and Melt  => To reshape the df change x,y to y,x

to reset data  PIVOT

1.217e-09 = 1.217*(10^-9)
1.217e+3 = 1.217*(10^3)

pivot_df = df.pivot_table(index='country', columns='year', values=['GDP'], aggfunc='sum') to pivot column change in index of the rows

to pivot one column in row
df_multiindex = df.set_index(['country', 'year'])
df_multiindex

df_multiindex.index  -> To see the indexes

to access to the index by label df.loc("","")

STACK
we "stack" column transform the columns into line. => all the remaining colomn are transformed in row
stacked_data = df_multiindex.stack()
stacked_data

stacked_data = df_multiindex.unstack()  to take out the unique value of the colums

MELL   is used to transform a DataFrame from a wide format to a long format,  
# Melt the DataFrame, keeping 'country' and 'year' as identifier variables, and 'Population' and 'GDP' as value variables
melted_data = pd.melt(df, id_vars=['country', 'year'], value_vars=['Population', 'GDP'], var_name='Indicator', value_name='Value')
melted_data.head()

the column "variable and "value" are automaticaly created.. var_name'new_name) if i want to change the name "variable'
stacked_data
