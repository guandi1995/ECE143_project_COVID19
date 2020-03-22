#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''

This file plots the railway network departure from wuhan

@ Di Guan

'''


import pandas as pd
import plotly.graph_objects as go
import plotly as py


def railway_flow(places):
    
    '''
    
    plot the railway network departure from wuhan
    
    '''
    
    places=places.sort_values('cnt',ascending=False).reset_index(drop=True)
    
    
    fig = go.Figure()
    
    
    fig.add_trace(go.Scattergeo(
        locationmode = 'USA-states',
        lon = places['long'],
        lat = places['lat'],
        hoverinfo = 'text',
        text = places['name'],
        mode = 'markers',
        marker = dict(
            size = 3,
            color = 'rgb(255, 0, 0)',
            line = dict(
                width = 3,
                color = 'rgba(68, 68, 68, 0)'
            )
        )))

    
    for i in range(len(places)):
        fig.add_trace(
            go.Scattergeo(
                lon = [114, places['long'][i]],
                lat = [31, places['lat'][i]],
                mode = 'lines',
                hoverinfo = 'text',
                text = places['name'][i],
                line = dict(width = 1,color = 'red'),
                opacity = float(places['cnt'][i]) / float(places['cnt'].max()),
                name=places['name'][i]
            )
        ) 

    fig.update_layout(
        title_text = 'Railways Departure From Wuhan',
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



def main():
    #from url=https://www.travelchinaguide.com/china-trains/wuhan-schedule.htm
    places=pd.DataFrame([
                             ['guangzhou',113.3,23.1,66+34],
                             ['shenzhen',114.1,22.5,26+7],
                             ['huanggang',114.9,30.4,14],
                             ['beijing',116.4,39.9,32+27],
                             ['shanghai',121.5,31.2,35+6],
                             ['yichang',111.3,30.7,9],
                             ['zhengzhou',113.6,34.7,85+42],
                             ['lanzhou',103.8,36.1,6],
                             ['nanchang',115.9,28.7,6],
                             ["xi'an",109,34.3,44+11],
                             ['fuzhou',119.3,26.1,5],
                             ['chengdu',104.1,30.6,16+10],
                             ['yangxin',115.2,29.8,4],
                             ['hangzhou',120.2,30.3,12+8],
                             ['nanjing',118.8,32.1,59],
                             ['xiamen',118.1,24.5,3],
                             ['qingdao',120.4,36.1,3],
                             ['kunming',102.8,24.9,3],
                             ['nanning',108.4,22.8,7],
                             ['nanchang',115.9,28.7,20],
                             ['jinan',117.1,36.7,2],
                             ['guiyang',106.6,26.6,5],
                             ['changsha',112.9,28.2,103+52],
                             ['chongqing',106.9,29.4,38+7],
                             ['tianjin',117.4,39.3,8],
                             ['wenzhou',120.7,28,2],
                             ['harbin',126.5,45.8,1+3],
                             ['xinyang',114.1,32.1,1],
                             ['shenyang',123.4,41.8,4],
                             ['hongkong',114.2,22.3,2],
                             ['futian',114.1,22.5,26],
                             ['xianning',114.3,29.8,58],
                             ['shiyan',110.8,32.6,13+9]
                            ],columns=['name','long','lat','cnt'])
    
    fig=railway_flow(places)
    py.offline.plot(fig,filename='plots/railway_network.html')
    
if __name__ == '__main__':
    main()


# In[ ]:




