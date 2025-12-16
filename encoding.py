import pandas as pd

from sklearn.preprocessing import LabelEncoder

df=pd.read_csv("cleans.csv")

df_label=df.copy()

result=LabelEncoder()

df_label['Result_Encoded']=result.fit_transform(df['Result'])

df_label["Name_OneHot"]=pd.get_dummies(df["Name"]).astype(int).values.tolist()

print(df_label)

df_label.to_csv("encoded.csv",index=False)

