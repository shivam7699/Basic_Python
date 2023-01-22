#!/usr/bin/env python
# coding: utf-8

# In[1]:


L = [1,2,4,8,16,32,64,128,256,512,1024,32768,65536,4294967296] 


# In[2]:


s=[]
d=[]
t=[]
f=[]
fi=[]
si=[]
se=[]
ei=[]
ni=[]
te=[]
all=[s,d,t,f,fi,si,se,ei,ni,te]
for i in L:
    if i<10:
        s.append(i)
    elif i<100:
        d.append(i)
    elif i<1000:
        t.append(i)
    elif i<10000:
        f.append(i)
    elif i<100000:
        fi.append(i)
    elif i<1000000:
        si.append(i)
    elif i<10000000:
        se.append(i)
    elif i<10000000:
        ei.append(i)
    elif i<100000000:
        ni.append(i)
    elif i<10000000000:
        te.append(i)
print(all)


# In[21]:


a=range(1,11,1)
all
dictionary = dict(zip(a, all))

rem_key = dictionary.pop(6)
rem_key = dictionary.pop(7)
rem_key = dictionary.pop(8)
rem_key = dictionary.pop(9) 
print(dictionary)


# In[ ]:





# In[ ]:





# In[ ]:





# In[23]:


# practice


# In[22]:


a=[]
t=10
for i in L:
    if i<t:
        a.append(i) 
        t=t*10
a


# In[ ]:





# In[ ]:





# In[ ]:




