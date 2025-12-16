import pandas as pd
df=pd.read_csv("data.csv")

print(df)

print(df.isnull().sum())
'''dr=df.dropna()
print(dr)'''

df['Name'].fillna(df['Name'].mode()[0],inplace=True)

df['Hours'].fillna(df['Hours'].mean().round(1),inplace=True)

df['Scores'].fillna(df['Scores'].mean().round(1),inplace=True)

df['Result'].fillna(df['Result'].mode()[0],inplace=True)

print(df)

df.to_csv("cleans.csv",index=False)