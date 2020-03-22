#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''

This file plot domestic and international flight network departure from wuhan 

@ Di Guan

'''


import pandas as pd
import plotly.graph_objects as go
import plotly as py


def flight_flow(domestic,inter):
    
    '''
    
    plot flight network departure from Wuhan domestically and internationally
    when inter is empty, then plot domestic flight only,
    otherwise, plot international flight
    
    '''
    
    flight_destination=domestic.append(inter,sort=False)
    
    fig = go.Figure()
    fig.add_trace(go.Scattergeo(
        locationmode = 'USA-states',
        lon = flight_destination['longitude'],
        lat = flight_destination['latitude'],
        hoverinfo = 'text',
        text = flight_destination['destination'],
        mode = 'markers',
        name='Destinations:',
        marker = dict(
            size = 3,
            #color='blue',
            color = 'rgb(255, 0, 0)',
            line = dict(
                width = 3,
                #color='black'
                color = 'rgba(68, 68, 68, 0)'
            )
        )))

    
    #add trace for each destination, with lines mode
    for i in range(len(flight_destination)):
        fig.add_trace(
            go.Scattergeo(
                lon = [flight_destination['longitude'][0], flight_destination['longitude'][i]],
                lat = [flight_destination['latitude'][0], flight_destination['latitude'][i]],
                mode = 'lines',
                hoverinfo = 'text',
                text = flight_destination['destination'][i],
                line = dict(width = 1,color = 'red'),
                opacity = float(flight_destination['passengers'][i] / flight_destination['passengers'].max()),
                name=flight_destination['destination'][i]
            )
        ) 

    #plot the international flight departure from wuhan
    if domestic is empty:
        fig.update_layout(
            title_text = 'International Flights Departure from Wuhan',
            geo = dict(
                scope = 'world',
                projection_type = 'orthographic',
                showland = True,
                landcolor = 'rgb(243, 243, 243)',
                countrycolor = 'rgb(204, 204, 204)',
            ),
            margin={'l':0,'r':50,'t':50,'b':0}
        )
        
    #plot the domestic flight departure from wuhan
    else:
        fig.update_layout(
            title_text = 'Domestic Flights Departure from Wuhan',
            geo = dict(
                scope = 'asia',
                projection_type = 'equirectangular',
                showland = True,
                landcolor = 'rgb(243, 243, 243)',
                countrycolor = 'rgb(204, 204, 204)',
            ),
            margin={'l':0,'r':50,'t':50,'b':0}
        )
    
    fig.show()
    
    return fig

    
#import international and domestic data
flight_destination_domestic = pd.read_csv('../data/flight_from_wuhan_domestic.csv')
flight_destination_inter = pd.read_csv('../data/flight_from_wuhan_international.csv')

empty=pd.DataFrame(columns = None)

#plot domestic flight
fig=flight_flow(flight_destination_domestic,empty)
py.offline.plot(fig,filename='plots/domestic_flight.html')

#plot international flight
fig=flight_flow(empty,flight_destination_inter)
py.offline.plot(fig,filename='plots/international_flight.html')


# In[ ]:




