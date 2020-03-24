
'''

This file shows the map how many were confirmed in China for each province on date before '3/10/2020'

@author: Di Guan

'''


import pandas as pd
import plotly.graph_objects as go
import plotly as py


def bubble_map(confirmed,date):
    
    '''
    plot the map how many were confirmed in China for each province on specific date
    '''
    
    #assert statement
    assert type(confirmed)==pd.core.frame.DataFrame
    assert isinstance(date,str)
    
    #set the confirmed cases to 7000 for Hubei province, of which the index is 12
    confirmed.at[12,date]=7000
    
    #set limits and corresponding colors and the bubble area scale
    limits = [(2000,100000),(900,2000),(300,900),(100,300),(0,100)]
    colors = ["crimson","orange","yellow","lightyellow","lightgrey",]
    scale = 2

    fig = go.Figure()

    #add trace for each province within limits
    for i in range(len(limits)):
        lim = limits[i]
        df_sub=confirmed.loc[confirmed[date]<lim[1]]
        fig.add_trace(go.Scattergeo(
            locationmode = 'USA-states',
            lon = df_sub['Long'],
            lat = df_sub['Lat'],
            hoverinfo = 'text',
            text = df_sub[['Province/State',date]],
            #text = df_sub['text'],
            marker = dict(
                size = df_sub[date]/scale,
                color = colors[i],
                line_color='rgb(40,40,40)',
                line_width=0.5,
                sizemode = 'area'
            ),
            name = '{0} - {1}'.format(lim[0],lim[1])))
    
    #update the layout
    fig.update_layout(
        title_text = date,
        showlegend = True,
        geo = dict(
            scope = 'asia',
            landcolor = 'rgb(243, 243, 243)'
        ),
        margin={'l':50,'r':50,'t':50,'b':0}
    )
    
    fig.show()
    
    py.offline.plot(fig,filename='plots/china_confirmed_case_map.html')
    
    return confirmed


def main():
    
    #import data and sort data
    confirmed = pd.read_csv('../data/time_series_19-covid-Confirmed.csv')
    #date can be set any date between '1/23/2020' and '3/10/2020'
    date='3/10/2020'
    confirmed =confirmed.head(31).sort_values(date,ascending=False)
    
    #plot the bubble map of confirmed case in China
    bubble_map(confirmed,date)
    

if __name__ == '__main__':
    main()

