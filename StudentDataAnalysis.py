import pandas as pd

data = {"name": ["Bill", "Tom", "Tim", "John", "Alex", "Vanessa", "Kate"],
        "math score": [90, 90, 80, 70, 65, 10, 50],
        "sport": ["Wrestling", "Football", "Skiing", "Soccer", "Soccer", "Soccer", "Soccer"],
        "gender": ["M", "M", "M", "M", "F", "F", "F"]}

df_data = pd.DataFrame(data)
print(df_data.shape)

#adding column
df_data["major"] = ["BA", "BA", "FIN", "FIN", "MKTG", "MKTG", "MGT"]

#deleting column
del df_data["gender"]

#change index
df_data.index = ["one", "two", "three", "four", "five", "six", "seven", ]

#create a column based on condition
df_data["pass"] = df_data["math score"] >= 85

#summary statistics
df_data.describe()

chem_phy = {"name":["Bill", "Tom", "Tim", "John", "Alex", "Vanessa", "Kate"],
            "chem score": [50, 60, 70, 80, 65, 80, 90],
            "phys_score": [55, 65, 75, 85, 70, 85, 95]}

df_data_2 = pd.DataFrame(chem_phy)

df_data

df_data_2

df_merge = pd.merge(df_data, df_data_2, on = "name", how = "left")

df_merge = df_merge.rename(columns = {"phys_score": "phys score"})

df_merge["total score"] = df_merge["math score"] + df_merge["chem score"] + df_merge["phys score"] 

df_merge[(df_merge["math score"]>=75) & (df_merge["chem score"]>=70)]

df_merge.sort_values(by = ["name"])