# tee ratkaisu tänne
# Write your solution here
import math

def get_station_data(filename: str):
    station_dict = {}
    with open(filename) as stations:
        for line in stations:
            parts = line.strip().split(';')
            if parts[0] == 'Longitude':
                continue
            station_dict[parts[3]] = (float(parts[0]),float(parts[1]))

    return station_dict
        
def distance(stations: dict, station1: str, station2: str):
    for key, value in stations.items():
        if key == station1:
            coord1 = value
        if key == station2:
            coord2 = value

    result = calculate_distance(coord1, coord2)
    return result

def calculate_distance(coord1, coord2):
    x_km = (coord1[0] - coord2[0]) * 55.26
    y_km = (coord1[1] - coord2[1]) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

def greatest_distance(stations: dict):
    max_distance = 0
    farthest_pair = ()
    station_keys = list(stations.keys())
    n = len(station_keys)
    
    for i in range(n):
        for j in range(i + 1, n):
            loc1 = station_keys[i]
            loc2 = station_keys[j]
            distance = calculate_distance(stations[loc1], stations[loc2])
            if distance > max_distance:
                max_distance = distance
                farthest_pair = (loc1, loc2, max_distance)
    
    return farthest_pair



if __name__ == "__main__":
    stations = get_station_data("stations2.csv")
    x = greatest_distance(stations)
    print(x)