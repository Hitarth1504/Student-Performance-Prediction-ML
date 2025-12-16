import pandas as pd

df_encod = pd.read_csv("encoded.csv")
df_scal = pd.read_csv("scaldata.csv")

df_final = pd.concat([df_encod,df_scal],axis=1)
df_final.to_csv("final.csv",index=False)