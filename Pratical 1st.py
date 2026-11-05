import pandas as pd

df = pd.DataFrame({     
    "Name": ["Arjun", "Kavya", "Sahil", "Meera"],     
    "Dept": ["HR", "Sales", "Finance", "IT"],     
    "Age": [24, 29, 26, 31],     
    "Weight": [68, 55, 72, 60],     
    "Salary": [35000, 42000, 38000, 50000] })
  
print("Original Data:\n", df)

# Data Subsetting
print("\nSubset (Salary > 40000):\n", df[df["Salary"] > 40000])

# Sorting in Ascending Order
print("\nSorted by Salary (Ascending):\n",
df.sort_values("Salary"))

# Sorting in Descending Order
print("\nSorted by Salary (Descending):\n",
df.sort_values("Salary", ascending=False))

# Grouping
print("\nGrouped (Average Salary by Department):\n",
df.groupby("Dept")["Salary"].mean())

# Statistical Operations
print("\nMean Salary =", df["Salary"].mean())
print("Median Salary =", df["Salary"].median())
print("Mode Salary =")
print(df["Salary"].mode())