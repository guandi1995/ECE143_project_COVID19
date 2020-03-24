
"""

This file calculates the daily confirmed cases increment for each province

plot the daily increment for each province except Hubei in one graph

and daily increment for each province over time can be checked separately by dropdown box

based on the daily increment over time for each province, average daily increment is computed and ranked

finally, make a scatter plot wrt population and average daily increment for each province

@ Di Guan


"""


import pandas as pd
import plotly.express as px
import plotly as py
import numpy as np
import plotly.graph_objects as go

    
def daily_increment_each_province(confirmed_china):
    
    '''
    
    check the status of daily increment in each province in china
    
    transfer the dataframe from the structure of 
    
    province--country--lat--long--1/22/20--1/23/20.....3/21/20
    .......   ......   ..   ...     ...      ...        ...
    .......   ......   ..   ...     ...      ...        ...
    .......   ......   ..   ...     ...      ...        ...
    
    
    to the structure of 
    
    date     hubei guangdong henan zhejiang
    1/22/20   ..     ..       ..      ..
    1/23/20   ..     ..       ..      ..
    ...
    
    3/21/20   ..     ..       ..      ..
    
    which records the daily increment for each province
    
    '''
    
    
    #get date in the columns: 1/22/20,.....,3/21/20
    index = confirmed_china.columns[4:]
    #convert the type from index to array
    index = np.array(index)
    
    #get the province names in china
    province_name = confirmed_china['Province/State']
    #convert it to array type
    province_name = np.array(province_name)

    all_province_record = index
    
    #select each province
    for j in range(len(confirmed_china)):
        
        #get confirmed case time series for each province
        province=confirmed_china.loc[j][4:]
        #initialize the daily increment for specific province
        increase_daily_province=len(province)*[0]
        
        #get daily increment for each date after day 1
        for i in range(len(province)):
            
            if i >0:
                increase_daily_province[i] = province[i] - province[i-1]
                
            increase_daily_province = np.array(increase_daily_province)

        all_province_record = np.column_stack((all_province_record,increase_daily_province))


    #convert the stacked array to dataframe
    all_province_record=pd.DataFrame(all_province_record)
    #set the index of the dataframe
    all_province_record.set_index(index)
    #append columns name
    all_province_record.columns=np.append('date',province_name)
    
    return all_province_record,province_name


def plot_daily_increment_for_all_except_hubei(all_province_record):
    
    '''
    
    plot the daily increment for all province except Hubei in one graph
    
    '''
    #drop the columns of Hubei 
    all_province_record_except_hubei=all_province_record.drop(columns='Hubei')
    
    #melt the data
    all_province_record_transform = all_province_record_except_hubei.melt(id_vars="date")
    all_province_record_transform=all_province_record_transform.rename(columns={'variable': 'Provinces',
                                                                                'value':'daily increment'})
    
    #plot the graph
    fig = px.line(all_province_record_transform, 
                         x="date", 
                         y="daily increment", 
                         color="Provinces")
    fig.update_layout(title="Daily Increment for All Province except Hubei")
    fig.show()
    
    py.offline.plot(fig,filename='plots/daily_increment_combine.html')
    
    
def avg_daily_increment_rank(all_province_record):
    
    '''
    
    rank the average daily increment among all province except Hubei province
    
    transform the all_province_record structure of 
    
    date     hubei guangdong henan zhejiang
    1/22/20   ..     ..       ..      ..
    1/23/20   ..     ..       ..      ..
    ...
    
    3/21/20   ..     ..       ..      ..
    
    to the variable avg_increase_province, with structure of 
    
    index provinces avg_daily_increment
     0       ..
     1       ..
     ..      ..
     ..
     31      ..
    
    '''
    
    #drop the columns of hubei
    all_province_record_except_hubei=all_province_record.drop('Hubei',axis=1)
    #calculate the mean for each column
    avg_increase_province=all_province_record[all_province_record_except_hubei.columns[1:]].mean(axis=0)
    #convert it to the dataframe type
    avg_increase_province=avg_increase_province.to_frame()
    #add column name
    avg_increase_province.columns=['average_daily_increasement']
    #sort the dataframe descending
    avg_increase_province=avg_increase_province.sort_values('average_daily_increasement',ascending=True)
    
    #reset index and rename the columns
    avg_increase_province.reset_index(inplace=True)
    avg_increase_province=avg_increase_province.rename(columns={'index':'provinces'})
    
    #plot the bar chart
    fig = px.bar(avg_increase_province, 
                 x='average_daily_increasement',
                 y='provinces',
                 labels={'y':'Province(Except Hubei)',
                         'average_daily_increasement':'Average Daily Increasement'},
                 color='average_daily_increasement',
                 orientation='h',
                 height=700)

    fig.update_layout(title_text='Average Daily Increasement for each province except Hubei')
    fig.show()
    
    py.offline.plot(fig,filename='plots/avg_daily_increment_rank.html')
    
    
    return avg_increase_province



