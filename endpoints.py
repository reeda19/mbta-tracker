# importing the requests library
import requests
from enum import Enum
# mbta inefficiency dashboard: 
# Tracks average speed of trains, amount of stoppages/break downs per day per line,
# most and least efficient lines, avg time between trains, etc

# api-endpoint
base_url = f'https://api-v3.mbta.com/'

# TODO
# Implement end points for:
# 1. Number of trips per day per line
# 2. Average speed of trains per line
# 3. Average time between trains per line
# 4. Number of stoppages per day per line
# 5. Number of available trains per line per day

lines = ['Red', 'Orange', 'Blue', 'Green-B', 'Green-C', 'Green-D', 'Green-E']

def get_trips_per_day_per_line():
    pass

def get_average_train_speed_by_line():
    for line in lines:
        get_url = f'https://api-v3.mbta.com/vehicles?filter[route]={line}&include=trip'
        r = requests.get(url = get_url)
        data = r.json()['data']
        speeds = [train['attributes']['speed'] for train in data if train['attributes']['speed'] != None]
        avg_speed = 0 if len(speeds) == 0 else sum(speeds)/len(speeds)
        print(f'Average speed for {line}: {avg_speed}')

def get_average_time_between_trains_by_line():
    for line in lines:
        get_url = f'https://api-v3.mbta.com/vehicles?filter[route]={line}&include=trip'
        r = requests.get(url = get_url)
        data = r.json()['data']
        arrival_times = [train['attributes']['arrival_time'] for train in data[:3]]
        

def get_number_of_stoppages_per_day_per_line():
    pass

def get_number_of_available_trains_per_line_per_day():
    for line in lines:
        get_url = f'https://api-v3.mbta.com/vehicles?filter[route]={line}&include=trip'
        r = requests.get(url = get_url)
        data = r.json()['data']
        print(f'Number of available trains for {line}: {len(data)}')

get_number_of_available_trains_per_line_per_day()
get_average_train_speed_by_line()


