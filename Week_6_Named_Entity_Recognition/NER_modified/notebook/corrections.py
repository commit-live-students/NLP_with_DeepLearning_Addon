
# coding: utf-8

# In[8]:


import re
def checkEmailRegex(regex):
    text = "Please write to us at Ask_info1@grayatom.com"
    try:
    	email = re.search(regex,text).group()
    except :
    	return "The regex is Incorrect. Please try again"
    if email == "Ask_info1@grayatom.com":
        return "Congratulations!!! You have successfully completed this exercise. Great work"
    else: return "The regex is Incorrect. Please try again"

