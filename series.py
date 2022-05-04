import pandas as pd
df = pd.read_csv("cities.csv")
#for column in df.head():
#   print(df.head()[column])
for i in df.index:
    print(list(df.iloc[i]))