#!/usr/bin/env python
# coding: utf-8

# In[ ]:


name=input ('Enter your name: ')
print ('Welcome',name,'! This is your rewards tracker!') 

answer = input ('Do you want to check if you have earned your treat yet? \n (y) Yes \n (n) No \n\n Option:')
if answer == "y" : 
    days_since_last_treat =(input("How many days ago was your last treat? "))
    dsltft= int(days_since_last_treat)
    if dsltft < 10 :
        print ('Uh oh',name,'you have to wait a little longer!')
    else: 
        print ('\n Well done',name,'\n You can have a treat! \n Thats the summary of your rewards report. Thank you!')
else: 
  print ('Okay have a great day',name)


#  

# In[ ]:





# In[ ]:




