#merge Infrastructure:Public Road Length, Miles by Ownership and Passenger Travel:Licensed Drivers
#merging the two csv files for each year(2005-2009) based on state level
import pandas as pd
#year 2005
a=pd.read_csv("PRL2005.csv")
b= pd.read_csv("LD2005.csv")
merged = a.merge(b, on='State')
merged.to_csv("output2005.csv", index=False)

#year 2006
c=pd.read_csv("PRL2006.csv")
d= pd.read_csv("LD2006.csv")
merged = c.merge(d, on='State')
merged.to_csv("output2006.csv", index=False)

#year 2007
e=pd.read_csv("PRL2007.csv")
f= pd.read_csv("LD2007.csv")
merged = e.merge(f, on='State')
merged.to_csv("output2007.csv", index=False)

#year 2008
g=pd.read_csv("PRL2008.csv")
h= pd.read_csv("LD2008.csv")
merged = g.merge(h, on='State')
merged.to_csv("output2008.csv", index=False)

#year 2009
#merge on 'ID' due to error received when merging on 'State'
i=pd.read_csv("PRL2009.csv")
j= pd.read_csv("LD2009.csv")
merged = i.merge(j, on='ID')
merged.to_csv("output2009.csv", index=False)
#for output2009 when then edit the csv file by deleting ID column and repetition in 'State' column

#Combine all 5 years csv files together
f1=pd.read_csv('output2005.csv',header=None)
f2=pd.read_csv('output2006.csv',header=None)
f3=pd.read_csv('output2007.csv',header=None)
f4=pd.read_csv('output2008.csv',header=None)
f5=pd.read_csv('output2009.csv',header=None)
merged=pd.concat([f1,f2,f3,f4,f5],axis=0)
merged.to_csv("output.csv", index=False)

#Combine only the columns we really need in each csv for each year, and drop variables with missing values
#year 2005
df_05_PRL = pd.read_csv("PRL2005.csv", index_col = "State")
df_05_PRL = df_05_PRL[["Total"]]
df_05_PRL.dropna(inplace=True)
df_05_LD = pd.read_csv("LD2005.csv", index_col= "State", usecols=["State", "Number of licensed drivers", "Resident population", "Drivers per 1,000 total resident population"])
df_05_merged= df_05_PRL.join(df_05_LD)
df_05_merged.to_csv("Final2005.csv", index= False)

#year 2006
df_06_PRL = pd.read_csv("PRL2006.csv", index_col = "State")
df_06_PRL = df_06_PRL[["Total"]]
df_06_PRL.dropna(inplace=True)
df_06_LD = pd.read_csv("LD2006.csv", index_col= "State", usecols=["State", "Number of licensed drivers", "Resident population", "Drivers per 1,000 total resident population"])
df_06_merged= df_06_PRL.join(df_06_LD)
df_06_merged.to_csv("Final2006.csv", index= False)

#year 2007
df_07_PRL = pd.read_csv("PRL2007.csv", index_col = "State")
df_07_PRL = df_07_PRL[["Total"]]
df_07_PRL.dropna(inplace=True)
df_07_LD = pd.read_csv("LD2007.csv", index_col= "State", usecols=["State", "Number of licensed drivers", "Resident population", "Drivers per 1,000 total resident population"])
df_07_merged= df_07_PRL.join(df_06_LD)
df_07_merged.to_csv("Final2007.csv", index= False)

#year 2008
df_08_PRL = pd.read_csv("PRL2008.csv", index_col = "State")
df_08_PRL = df_08_PRL[["Total"]]
df_08_PRL.dropna(inplace=True)
df_08_LD = pd.read_csv("LD2008.csv", index_col= "State", usecols=["State", "Number of licensed drivers", "Resident population", "Drivers per 1,000 total resident population"])
df_08_merged= df_08_PRL.join(df_06_LD)
df_08_merged.to_csv("Final2008.csv", index= False)

#year 2009
df_09_PRL = pd.read_csv("PRL2009.csv", index_col = "State")
df_09_PRL = df_09_PRL[["Total"]]
df_09_PRL.dropna(inplace=True)
df_09_LD = pd.read_csv("LD2009.csv", index_col= "State", usecols=["State", "Number of licensed drivers", "Resident population", "Drivers per 1,000 total resident population"])
df_09_merged= df_09_PRL.join(df_06_LD)
df_09_merged.to_csv("Final2009.csv", index= False)

#Combine all 5 years csv files together
f1=pd.read_csv('Final2005.csv',header=None)
f2=pd.read_csv('Final2006.csv',header=None)
f3=pd.read_csv('Final2007.csv',header=None)
f4=pd.read_csv('Final2008.csv',header=None)
f5=pd.read_csv('Final2009.csv',header=None)
merged=pd.concat([f1,f2,f3,f4,f5],axis=0)
merged.to_csv("Output.csv", index=False)
