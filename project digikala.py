#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install selenium


# In[2]:


import selenium


# In[ ]:


from selenium import webdriver


# In[17]:


import time


# In[25]:


mororgar=webdriver.Firefox()


# In[26]:


mororgar.get('https://www.digikala.com/users/login/?backUrl=/')


# In[27]:


shomareh='09367870938'


# In[28]:


inputtext=mororgar.find_element(by='name',value='username')


# In[10]:


inputtext.send_keys(shomareh)


# In[11]:


buttonvorod=mororgar.find_element(by='xpath',value='/html/body/div[1]/main/div[2]/form/button')


# In[12]:


buttonvorod.click()


# In[13]:


codetaaeed=input('input the code')


# In[14]:


inputsms=mororgar.find_element(by='xpath',value='/html/body/div[1]/main/div[2]/form/label/div/div/input')


# In[15]:


inputsms.send_keys(codetaaeed)


# In[18]:


time.sleep(5)


# In[19]:


mororgar.get('https://www.digikala.com/profile/')


# In[20]:


txtshomareh=mororgar.find_element(by='xpath',value='//*[@id="profileLayoutContainer"]/div/div[2]/div[1]/div[1]/div/div[2]/p[2]')


# In[21]:


shomarehakhar=txtshomareh.text


# In[22]:


if int(shomarehakhar)==int(shomareh):
    print('the test is successful for ',shomareh)
else:
     print('test was not good')

  

        


# In[ ]:





# In[ ]:




