#!/usr/bin/env python
# coding: utf-8

# In[23]:


from flask import Flask, request, render_template


# In[24]:


import joblib


# In[25]:


app = Flask(__name__)


# In[26]:


@app.route("/",methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        print(rates)
        model1 = joblib.load("regression")
        r1 = model1.predict([[rates]])
        model2 = joblib.load("tree")
        r2 = model2.predict([[rates]])
        return(render_template("index.html", result1 = r1, result2 = r2))
    else:
        return(render_template("index.html", result1 = "WAITING", result2 = "WAITING"))


# In[27]:


if __name__ == "__main__":
    app.run()


# In[ ]:




