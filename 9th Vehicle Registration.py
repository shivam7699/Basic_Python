#!/usr/bin/env python
# coding: utf-8

# In[15]:


n=input('enter number: ')
if len(n)==10:
    sc=n[0:2]
    rto=n[2:4]
    series=n[4:6] 
    number=n[6:10]

    x= sc.isalpha()
    y= rto.isnumeric()
    z= series.isalpha()
    num= number.isnumeric()

    if not x== True:
        print('invalid')
    elif not y==True:
        print('invalid')
    elif not z== True:
        print('invalid')
    elif not num == True:
        print('invalid')
    else:
        print('valid')
else:
    print('invalid')

