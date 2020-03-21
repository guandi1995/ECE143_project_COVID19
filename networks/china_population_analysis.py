#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''

This file plots the China population map and the population rank for each province in China

@author: Di Guan

'''


import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly as py

def population_bubble_map(population):
    
    '''
    plot China population map in million
    '''
    
    ##assert statements
    assert type(population)==pd.core.frame.DataFrame
    
    limits = [(90,120),(60,90),(40,60),(20,40),(0,20)]
    colors = ["crimson","orange","yellow","lightyellow","lightgrey",]
    scale = 0.1

    fig = go.Figure()

    for i in range(len(limits)):
        lim = limits[i]
        df_sub=population.loc[population['Population(million)']<lim[1]]
        fig.add_trace(go.Scattergeo(
            locationmode = 'USA-states',
            lon = df_sub['Long'],
            lat = df_sub['Lat'],
            hoverinfo = 'text',
            text = df_sub[['Province','Population(million)']],
            #text = df_sub['text'],
            marker = dict(
                size = df_sub['Population(million)']/scale,
                color = colors[i],
                line_color='rgb(40,40,40)',
                line_width=0.5,
                sizemode = 'area'
            ),
            name = '{0} - {1}'.format(lim[0],lim[1])))

    fig.update_layout(
        title_text = 'China Population Map (in million)',
        showlegend = True,
        geo = dict(
            scope = 'asia',
            landcolor = 'rgb(243, 243, 243)'
        ),
        margin={'l':50,'r':50,'t':50,'b':0},
    )
    
    fig.show()
    
    #save image to html file
    py.offline.plot(fig,filename='plots/china_population_geography.html')

    
def china_pop_bar(population):
    '''
    china population rank
    '''
    fig = px.bar(population,
                               x='Population(million)', 
                               y='Province',color='Population(million)',
                               orientation='h',title="China Population Rank",height=700)
    fig.show()
    py.offline.plot(fig,filename='plots/china_population_rank.html')
    
    
    
def main():
    #import data
    population = pd.read_csv('../data/china_population.csv')
    population =population.sort_values('Population(million)',ascending=True)

    #plot china population bubble map 
    population_bubble_map(population)

    #rank the population
    china_pop_bar(population)
    
    
    
if __name__ == '__main__':
    main()


# In[ ]:




