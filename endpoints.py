import requests
from enum import Enum
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# mbta live map
# Gets the locations of all trains on a given line and displays them on a map

# api-endpoint
base_url = f'https://api-v3.mbta.com/'


lines = ['Red', 'Orange', 'Blue', 'Green-B', 'Green-C', 'Green-D', 'Green-E']


# get latitudes and longitudes of all trains on a given line
@app.route('/api/data')
def get_train_locations_by_line():
    get_url = f'https://api-v3.mbta.com/vehicles?filter[route]=Green-E&include=trip'
    r = requests.get(url=get_url)
    data = r.json()['data']
    locations = [(train['attributes']['latitude'], train['attributes']['longitude'])
                 for train in data if train['attributes']['latitude'] != None and train['attributes']['longitude'] != None]
    location_map = {'train'+str(i): locations[i]
                    for i in range(len(locations))}
    return jsonify(location_map)


if __name__ == '__main__':
    app.run()
