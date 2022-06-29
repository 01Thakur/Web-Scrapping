#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[35]:


from bs4 import BeautifulSoup
import requests
import re
import pandas as pd


# Write a python program to display all the header tags from wikipedia.org.

# In[2]:


page = requests.get('https://en.wikipedia.org/wiki/Main_Page')


# In[3]:


page


# In[4]:


Soup = BeautifulSoup(page.content)
Soup


# In[5]:


first_title = Soup.find('span' ,class_="mw-headline")
first_title.text


# In[6]:


Header = []

for i in Soup.find_all('span' ,class_="mw-headline"):
    Header.append(i.text)
    
Header


# Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year of release)
# and make data frame.

# In[7]:


page = requests.get('https://www.imdb.com/chart/top/')
page


# In[8]:


Soup = BeautifulSoup(page.content, "html.parser")
print(Soup.prettify())


# In[65]:


movies = Soup.find_all('tbody' ,class_="lister-list")
movies


# In[70]:


for Movie in movies:
    
    Name = Movie.find('td',class_="titleColumn").a.text
    
    Rank = Movie.find('td',class_="titleColumn").get_text(strip=True).split('.')[0]
    
    Year = Movie.find('td',class_="titleColumn").span.text.strip("()")
    
    Rating = Movie.find('td',class_="ratingColumn imdbRating").strong.text
    
    print(Rank, Name, Rating, Year)  


# In[71]:


Movies_DF = pd.DataFrame({'Rank': Rank, 'Movie Name': Name, 'Year': Year, 'Rating': Rating}, index=[0])
Movies_DF


# In[ ]:




