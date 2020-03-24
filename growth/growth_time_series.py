'''

This file plots the daily growth around China and outside China

@ Di Guan

'''

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly as py
import numpy as np

def daily_growth_series(data,china=True,world=False):
    
    '''
    
    plot the daily growth for the confirmed case in china and outside china in separate graphs
    
    if the argument china=True, world=False, then plot the growth in china
    
    if the argument china=False, world=True, then plot the growth outside china
    
    '''
    
    #assert statement
    assert (china==True and world==False) or (china==False and world==True)
    
    fig = go.Figure()
    
    if china==True and world==False:
        
        #if china ==True and world==False, then filter the data that is in china
        confirmed=data.loc[data['Country/Region'] == 'China']
        plot_title='Coronavirus Growth over time in China'
        filepath='plots/growth_in_china.html'
    
    else:
        #if china ==False and world==True, then filter the data that is outside china
        confirmed=data.loc[data['Country/Region'] != 'China']
        plot_title='Coronavirus Growth over time outside China'
        filepath='plots/growth_outside_china.html'
    
    #calculate the sum for each date
    confirmed=confirmed.sum(axis=0,skipna=True)
    confirmed=confirmed[4:].to_frame()
    confirmed.columns=['Confirmed Cases']

    #plot the daily growth in china or around china
    fig.add_trace(go.Scatter(x=confirmed.index, 
                             y=confirmed['Confirmed Cases'],
                             mode='lines+markers'))
    
    fig.update_layout(title=plot_title,
                   xaxis_title='Date',
                   yaxis_title='Confirmed Cases')
    
    fig.show()
    
    py.offline.plot(fig,filename=filepath)
    
    return confirmed

def daily_growth_series_combine(confirmed_china,confirmed_world):
    
    '''
    take the inputs of confirmed case in china and outside china 
    
    plot the growth seperately in the same graph
    '''
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(x=confirmed_china.index, 
                             y=confirmed_china['Confirmed Cases'],
                             mode='lines+markers',name='In China'))
    
    fig.add_trace(go.Scatter(x=confirmed_world.index, 
                             y=confirmed_world['Confirmed Cases'],
                             mode='lines+markers',name='Outside China'))
    
    fig.update_layout(title='Coronavirus Growth around the world',
                   xaxis_title='Date',
                   yaxis_title='Confirmed Cases')
    
    fig.show()
    
    py.offline.plot(fig,filename='plots/growth_around_world.html')
    
    
def main():
    
    #import the data 
    data = pd.read_csv('../data/time_series_19-covid-Confirmed_3_22.csv')
    
    #plot the growth in China
    confirmed_china=daily_growth_series(data,china=True,world=False)
    
    #plot the growth outside China
    confirmed_world=daily_growth_series(data,china=False,world=True)
    
    #plot the growth in china and outside china in the same graph
    daily_growth_series_combine(confirmed_china,confirmed_world)
    
    
if __name__ == '__main__':
    main()    
