import math

def haversine_distance(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    r = 6371.0
    return c * r

lat2 = 8.509302  
lon2 = 77.066998  
lat1 = 8.523572  
lon1 = 76.953707 

distance = haversine_distance(lat1, lon1, lat2, lon2)
print(f"Distance: {distance:.2f} km")
