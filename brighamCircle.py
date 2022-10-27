# importing the requests library
import requests
import datetime

# mbta inefficiency dashboard: 
# Tracks average speed of trains, amount of stoppages/break downs per day per line,
# most and least efficient lines, avg time between trains, etc

# api-endpoint
STOP_ID = 'place-mispk'
get_url = f'https://api-v3.mbta.com/predictions?filter[stop]={STOP_ID}&sort=arrival_time'
direction_destinations = ["Heath Street","Union Square"]
  
# sending get request and saving the response as response object
r = requests.get(url = get_url)

# extracting data in json format
data = r.json()['data']
#print(data)
  
arrival_times = [(train['attributes']['arrival_time'], direction_destinations[train['attributes']['direction_id']]) for train in data[:3]]
#print(arrival_times)
for time, dest in arrival_times:
    minutes_until_arrival = (datetime.datetime.strptime(time, '%Y-%m-%dT%H:%M:%S-04:00') - datetime.datetime.now()).seconds // 60
    print(f'Train to {dest} arriving at Mission Park in {minutes_until_arrival} minutes')





