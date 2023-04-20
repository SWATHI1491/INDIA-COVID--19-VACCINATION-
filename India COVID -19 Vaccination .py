#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install plotly')
get_ipython().system('pip install matplotlib')
get_ipython().system('pip install seaborn')


# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots 
from datetime import datetime


# In[5]:


pip install openpyxl


# In[6]:


get_ipython().system('pip install openpyxl')


# In[7]:


COVID_df=pd.read_excel(r'D:\Certificates\SQL Jupyter Notebook\India COVID-19 VACCINATION\covid_19_india DATA.xlsx') 


# In[8]:


COVID_df.head()


# In[9]:


COVID_df.head(10)


# In[10]:


COVID_df.info()


# In[11]:


COVID_df.describe()


# In[13]:


print(COVID_df.columns)


# In[14]:


COVID_df.drop(["Sno","Time","ConfirmedIndianNational", "ConfirmedForeignNational"],inplace = True,axis = 1 )


# In[15]:


COVID_df.head()


# In[16]:


COVID_df.head()


# In[17]:


Covid_df=pd.read_excel(r'D:\Certificates\SQL Jupyter Notebook\India COVID-19 VACCINATION\covid_19_india DATA.xlsx') 


# In[18]:


Covid_df.head()


# In[20]:


Covid_df.drop(["Sno","Time","ConfirmedIndianNational", "ConfirmedForeignNational"],inplace = True,axis = 1 )


# In[21]:


Covid_df.head()


# In[23]:


Covid_df['Date'] = pd.to_datetime(Covid_df['Date'],format ='%Y-%m-%d')


# In[24]:


Covid_df.head()


# In[26]:


# Active cases = Confirmed - cured +death 

Covid_df['Active_Cases'] = Covid_df['Confirmed'] - (Covid_df['Cured'] + Covid_df['Deaths'])
Covid_df.tail()


# In[27]:


statewise = pd.pivot_table(Covid_df, values = ["Confirmed","Deaths","Cured"], index = "State/UnionTerritory", aggfunc = max)


# In[28]:


statewise["Recovery Rate"] = statewise["Cured"]*100/statewise["Confirmed"]


# In[29]:


statewise["Mortality Rate"] = statewise["Deaths"]*100/statewise["Confirmed"]


# In[30]:


statewise = statewise.sort_values(by = "Confirmed", ascending = False)


# In[31]:


statewise.style.background_gradient(cmap = "cubehelix")


# In[40]:


top_10_active_cases = Covid_df.groupby(by='State/UnionTerritory').max()[['Active_Cases','Date']].sort_values(by=['Active_Cases'], ascending=False).reset_index()


# In[41]:


fig= plt.figure(figsize=(16,9))


# In[42]:


plt.title("Top 10 states with most Active Cases in India", size = 25)


# In[44]:


ax=sns.barplot(data = top_10_active_cases.iloc[:10],y ="Active_Cases",x="State/UnionTerritory",linewidth=2, edgecolor = 'red')


# In[45]:


# "Top 10 states with most Active Cases in India

top_10_active_cases = Covid_df.groupby(by='State/UnionTerritory').max()[['Active_Cases','Date']].sort_values(by=['Active_Cases'], ascending=False).reset_index()

fig= plt.figure(figsize=(16,9))

plt.title("Top 10 states with most Active Cases in India", size = 25)

ax=sns.barplot(data = top_10_active_cases.iloc[:10],y ="Active_Cases",x="State/UnionTerritory",linewidth=2, edgecolor = 'red')

plt.xlabel("States")
plt.ylabel("Total Active Cases")
plt.show()


# In[48]:


# Top States in Deaths 

top_10_deaths = Covid_df.groupby(by='State/UnionTerritory').max()[['Deaths','Date']].sort_values(by=['Deaths'], ascending=False).reset_index()

fig= plt.figure(figsize=(18,5))

plt.title("Top 10 states with most Deaths Cases in India", size = 25)

ax=sns.barplot(data = top_10_deaths.iloc[:12],y ="Deaths",x="State/UnionTerritory",linewidth=2, edgecolor = 'black' )

plt.xlabel("States")
plt.ylabel("Total Deaths Cases")
plt.show()




# In[54]:


# Growth Trend 

fig= plt.figure(figsize=(12,6))

ax=sns.lineplot(data=Covid_df[Covid_df["State/UnionTerritory"].isin(['Maharashtra','Karnataka','Kerala','Tamil Nadu','Uttar Pradesh'])], x='Date', y='Active_Cases', hue='State/UnionTerritory')
ax.set_title("Top 10 states with most Affected Cases in India", size = 16)



# In[55]:


Vaccine_df=pd.read_csv('D:\Certificates\SQL Jupyter Notebook\India COVID-19 VACCINATION\covid_vaccine_statewise.csv') 


# In[56]:


Vaccine_df.head()


# In[59]:


Vaccine_df.rename(columns = { 'Updated On' : 'Vaccine_Date'}, inplace = True)


# In[60]:


Vaccine_df.head(10)


# In[63]:


Vaccine_df.info()


# In[64]:


Vaccine_df.isnull().sum()


# In[66]:


Vaccination =Vaccine_df.drop(columns = ['Sputnik V (Doses Administered)','AEFI','18-44 Years (Doses Administered)','45-60 Years (Doses Administered)','60+ Years (Doses Administered)'], axis = 1)


# In[67]:


Vaccination.head()


# In[71]:


# Male vs  Female

male= Vaccination["Male(Individuals Vaccinated)"].sum()
female = Vaccination["Female(Individuals Vaccinated)"].sum()
px.pie(names=["Male","Female"],values=[male,female],title="Male and Female Vaccination")


# In[73]:


#Remove Rows State is india

vaccine = Vaccine_df[Vaccine_df.State!='India']
vaccine 


# In[75]:


vaccine.rename(columns = {"Total Individuals Vaccinated" : "Totals"}, inplace = True)
vaccine.head()


# In[78]:


# Most Vaccinated State

max_vac=vaccine.groupby('State')['Totals'].sum().to_frame('Totals')
max_vac=max_vac.sort_values('Totals',ascending = False)[:5]
max_vac
                            


# In[83]:


fig= plt.figure(figsize=(10,5))

plt.title("Top 5 Vaccinated in India", size = 25)

ax=sns.barplot(data = max_vac.iloc[:10],y =max_vac.Totals, x=max_vac.index,linewidth=2, edgecolor = 'black')

plt.xlabel("States")
plt.ylabel("Vaccination")
plt.show()


# In[ ]:




