# Online Python compiler (interpreter) to run Python online.
import pandas as pd
a=  [1,2,3,4,5]
myvar = pd.Series(a,index = [0,1,2,3,4])
print(myvar)

print(myvar[2:])
    
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)
print(myvar)
print() # one line space

# Create a Series using only data from "day1" and "day2":
print("Selecting only 'day1' & 'day2' ")

myvar1 = pd.Series(calories,index = ['day1','day2'])
print(myvar1)

#create a dataframe from two series
data = {
    'calories':[420,380,390],
    'duration':[50,40,45]
}

df = pd.DataFrame(data)
print(df)
print("\n The first rows ")
print(df.loc[[0]])
