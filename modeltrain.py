import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_absolute_error
df = pd.read_csv("final.csv")

x = df[['Hours']]
y = df['Scores']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.1,random_state=44)

model = LinearRegression()

model.fit(x_train,y_train)
h = float(input("Enter your study hours :"))
p = model.predict([[h]])
print(f"as your study hours{h} your expected marks is {p} ")

k = model.predict(x_test)
score = r2_score(y_test,k)
print("r2 score :",score)
mae = mean_absolute_error(y_test,k)
print("mae : ",mae)