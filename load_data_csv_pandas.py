import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)


# loc to return one or more specified rows
print('first row \n',df.loc[[0]])
print('two row \n',df.loc[[0,1]])

#In order to give index names we index = 
df1 = pd.DataFrame(data,index = ['day1','day2','day3'])
print(df1)

#Locate index name
print()
print(df1.loc[['day1']])

# Load csv file into dataframe
df = pd.read_csv('C:\\Users\\ss\\AppData\\Local\\Programs\\Python\\Python312\emp_data.csv')
print(df)

#If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows:

# use to_string() to print the entire DataFrame.
print(df.to_string())

# Or else we can another way
pd.options.display.max_rows = None
