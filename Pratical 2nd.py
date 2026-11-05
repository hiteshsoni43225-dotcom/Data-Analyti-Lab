from tkinter.font import names

import pandas as pd

def calculate_average(marks):
    return sum(marks)/ len(marks)


n=int(input("enter number of students:"))

names =[]
marks =[]

for i in range (n):
    name = input("enter student name:")
    mark = float(input("enter student marks:"))

    names.append(name)
    marks.append(mark)



df = pd.DataFrame({
    "name":names,
    "marks":marks
})


def result(marks):
    if marks >= 85:
        return "Distinction"
    elif marks >= 75:
        return "Pass"
    else:
        return "Fail"

    df["Result"]=df["Marks"].apply(result)

    
    print("\nDataset:")
    print(df)

    
    print("\nStudent Analysis:")
    for marks in df["Marks"]:
        if marks >= 85:
            print(marks,"Distinction")
        elif marks >= 75:
            print(marks,"Pass")
        else:
            print(marks,"Fail")

            
            print("\nAverage maeks:",calculate_average(df["Marks"]))
            print("highest marks:",max(df["Marks"]))
            print("lowest marks:",min(df["Marks"]))

