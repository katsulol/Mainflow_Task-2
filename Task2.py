import pandas as pd

df = pd.read_csv("data.csv")

#Summary Statistics
print(df.head())
print(df.info())
print(df.describe())

#Filtering Data based on Conditions
print(df["Y-Kappa"] > 25) #Conditional Slicing
print(df[df["Y-Kappa"] > 25])#With this line of code we only got those elements whose Y-Kappa is greater than 25.

print((df["ChipRate"] > 14) & (df["ChipRate"] < 16))#In this only those values will be shown true whose ChipRate is between 14 and 16.
print(df[(df["ChipRate"] > 14) & (df["ChipRate"] < 16)])#Out of all 325 elements only 10 elements have ChipRate between 14 and 16.

print(df[(df["Y-Kappa"] > 25) & (df["ChipRate"] < 16) & (df["ChipRate"] > 14)])#Upon Combining both of the above Conditions we can see that only 7 values which have Y-Kappa greater than 25 and ChipRate between 14 to 16.

#Handling Missing Values
df.fillna(df.mean(), inplace=True)
df.fillna(df.median(), inplace=True)


