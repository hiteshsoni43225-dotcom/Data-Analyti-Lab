from tkinter.font import names

import pandas as pd

n=int(input("Enter number of students: "))

names = []
ages = []
departments = []
dates = []

for i in range(n):
    print("\nEnter details for student",i+1)

    name = input("enter name:")
    age = input("enter age:")
    department = input("enter department:")
    date = input("enter admissoin date (DD-MM-YYYY):")

    names.append(name)   
    ages.append(age)     
    departments.append(department)     
    dates.append(date) 

    data ={
        'Name': name,  
        'Age': ages,    
        'Department': department,     
        'Admission_Date': dates 
    }

    df = pd.DataFrame(data)

    print("\nOringinal data:")
    print(df)

    print("\nOringinal data types:")
    print(df.dtypes)

#1
#-----------------------------------------------------------------------
df['Age'] = df['Age'].astype(int)
#----------------------------------------------------------------------

#2
#----------------------------------------------------------------------
df['Name'] = df['Name'].str.strip() 

df['Name'] = df['Name'].str.title()

df['Department'] = df['Department'].str.strip() 
#-------------------------------------------------------------------

df['Admission_Date'] = pd.to_datetime(     
    df['Admission_Date'],     
    format='%d-%m-%Y' 
) 

df['year'] = df['Admission_Date'].dt.year

df['month'] = df['Admission_Date'].dt.month

df['day'] = df['Admission_Date'].dt.day

#----------------------------------------------------------------------

print("\ntransformed data:")
print(df)

print("\ntransformed data types:")
print(df.dtypes)


