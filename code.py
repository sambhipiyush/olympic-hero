# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)

data.rename(columns={'Total': 'Total_Medals'}, inplace=True)

data.head(10)


# --------------
#Code starts here




data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'], 'Summer', (np.where(data['Total_Summer'] < data['Total_Winter'], 'Winter', 'Both')))


better_event = data['Better_Event'].value_counts().idxmax()

print(better_event)




# --------------
#Code starts here

top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]

top_countries.drop(top_countries.tail(1).index, inplace=True)

def top_ten(top_countries_df, col):
    country_list = pd.DataFrame()
    country_list = top_countries_df.nlargest(10, col)['Country_Name'].tolist()
    return country_list

top_10_summer = top_ten(top_countries, 'Total_Summer')
top_10_winter = top_ten(top_countries, 'Total_Winter')
top_10 = top_ten(top_countries, 'Total_Medals')

common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))

print(common)




# --------------
#Code starts here

summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

fig, (ax_1, ax_2, ax_3) = plt.subplots(3,1, figsize=(20,10))

summer_df.groupby(['Country_Name', 'Total_Summer']).agg({'Total_Summer': 'sum'}).unstack().plot(kind='bar', ax=ax_1)

winter_df.groupby(['Country_Name', 'Total_Summer']).agg({'Total_Summer': 'sum'}).unstack().plot(kind='bar', ax=ax_2)

top_df.groupby(['Country_Name', 'Total_Summer']).agg({'Total_Summer': 'sum'}).unstack().plot(kind='bar', ax=ax_3)


# --------------
#Code starts here

summer_df['Golden_Ratio'] = summer_df['Gold_Summer'] / summer_df['Total_Summer']
summer_max_ratio, summer_country_gold = summer_df.groupby(['Golden_Ratio', 'Country_Name']).agg({'Golden_Ratio':'max'}).idxmax().tolist()[0]
print(summer_max_ratio, summer_country_gold)

winter_df['Golden_Ratio'] = winter_df['Gold_Winter'] / winter_df['Total_Winter']
winter_max_ratio, winter_country_gold = winter_df.groupby(['Golden_Ratio', 'Country_Name']).agg({'Golden_Ratio':'max'}).idxmax().tolist()[0]
print(winter_max_ratio, winter_country_gold)

top_df['Golden_Ratio'] = top_df['Gold_Total'] / top_df['Total_Medals']
top_max_ratio, top_country_gold = top_df.groupby(['Golden_Ratio', 'Country_Name']).agg({'Golden_Ratio':'max'}).idxmax().tolist()[0]
print(top_max_ratio, top_country_gold)



# --------------
#Code starts here

data_1 = data.drop(data.tail(1).index)

data_1['Total_Points'] = ((data_1['Gold_Total'] * 3) + (data_1['Silver_Total'] * 2) + (data_1['Bronze_Total'] * 1))

most_points, best_country = data_1.groupby(['Total_Points', 'Country_Name']).agg({'Total_Points':'max'}).idxmax().tolist()[0]

print('Max Points: {} || Best Country: {}'.format(most_points, best_country))



# --------------
#Code starts here

best = data[data['Country_Name'] == best_country][['Gold_Total','Silver_Total','Bronze_Total']]

best.plot(kind='bar', stacked=True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)
plt.show()



