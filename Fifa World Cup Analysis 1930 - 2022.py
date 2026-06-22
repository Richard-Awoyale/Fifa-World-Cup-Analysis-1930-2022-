#!/usr/bin/env python
# coding: utf-8

# In[99]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly as px


# In[100]:


World_cup = pd.read_csv(r"C:\Users\grawo\OneDrive\Desktop\World Cup\World Cup Host.csv")
goal_scorers = pd.read_csv(r"C:\Users\grawo\OneDrive\Desktop\World Cup\World Cup Top Goal Scorers.csv")
fifa_2022_ranking = pd.read_csv(r"C:\Users\grawo\OneDrive\Desktop\World Cup\fifa_ranking_2022-10-06.csv")


# In[101]:


World_cup.tail()


# In[102]:


goal_scorers.head()


# In[103]:


fifa_2022_ranking.head()


# In[104]:


World_cup.info()


# In[105]:


goal_scorers.info()


# In[106]:


fifa_2022_ranking.info()


# ### Analysis of Hosting by Continents

# In[107]:


host_continent_num = World_cup['Host Continent'].value_counts().reset_index()
host_continent_num.columns = ['Host Continent','Count']



host_continent_num


# In[108]:


sns.barplot(data=host_continent_num, x='Host Continent',y='Count',palette = 'viridis')



plt.title('Number of World Cup Host By Continent')
plt.xlabel('Host Continent')
plt.ylabel('Number of Host')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ### Top 5 Winning Countries (2022)

# In[109]:


country_win = World_cup['Winner'].value_counts().reset_index().head(5)
country_win.columns = ['Country', 'Wins']



country_win


# In[120]:


sns.barplot(x='Wins',y='Country',data=country_win,palette='viridis', hue='Wins', dodge=False)
            
plt.title('Top 5 Champions')
plt.tight_layout()
plt.show()


# ### Top 5 Runners-up (2nd placed)

# In[121]:


country_win = World_cup['Runners-Up'].value_counts().reset_index().head(5)
country_win.columns = ['Country', 'Count']



country_win


# In[125]:


sns.barplot(x='Count',y='Country',data=country_win,palette='viridis',hue='Count',dodge=False)
            
plt.title('Top 5 Runners-up')
plt.tight_layout()
plt.show()


# ### Top Goal Scorers

# In[141]:


top_scorers = goal_scorers[['Player','Goals']].head(5)
top_scorers


# In[143]:


plt.figure(figsize=(8, 8))

plt.pie(top_scorers['Goals'], labels=top_scorers['Player'], autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)

plt.title('Top 5 Scorers in FIFA World Cup History')
plt.axis('equal')  
plt.show()


# ### Matches Per Tournament

# In[152]:


matches_per_year = World_cup[['Year','Matches Played']]
matches_per_year


# In[153]:


plt.figure(figsize=(10,6))
sns.lineplot(x='Year',y='Matches Played',data=World_cup,marker='o')
plt.title('Number of Matches per Year')
plt.xlabel('Year')
plt.ylabel('Number of Matches')
plt.show()


# ### Goals scored per Tournament

# In[185]:


plt.figure(figsize=(10, 6))
goal_scored1 = World_cup[['Year','Goals Scored']].tail()
sns.barplot(data=goal_scored1, x='Year', y='Goals Scored', palette='viridis')
plt.title('Goals Scored in last 5 tournaments')
plt.show()


# In[ ]:




