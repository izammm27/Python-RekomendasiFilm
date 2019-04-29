#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


# In[2]:


#masukan data CSV movie
movie = pd.read_csv(r"C:\Users\Kodeic\Documents\Python\the-movies-dataset\movies_metadata.csv")
movie.dtypes


# In[3]:


#convert id to float64 agar sama dengan tipe data CSV Link
movie['id'] = pd.to_numeric(movie['id'], errors='coerce')
movie.dtypes


# In[4]:


#ganti nama id ke tmdbID agar sesuai dengan nama kolom di Data CSV Link
movie_rename = movie.rename(index=float, columns={"id": "tmdbId"})
movie_rename.columns


# In[5]:


#untuk mensortir hanya kolom title dan tmdbId saja yang diambil
movie_loc = movie_rename.loc[:,["title","tmdbId"]]
movie_loc.head(5)


# In[6]:


#masukan data CSV Link
link = pd.read_csv(r"C:\Users\Kodeic\Documents\Python\the-movies-dataset\links.csv")
link.dtypes


# In[7]:


#untuk mensortir hanya kolom movieID dan tmdbId saja yang diambil
link_loc = link.loc[:,["movieId","tmdbId"]]
link_loc.head(5)


# In[8]:


#gabungkan Data movie_loc dan Data link_loc
data1 = pd.merge(movie_loc,link_loc)
data1.head(5)


# In[9]:


#masukan data CSV rating
rating = pd.read_csv(r"C:\Users\Kodeic\Documents\Python\the-movies-dataset\ratings.csv")
rating.dtypes


# In[10]:


#gabungkan Data1 (yang telah di merge sebelumnya) dengan Data Rating
data2 = pd.merge(data1,rating)
pd.DataFrame(data2.head(5))


# In[11]:


#lihat berapa data yang terbentuk dari penggabungan table tsb
data2.shape


# In[12]:


#lalu ambil lah 1juta data karena kalo terlalu banyak tidak bisa
data3 = data2.iloc[:1000000,:]
data3.shape


# In[13]:


#Bikin pivot table dengan masukan Data dari Data3 , tetapkan rating sebagai nilai values, titel sebagai kolom, dan user ID sebagai indeks
pivot_table = data3.pivot_table(values='rating', index=['userId'],columns=['title'], aggfunc=np.sum, fill_value=0)
pivot_table.head(100)


# In[14]:


#Masukan Title Film pada pivot table untuk menkompare dari Nilai yg lainnya
movie_watched = pivot_table["Pocahontas"] #masukan Title Film yg ingin dicari
similarity_with_other_movies = pivot_table.corrwith(movie_watched)
#Mencari kolerasi antara Title Film yang telah dimasukan dengan Title Film Lain
similarity_with_other_movies = similarity_with_other_movies.sort_values(ascending=False)
result = similarity_with_other_movies.head()
print (result.head())#untuk melihat / mencetak rekomendasi dengan Title Film Lain  
                     #semakin mendekati nilai angka 1 pada Title Film yang di input maka film tersebut semakin di rekomendasikan sesuai berurutan


# In[15]:


#Untuk melihat hasil Grafik Film yang direkomendasikan sesuai urutan dengan Title FIlm yang telah di input.
result.plot(kind='bar',colormap='cool')


# In[ ]:




