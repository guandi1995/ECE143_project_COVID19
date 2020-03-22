#!/usr/bin/env python
# coding: utf-8

# In[13]:


'''

This file make an animation illustrated how the virus grows over time around the world

@ Di Guan

'''


import pandas as pd
import plotly.express as px
import plotly as py
import numpy as np


def worldwide_growth_bubble_animation(data):
    '''
    
    animation of how it grows over time around the world
    
    the original data has the structure for each row as below:
    
    Pronvince/State--Country/Region--Lat--Long--1/22/2020 ........ 3/22/2020
    
    then, we transform the data structure to the form such as 
    
    Province/State--Country/Region--Lat--Long--1/22/2020
    Province/State--Country/Region--Lat--Long--1/23/2020
    .........
    Province/State--Country/Region--Lat--Long--3/22/2020
    
    then take the log value for each date
    
    '''
    
    #melt the dataframe 
    tidy_df = data.melt(id_vars=["Province/State","Country/Region","Lat","Long"],var_name="Date",value_name="value")
    
    #take the log and add the log value to the dataframe
    log_value=(tidy_df.value+1).apply(np.log10)
    tidy_df['log_value']=log_value

    #make the animation
    fig_growth = px.scatter_geo(tidy_df, 
                                lat=tidy_df['Lat'],
                                lon=tidy_df['Long'],
                                hover_name="Country/Region", 
                                size="log_value",
                                animation_frame='Date',
                                projection="natural earth",
                                title="Spread Across The World")

    fig_growth.show()
    
    return fig_growth
    
def main():
    #import data from github
    data = pd.read_csv('../data/time_series_19-covid-Confirmed_3_22.csv')

    #animation of how it grows over time around the world
    fig=worldwide_growth_bubble_animation(data)
    py.offline.plot(fig,filename='plots/worldwide_growth_animation.html')
    
if __name__ == '__main__':
    main()


# In[ ]:




