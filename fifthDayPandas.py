import pandas as pd

#first column is index 
#second column value

print(pd.Series([10,88,3,4,5]));

series = pd.Series([1,85,3,4,5]);
print(type(series));


#The index structure of the series is accessed
print(series.axes);

print(series.ndim);
print(series.dtype);
print(series.size);

print(series.values);

print(series.head());  #return the first 5 row

print(series.tail());  #return the last 5 row


series1 = pd.Series([99,23,76,2323,98], index=[1,3,5,7,9]);
print(series1);

series2 = pd.Series([99,23,76,2323,98], index=["a","b","c","d","e"]);
print(series2);

print(series2["a"]);
print(series2["a":"c"]);

#Create a dictionary

dict1 = {"reg":10, "log":11,"cart":12};
print(pd.Series(dict1));

#Concatenation
print(pd.concat([series2,series2]));

#Indexing and Slicing

import numpy as np

a = np.array([1,2,33,444,75],dtype=np.int64);
npSeries = pd.Series(a);

print(npSeries);
print(npSeries[0]);
print(npSeries[0:3]);


b = pd.Series([121,200,150,99], index=["reg","log","cart","rf"]);

print(b);
print(b.index);
print(b.keys);
print(b.keys());

print(list(b.items()));
print(b.values);


print("reg" in b);
print("a" in b);

print(b["reg"]);


#fancy
print(b[["rf","reg"]]);

print(b["reg":"log"]);

print(b["reg"] in b);


#Creating DataFrame
#Numpy  cannot keep categorical and numeric data together. That's why we need Pandas

l = [1,2,23,345,7,8,3];

print(pd.DataFrame(l,columns=["Değişken İsimleri"]));

m = np.arange(1,10).reshape((3,3));
print(m);

print(pd.DataFrame(m,columns=["var1","var2","var3"]));


#DataFrame renaming
df = pd.DataFrame(m,columns=["val1","val2","val3"]);

print(df);

print(df.head());

print(df.columns);

df.columns = ["deg1","deg2","deg3"];
print(df);

print(df.index);

print(df.describe());

print(df.T);

print(type(df));

print(df.axes);

print(df.shape);

print(df.ndim);

print(df.size);

print(df.values);

s1 = np.random.randint(10,size=5);
s2 = np.random.randint(10,size=5);
s3 = np.random.randint(10,size=5);

dict2 = {"var1":s1, "var2":s2, "var3":s3};
print(dict2);

dfDict = pd.DataFrame(dict2);

print(dfDict);
print(dfDict[0:2]);

dfDict.index=["a","b","c","d","e"];

print(dfDict);

print(dfDict["c":"e"]);

dfDict.drop("a",axis=0);
print(dfDict);

#inplace = If we make it true, the drop will be done permanently.
dfDict.drop("a",axis=0, inplace=True);  #inplace = default False
print(dfDict);

#fancy
l = {"c","e"};
dfDict.drop(l,axis=0);


#loc & iloc

r = np.random.randint(1,30,size=(10,3));
dfR = pd.DataFrame(r, columns=["var1","var2","var3"]);

print(dfR);

print(dfR.loc[0:3]);
print(dfR.iloc[0:3]);
print(dfR.loc[0:3,"var3"]);
print(dfR.loc[0:3]["var3"]);

#print(dfR.iloc[0:3,"var3"]);  #error
print(dfR.iloc[0:3]["var3"]);


#Conditional Operations
print(dfR[0:2][["var1","var2"]]);

print(dfR.var1 > 15);

print(dfR[dfR.var1 > 15]["var2"]);

print(dfR[(dfR.var1 > 10)&(dfR.var3 < 8)]);


#Join
dfR2 = dfR + 99;
print(dfR2);

print(pd.concat([dfR,dfR2]));
print(pd.concat([dfR,dfR2], ignore_index=True));

print(dfR2.columns);

dfR2.columns = ["var1", "var2", "deg3"];
print(dfR2);

print(pd.concat([dfR,dfR2]));

print(pd.concat([dfR,dfR2],join="inner",ignore_index=True));


#Concatenation
dfD = pd.DataFrame({'Worker':['John','Doe','Mehmet','Jeff'],'Positions':['HR','Engineering','AI','Accounting']});

print(dfD);

dfD2 = pd.DataFrame({'Worker':['John','Doe','Mehmet','Jeff'],'Date_Of_Starting_Work':[2012,2018,2015,2017]});
print(dfD2);

dfD3 = pd.merge(dfD,dfD2);
print(dfD3);

#many to one
dfD4 = pd.merge(dfD,dfD2,on='Worker');
print(dfD4);

dfD5 = pd.DataFrame({'Positions':['HR','Engineering','Accounting'], 'Mudur':['Caner','Mustafa','Berkcan']})
dfD6 = pd.merge(dfD4,dfD5);
print(dfD6);


#many to many
dfD7 = pd.DataFrame({'Positions':['HR','Engineering','Accounting','AI'],'Ability':['Math','Excel','Linux','Coding']});

dfD8 = pd.merge(dfD7,dfD);

print(dfD8);