def daily_increment_status_each_province(all_province_record,province_name):
    
    """
    choose different province name to check the status of daily increment in that province
    
    select the dropdown box and choose to see the status of every province
    
    """
    

    #all_province_record=all_province_record.drop('Hubei',axis=1)
    
    fig = go.Figure()
    
    #add trace for each province
    for i in province_name:
        
        #invisible for Hubei Province in main
        visible=True
        if i == 'Hubei':
            visible=False
            
        fig.add_trace(
            go.Scatter(
                x=all_province_record['date'],
                y=all_province_record[i],
                mode="lines+markers",
                name=i,
                visible=visible,
                
            )
        )

    
    #define annotation,visible and button_pro function
    annotation={}
    visible={}
    buttons_pro={}
    for i in province_name:
        annotation[i]=[dict(x=all_province_record['date'],
                       y=all_province_record[i])]
        visible[i]=list(province_name==i)
        buttons_pro[i]=dict(label=i,
                         method="update",
                         args=[{"visible": visible[i]},
                               {"title": "Daily Increment in "+i+" Province",
                                "annotations": annotation[i] }])

    
    #add layout
    fig.update_layout(
        updatemenus=[
            dict(
                active=0,
                buttons=list([
                    buttons_pro[i] for i in province_name
                ]),
        )
    ])
    
    fig.show()
    
    py.offline.plot(fig,filename='plots/daily_increment_separate.html')
    
    
def population_vs_avg_daily_increment(population,avg_increase_province):
    
    """
    
    plot the relationship with population and average daily increment for each province except Hubei and Taiwan
    
    the data of population and avg_increase_province are needed to be reorganized and concated together
    
    
    """
    
    #drop Hubei and Taiwan in population, reorder the data by the columns 'Province', ordered from A to Z
    population_withoutWuhan=population.drop([12,31])
    population_withoutWuhan.sort_values(by='Province', inplace=True)
    population_withoutWuhan.reset_index(inplace=True)
    
    #reorder the data by the columns 'provinces', ordered from A to Z
    avg_increase_province.sort_values(by='provinces' , inplace=True)
    avg_increase_province.reset_index(inplace=True)
    
    #concat those two dataframe horizontally
    df=pd.concat([population_withoutWuhan, avg_increase_province], axis=1)

    #plot the scatter plot
    fig = go.Figure(data=go.Scatter(x=df['Population(million)'],
                                    y=df['average_daily_increasement'],
                                    mode='markers+text',
                                    marker_color=df['Population(million)'],
                                    text=df['Province'],# hover text goes here
                                    textposition='bottom center',
                                    )) 
    fig.update_layout(
        title="Population versus. Average Daily Increment for each province",
        xaxis_title="Population(million)",
        yaxis_title="Average Daily Increment"
    )
    
    fig.show()
    
    py.offline.plot(fig,filename='plots/population_vs_avg_increment.html')
    
    
    
def main():
    
    #import the data
    data=pd.read_csv('../data/time_series_19-covid-Confirmed_3_22.csv')
    population=pd.read_csv('../data/china_population.csv')

    #rechieve the confirmed cases in china
    confirmed_china = data.loc[data['Country/Region'] == 'China']
    confirmed_china = confirmed_china.set_index(np.arange(len(confirmed_china)))

    #calculate the daily increment for each province
    all_province_record,province_name = daily_increment_each_province(confirmed_china)

    #plot the daily increment for each province over time
    plot_daily_increment_for_all_except_hubei(all_province_record)

    #rank the average daily increment for each province
    avg_increase_province=avg_daily_increment_rank(all_province_record)

    #check the status of daily increment for each province with dropdown box
    daily_increment_status_each_province(all_province_record,province_name)

    #plot the scatter graph of population and average daily increment for each province
    population_vs_avg_daily_increment(population,avg_increase_province)
    
    
if __name__ == '__main__':
    
    main()



