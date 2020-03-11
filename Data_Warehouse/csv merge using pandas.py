import pandas as pd

# Read the csv files, adjust the file name if needed
time = pd.read_csv('./dim_time.csv') 
trip = pd.read_csv('./trips.csv')
traffic = pd.read_csv('./dim_traffic.csv')
display('time.head()', 'trip.head()', 'traffic.head()')

# Merge trip and time tables
trip.time = pd.merge(trip, time, how='outer',
                     left_on='start_timestamp_id', right_on='timestamp_id') 

# drop duplicate info (supposed to be the key column)
trip.time = trip.time.drop('timestamp_id', 1)
trip.time.head()

# Merge the time&trip table with the traffic table
finalMerge = pd.merge(trip.time, traffic, on='timestamp_id', how='left')
finalMerge.head()

# Write to csv
results_df.to_csv('tableMerge.csv', encoding='utf-8')
