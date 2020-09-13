prop={"poro":0.25,"perm":150,"lith":"sst"}
print(prop["lith"])

import pandas as pd
data={"poro":[0.1,0.2,0.3],"perm":[50,100,150]}
table=pd.DataFrame(data)
print(table)

data={"poro":[0.1,0.2,0.3],"perm":[50,100,150],"lith":["sst","shale","lst"]}
table=pd.DataFrame(data)
print(table.iloc[0:3,0:3])     
#iloc[row,column]   
#0,1,2 row is printed   #0,1,2 column is printed

print(table.loc[0:3,"poro":"lith"])  
#poro to lith is printed
#not to use i in front


log=pd.read_csv("csv/prod_data.csv")
print(log.shape)
print(log.describe())                                          #gives you the mean, mode, sd, etc. of a column. It gives data for only float and integer types
print(log.columns)                                             #gives you the names of the column
print(log.head())                                              #gives you the first 5 rows
print(log.tail())                                              #gives you the last 5 rows  
c=log[["AVG_DOWNHOLE_PRESSURE","AVG_DOWNHOLE_TEMPERATURE"]]    #Change column name serially
c.columns=["ADP","ADT"]
print(c)

log=pd.read_csv("csv/production_data_2.csv")
log.rename(columns={"AVG_DOWNHOLE_TEMPERATURE":"ADT","FLOW_KIND":"FW"},inplace=True)     #"Original":"New". inplace is used to store data
print(log)
# print(log[(log["ADT"]==0)&(log["FW"]=="production")])
print(log.sort_values(by="ADT",ascending=False))                #sorted by descending order of the values pf ADT

prod=pd.read_csv("csv/prod_data.csv")
print(prod.dtypes)                          #gives you the type of each column
u=prod["WELL_TYPE"].unique()                #gives you all the unique data in a column
u=prod["FLOW_KIND"].nunique()               #gives you total no. of unique values in a column
u=prod["FLOW_KIND"].value_counts()          #gives you how many times each unique value occurs
print(u)

g=prod.groupby("FLOW_KIND")                   #groups column by the each unique data. FLOW_KIND has "production" and "injection" 
print(g.get_group("injection"))               #prints the data you wish from all the unique data
print(g.mean())                               #gives you descriptive value for each unique data
print(g.sum()) 
print(g.count()) 

g=prod.groupby(["FLOW_KIND","WELL_TYPE"])       #multiple grouping
print(g.reset_index())                          #resets index from 0 to 1

print(prod.isna())                              #true if the value is NaN
                                                #false if the value has a number

print(prod.isna().sum())                          #gives you the count null values in a column

print(prod.fillna(method="ffill"))                #forward fill from top to last NaN
print(prod.fillna(method="bfill"))                #backward fill from bottom to top NaN

print(prod.dropna(axis=1))                         #drops all columns with NaN. axis=1 is for columns
print(prod.dropna(axis=0))                         #drops all rows with NaN. axis=0 is for rows
print(prod.dropna(how="all"))                      #drops all rows with NaN.
print(prod.dropna(how="any"))                      #drops all rows with NaN.
print(prod.dropna(thresh=5))                       #drops all rows with >=5 NaN.

prod1=pd.read_csv("csv/production_data_1.csv")
prod2=pd.read_csv("csv/production_data_2.csv")
m=prod1.merge(prod2,left_on="DATEPRD",right_on="DATEPRD")
print(m)

c=pd.concat([prod1,prod2])
print(c)
