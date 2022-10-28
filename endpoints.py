# importing the requests library
import requests
from enum import Enum
import datetime
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
    for line in lines:
        get_url = f'https://api-v3.mbta.com/schedules?filter[route]={line}'
        r = requests.get(url = get_url)
        data = r.json()['data']
        print(f'Number of trips for {line}: {len(data)}')

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
        get_url = f'https://api-v3.mbta.com/schedules?filter[route]={line}'
        r = requests.get(url = get_url)
        data = r.json()['data']
        times = [datetime.datetime.strptime(train['attributes']['departure_time'], '%Y-%m-%dT%H:%M:%S-04:00') for train in data if train['attributes']['departure_time'] != None]
        times.sort()
        time_diffs = [times[i+1] - times[i] for i in range(len(times)-1)]
        avg_time_diff = 0 if len(time_diffs) == 0 else sum(time_diffs, datetime.timedelta(0))/len(time_diffs)
        print(f'Average time between trains for {line}: {avg_time_diff}') 
        

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
get_average_time_between_trains_by_line()
get_trips_per_day_per_line()



