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

#add to the csv file a column of 'Year' (from 2005-2009)
#plot the trend from 2005-2009, two graphs per state, each show changes in total public road length,  drivers per 1000 total resident population as number of drivers must be closely related to overall amount of resident population
#for CA NY AK TX FL VA
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("Output.csv")
State=df["State"].unique()
ax = df.loc[df.State=="Alaska", ["Total", "Year"]].plot(x = "Year", y = "Total", title = "Alaska PRL")
ax.set_ylabel("Total Public Road Length")
ax.set_xlabel("Year")
ax.get_figure().savefig('AK_PRL.pdf')

ax1 = df.loc[df.State=="Alaska", ["Drivers per 1,000 total resident population", "Year"]].plot(x = "Year", y = "Drivers per 1,000 total resident population", title = "Alaska LD")
ax1.set_ylabel("Drivers per 1,000 total resident population")
ax1.set_xlabel("Year")
ax1.get_figure().savefig('AK_LD.pdf')

ax2= df.loc[df.State=="California", ["Total", "Year"]].plot(x = "Year", y = "Total", title = "California PRL")
ax2.set_ylabel("Total Public Road Length")
ax2.set_xlabel("Year")
ax2.get_figure().savefig('CA_PRL.pdf')

ax3 = df.loc[df.State=="California", ["Drivers per 1,000 total resident population", "Year"]].plot(x = "Year", y = "Drivers per 1,000 total resident population", title = "California LD")
ax3.set_ylabel("Drivers per 1,000 total resident population")
ax3.set_xlabel("Year")
ax3.get_figure().savefig('CA_LD.pdf')

ax4 = df.loc[df.State=="Texas", ["Total", "Year"]].plot(x = "Year", y = "Total", title = "Texas PRL")
ax4.set_ylabel("Total Public Road Length")
ax4.set_xlabel("Year")
ax4.get_figure().savefig('TX_PRL.pdf')

ax5 = df.loc[df.State=="Texas", ["Drivers per 1,000 total resident population", "Year"]].plot(x = "Year", y = "Drivers per 1,000 total resident population", title = "Texas LD")
ax5.set_ylabel("Drivers per 1,000 total resident population")
ax5.set_xlabel("Year")
ax5.get_figure().savefig('TX_LD.pdf')

ax7 = df.loc[df.State=="New York", ["Total", "Year"]].plot(x = "Year", y = "Total", title = "New York PRL")
ax7.set_ylabel("Total Public Road Length")
ax7.set_xlabel("Year")
ax7.get_figure().savefig('NY_PRL.pdf')

ax6 = df.loc[df.State=="New York", ["Drivers per 1,000 total resident population", "Year"]].plot(x = "Year", y = "Drivers per 1,000 total resident population", title = "New York LD")
ax6.set_ylabel("Drivers per 1,000 total resident population")
ax6.set_xlabel("Year")
ax6.get_figure().savefig('NY_LD.pdf')

ax8 = df.loc[df.State=="Florida", ["Total", "Year"]].plot(x = "Year", y = "Total", title = "Florida PRL")
ax8.set_ylabel("Total Public Road Length")
ax8.set_xlabel("Year")
ax8.get_figure().savefig('FL_PRL.pdf')

ax9 = df.loc[df.State=="Florida", ["Drivers per 1,000 total resident population", "Year"]].plot(x = "Year", y = "Drivers per 1,000 total resident population", title = "Florida LD")
ax9.set_ylabel("Drivers per 1,000 total resident population")
ax9.set_xlabel("Year")
ax9.get_figure().savefig('FL_LD.pdf')

ax10 = df.loc[df.State=="Virginia", ["Total", "Year"]].plot(x = "Year", y = "Total", title = "Virginia PRL")
ax10.set_ylabel("Total Public Road Length")
ax10.set_xlabel("Year")
ax10.get_figure().savefig('VA_PRL.pdf')

ax11 = df.loc[df.State=="Virginia", ["Drivers per 1,000 total resident population", "Year"]].plot(x = "Year", y = "Drivers per 1,000 total resident population", title = "Virginia LD")
ax11.set_ylabel("Drivers per 1,000 total resident population")
ax11.set_xlabel("Year")
ax11.get_figure().savefig('VA_LD.pdf')

#rearrange and group the columns by state 2000 to 2010 Population and Area Change by 2010 Urbanized Area
#First make a new column in the csv file 'State'
df_pop=pd.read_csv("PopAreaChngeUA.csv")
city='Chicago, IL'
patter  = '.*,\s.(.*)'
re.findall(pattern,city)
df_pop[State]=re.findall(pattern,df_pop[UANAME])

#Groupby states and ignore the ones with multiple states
print df_pop.groupby('State').sum()

#population change in urban area from 2000 to 2010 and land area change in urban area from 2000 to 2010
#general trend in CA NY AK TX FL VA
