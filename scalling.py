import pandas as pd 

from sklearn.preprocessing import StandardScaler

df=pd.read_csv("cleans.csv")

scal = StandardScaler().fit_transform(df[['Scores','Hours']])
scal_data = pd.DataFrame(scal,columns=['Scores','Hours'])
print(scal_data)
scal_data.to_csv("scaldata.csv",index=False)

