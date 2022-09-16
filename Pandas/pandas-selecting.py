import pandas as pd

from numpy.random import randn

df=pd.DataFrame(randn(3,3), index=["A","B","C"], columns = ["Column1","Column2","Column3"])

result=df
result=df["Column1"]
result=df.loc[:,"Column1"]
result=df[["Column1","Column2"]]
result=df.loc[:,["Column1","Column2"]]
result=df.loc[:,"Column1":"Column2"]
result=df.loc[:,:"Column2"]
result=df.loc["A":"B",:"Column2"]
result=df.loc[:"B",:"Column2"]
result=df.loc["A","Column2"]
result=df.loc["A"] #loc = location
print(result)