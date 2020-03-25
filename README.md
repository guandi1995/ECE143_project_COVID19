# ECE143_project_COVID19

Winter 2020 UCSD ECE143

The scope of the project is the demographic analysis of Coronavirus, especially in China. 

The files include the codes and the outputs graphs of the project


Team members:
-
- Di Guan
- Song Wang
- Vinamr Madan
- Yashdeep Singh

Motivations:
-
- Coronavirus outbreak, originated from Wuhan, Hubei Province, China in early December
- Difficult to detect 
- No vaccine yet

Objectives:
-
- Analyze how the virus spread in China and outside China
- Impact of population density and transportation networks on the outbreak
- who is impacted the most?


Topic 1: Growth over time in China and outside China
- 
- Growth in China and outside China

![growth_around_world](https://user-images.githubusercontent.com/53081268/77389407-5a6b1580-6d50-11ea-8f65-6df7073ec210.png)

- Growth animation around the world

![worldwide_animation](https://user-images.githubusercontent.com/53081268/77389479-900ffe80-6d50-11ea-8a03-454e45116949.png)

- Daily Increment for all provinces

Based on the growth over time around the world, we want to further analyze how it grows in China specificly. The graph below demonstrates the daily increment for each province except Hubei Province and then calulates the average daily increment for each province so that we can rank them and find out which provinces are the most serious infected areas around China except the origin of the virus, Hubei Province

![daily_increment_combine](https://user-images.githubusercontent.com/53081268/77393632-ab800700-6d5a-11ea-884e-990dfe194bca.png)

![avg_increment_rank](https://user-images.githubusercontent.com/53081268/77468719-3698e580-6dcb-11ea-89db-b3f4946afd86.png)

From the graph above obtained, the top 3 most serious infected areas except Hubei Province are Guangdong, Henan, Zhejiang Provinces. 

- Check the trend of growth

To check the trend of growth around China, a dropdown box is created so that the daily increment for each province can be checked, which helps us deeply analyze how it grows in each province over time. 

Notice, the general trend of growth shows that the virus is under control around China because many provinces have almost zero daily increment those days after it reach the peak. 

Basically, the trend of the growth can be classified into two types. One is that the daily increment hits the peak, starts to converge to zero and then remains the status of almost zero increment those days. The other one is that it acts the same behavior as first one except that it starts to bounce back after converging to zero increment. The reason why this happens is partly because the provinces or areas of the second type is the major import provinces or areas that they are receiving enormous amounts of passengers outside of China at international airports and those passengers cause the increment of imported cases occured in those provinces.

For example, we declare three representative provinces classified as type-one growth, which are Hubei Province, the origin of the virus, and Henan and Anhui provinces, with rank #3 and #6 respectively in terms of average daily increment across China. Those three provinces indicate the growth that it starts to converge to zero increment after hitting the peaks till March 21, 2020, without significant bouce back. 

![daily_increment_hubei](https://user-images.githubusercontent.com/53081268/77393680-ce122000-6d5a-11ea-8cb9-be01790712cf.png)

![daily_increment_henan](https://user-images.githubusercontent.com/53081268/77394485-be93d680-6d5c-11ea-8449-ccd66646c62a.png)

![daily_increment_anhui](https://user-images.githubusercontent.com/53081268/77484749-8df97e80-6de8-11ea-9ab5-1f3258b1e868.png)

Then, three representative provinces are classified as type-two growth, which are Guangdong Province, rank #2 in terms of average daily increment across the nation, city of Beijing and Shanghai. Those three areas indicate that the growth starts to converge to zero increment after hitting the peaks for a certain peroid, and then it has signs that the daily increment bounces back. This is partly because Guangdong, Beijing and Shanghai are the major areas that absorb enormous amount of international passengers flying from other regions of world. 

![daily_increment_guangdong](https://user-images.githubusercontent.com/53081268/77393876-3f51d300-6d5b-11ea-9ca8-81ba27a1f05d.png)

![daily_increment_beijing](https://user-images.githubusercontent.com/53081268/77394143-d9198000-6d5b-11ea-915a-cc30511f7d83.png)

![daily_increment_shanghai](https://user-images.githubusercontent.com/53081268/77394152-db7bda00-6d5b-11ea-9c74-0a473ff08438.png)


Topic 2: Impact of population density and networks impact on outbreak
- 
- Confirmed cases recorded on 3/21/2020

The graph below records the amount of confirmed cases for each province till March 21, 2020 where the area of circles represents the confirmed cases proportionally. It makes sense for us that the provinces next to Hubei Province has been impacted badly and have relatively high amount of confirmed cases than other provinces do, but Guangdong Province, which is quite far from Hubei, is the most seriously infected area except Hubei. Our first thought is probably because of the population density as Guangdong Province has the top 1 population density around the nation with over 100 million people.

![china_confirmed_case_map](https://user-images.githubusercontent.com/53081268/77390796-3f020980-6d54-11ea-8700-f0259c78b30d.png)

- Population density map  and rank of China

Thus, we made a map that indicates the population distribution in China and the population rank for each province

![china_population_map](https://user-images.githubusercontent.com/53081268/77390612-c3a05800-6d53-11ea-952a-91bef498e717.png)

![china_population_rank](https://user-images.githubusercontent.com/53081268/77391065-031b7400-6d55-11ea-8e4c-910579617230.png)

- Population density versus average daily increment for each province

Then, we made a plot that demonstrates the relationship between population size and the average daily increment we just calculate for each province. It seems like they do have a positive linear relationship of small population size with low average daily increment and large population size with high average daily increment. However, if you classify all provinces into 3 clusters conditioned on the population size with 0-40, 40-80 and over 80, then you can observe some outlier provinces which are circled. Those outliers indicate that population size is not the major significant cause, so what makes this happen? Our next thought is probably because of the transportation networks that connect those outlier provinces with Hubei Province.

![population_vs_avg_increment](https://user-images.githubusercontent.com/53081268/77390636-d155dd80-6d53-11ea-8bc9-e22d6aa97e3d.png)

- Major transportations in China

Before moving on, it is necessary to address the background of major transportations in China. The major transportation tools that commute cities to cities in China are highways, railways and flights, as shown below. Since the data of highways that records the connections of Hubei to other provinces is hard to gather online, we only gather the data of railways and flights departure from Wuhan. The data was recorded before the city was lockdown on January 23, 2020.

image 4

- Railways departure from Wuhan before lockdown

The data of railways departure from Wuhan was gathered from https://www.travelchinaguide.com/china-trains/wuhan-schedule.htm and it recorded how many railways departure from Wuhan daily and the its destination. The opacity represents the proportion of the railways departure from Wuhan to the specific destination over the max values. 

![railway_networks](https://user-images.githubusercontent.com/53081268/77390703-fba79b00-6d53-11ea-9e14-77d5274f556b.png)

- Railways impacted on the average daily increment

Let's take the top 3 cities that have the most connections with Wuhan as our examples here. They are city of Changsha, Zhengzhou and Guangzhou, which are the major cities of Hunan, Henan and Guangdong Province. 

![population_vs_avg_increment_railway](https://user-images.githubusercontent.com/53081268/77390669-e5014400-6d53-11ea-9b7d-aac1c90bcfe6.png)

- Domestic Flight departure from Wuhan 

![domestic_flight](https://user-images.githubusercontent.com/53081268/77390877-7e305a80-6d54-11ea-9747-3a2890fee4c7.png)

- Flights impacted on the average daily increment

![population_vs_avg_increment_flights](https://user-images.githubusercontent.com/53081268/77390887-8ee0d080-6d54-11ea-8f04-6e6ef5c60de8.png)


- International Flight departure from Wuhan

![international_flight](https://user-images.githubusercontent.com/53081268/77390902-999b6580-6d54-11ea-9c5f-4722f16ac904.png)


Topic 3: Demographic analysis
-

