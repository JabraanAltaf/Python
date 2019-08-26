#!/usr/bin/env python
# coding: utf-8

# In[49]:


import requests


# In[50]:


url = "https://api.yelp.com/v3/businesses/search"
    
api_key = "tTmPcJxm5WwrPcgcX9jX6QIr140bLkxsSsEWEQZR-m5qknEISxNGa7I_20DPnOAZtl0cWh1qlWGNdUmr3_L5D72gFoH70xkD530Do9PAcTNpdzTGxnFBjsvPJwxkXXYx"

# Key and Value of main header request
headers = {
    "Authorization": "Bearer " + api_key
}    

# Parameters which the program will search for
params = {
    "location": "London",
    "term": "food"
}

# Response takes in a header and params variable
response = requests.get(url, headers = headers, params = params)
#print(response.text)
#print(response.json())

# Getting a json of all the food businesses 
foodPlaces = response.json()["businesses"]
#print(business)

# Printing out all the names of the food placess
for place in foodPlaces:
    print(place["name"])




# In[51]:


# Find places rated 3.5 or better and store them in a list
wellRated = [place["name"] + " " + str(place["rating"]) for place in foodPlaces if place["rating"] > 3.5]
#print(wellRated)

# Print the name and rating of the first place in the list
print(wellRated[0])


# In[ ]:





# In[ ]:




