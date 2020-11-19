#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import xarray as xr
import numpy as np
import netCDF4
import matplotlib.pyplot as plt

from glob import glob




# In this case I was loading just one file
#NEMO = xr.open_dataset('/Users/marina/OneDrive - University of East Anglia/UEA/PostDoc/ELO/Science/Data/NEMO/20171230.nc')

# DEFINITIONS
# Directory where data is stored:
data_dir='/Users/marina/OneDrive - University of East Anglia/UEA/PostDoc/ELO/Science/Data/NEMO/'

#ELOx1_pos.latitude=[-10-10/60] # How to create something similar?
ELOx1_pos=[105+54/60,-10-10/60] # Glider Waypoints
ELOx2_pos=[106+32/60,-9-15/60]


# In[2]:


# Getting files list
all_files = glob(data_dir + '*.nc')


# Opening files at once
ds = xr.open_mfdataset(all_files)


# Files at waypoint ELOx1 - Loading everything salinity:
ELOx1_Nemodataset = ds.sel(latitude=ELOx1_pos[1],longitude=ELOx1_pos[0],method='nearest').compute()
# What is the difference between 'compute' and 'load'?


# Plotting
fig, axs = plt.subplots(nrows=1, ncols=2)


# In[3]:


# Creating figure and storing handles


# Does't give error, but doesn't plot:
ELOx1_Nemodataset.so.T.plot.contourf(ax=axs[0], levels=50, cmap=plt.cm.coolwarm)


# Nothing was plotted from the above line of code!

# In[4]:


# Works but not in subplot. Also, how to get axis handle?
ELOx1_Nemodataset.so.T.plot.contourf(levels=50, cmap=plt.cm.coolwarm)


# In[5]:


# Other ways that I could keep axis handle, but doens't work:
axs[0].contourf(ELOx1_Nemodataset.time,ELOx1_Nemodataset.depth,ELOx1_Nemodataset.so.T, 50, cmap=plt.cm.coolwarm)


# In[6]:


plt.show()


# In[ ]:




