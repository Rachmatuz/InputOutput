#!/usr/bin/env python
# coding: utf-8

# Nilai statis dan dinamis

# In[7]:


bil1 = input('isikan bilangan 1: ')
bil2 = input('isikan bilangan 2: ')
hasil = int(bil1) + int(bil2)
print("hasil penjumlahan dari?",bil1,"+",bil2,"=",hasil)


# buatlah luas dan keliling persegi panjang

# In[12]:


panjang = input("masukan nilai panjang : ")
lebar = input("masukan nilai lebar : ")

luas= int  (panjang)* int(lebar)
keliling= 2 * int(panjang) + int(lebar)

print("luas persegi panjang :",luas)
print("keliling persegi panjang : ",keliling)


# In[13]:


print("A","B","C","D", sep='@_@') #sep=separator atau pembatas


# In[14]:


print("A","B","C","D", sep='\n', end='>_<')


# In[16]:


print("rachmatu","rahma","bela","alya","nazilah", sep='\n', end='>_<')


# format index

# In[17]:


num_1 = 8
num_2 = 10

# Hasil dari 8 modulus 10 = 8
#str.format()
print('hasil dari {} modulus {} = {}'.format(num_1,num_2,num_1%num_2))


# In[21]:


fname = "Rachmatu"
mname = "zabila"
lname = "khaerunissa"

print('Nama anda {0} {2} {1}'.format(fname,mname,lname))


# menggunakan tanda pengenal

# In[22]:


print('Nama anda {nama}, nilai anda {nilai}'.format(nama='Aira',nilai=99))


# In[28]:


univ = "Universitas Nusa Putra"

print("karakter pertama : ",univ[0])
print("karakter terakhir : ",univ[-1])
#universitas
print(univ[0:11])
print(univ[-5 :])
print(univ[17:])
print(univ[::-1])


# f string

# In[35]:


f_name = 'sabella khaerinussa aufa julianto rachmatu alya'
l_name = 'sapitri fauziah kinaras syuhada zabila hendrawan'

print(f'Nama saya {f_name} {l_name}')

first = 100
second = 20
print(f'Hasil penjumlahan {first} + {second} = {first+second}')


# split pada string

# In[34]:


nama = "Alya,Nazilah,rahma"
nama2 = "Alya Nazilah Rahma"
print(nama.split())
print(nama.split(','))

#join
print('@'.join(nama.split(',')))

#input tgl lahir -> 18/oktober/2010
#input nama -> Bill Gate
#output:
#Tgl : 18, bulan:oktober, Tahun :2010
#Nama Insial : BG


# In[45]:


tgl = input ('masukan tanggal : ')
nama = input ('masukan nama : ')

pemisah = tgl.split("/")
print(f'tgl: {pemisah[0]},bulan: {pemisah[1]},tahun: {pemisah[2]}')
pemisah2 = nama.split()
nama_pertama = pemisah2[0]
nama_terakhir = pemisah2[1]
print(f'Nama Inisial: {nama_pertama[0]+nama_terakhir[0]}')


# In[ ]:





# In[ ]:




