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
