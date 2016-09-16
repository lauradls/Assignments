
# coding: utf-8

# # HW 1
# 
# ## Problem 2 - CAPM_CALCULATOR

# In[1]:

beta = float(input("Please, enter beta: "))
Rm = 4.8
Rf = 1.705
Rp = Rf + beta*(Rm - Rf)
print("The expected return on the asset is", Rp, "percent")

