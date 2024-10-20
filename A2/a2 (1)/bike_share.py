from math import radians, cos, sin, sqrt, atan2

# Constants to make the code easier to maintain
STATION_ID_INDEX = 0
NAME_INDEX = 1
LAT_INDEX = 2
LON_INDEX = 3
CAPACITY_INDEX = 2
NUM_BIKES_AVAILABLE_INDEX = 5
NUM_DOCKS_AVAILABLE_INDEX = 6
# Constants for station data
ID = 0
NAME = 1
LATITUDE = 2
LONGITUDE = 3
CAPACITY = 4
BIKES_AVAILABLE = 5
DOCKS_AVAILABLE = 6


NO_KIOSK = 'SMART'

# Helper function to check if a string represents a number
def is_number(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False

# Convert data function implementation
def convert_data(data: list[list[str]]) -> None:
    """
    Modify the given list so that:
    - Strings that represent whole numbers are converted to ints.
    - Strings that represent floating-point numbers are converted to floats.
    - Strings that do not represent numbers remain as strings.
    
    This function mutates the data list in place.
    
    Args:
    data (list[list[str]]): The list of lists containing station data.
    """
    for row in data:
        for i in range(len(row)):
            if is_number(row[i]):
                num = float(row[i])
                # Check if it is a whole number
                if num.is_integer():
                    row[i] = int(num)
                else:
                    row[i] = num

# Function: has_kiosk
def has_kiosk(station: list) -> bool:
    """
    Returns True if the station has a kiosk. A station without a kiosk contains
    the string referred to by NO_KIOSK in its name.
    
    Args:
    station (list): A list representing a station with the structure [station_id, name, lat, lon, capacity, num_bikes_available, num_docks_available]
    
    Returns:
    bool: True if the station has a kiosk, False otherwise.
    """
    return NO_KIOSK not in station[NAME_INDEX]

# Function: get_station_info
def get_station_info(station_id: int, stations: list) -> list:
    """
    Returns a list with station name, number of bikes available, number of docks available, 
    and whether the station has a kiosk for a given station ID.
    
    Args:
    station_id (int): The station ID to search for.
    stations (list): A list of lists representing multiple stations.
    
    Returns:
    list: [station name, number of bikes available, number of docks available, has_kiosk].
    """
    for station in stations:
        if station[STATION_ID_INDEX] == station_id:
            return [
                station[NAME_INDEX],
                station[NUM_BIKES_AVAILABLE_INDEX],  # Corrected: Number of bikes available
                station[NUM_DOCKS_AVAILABLE_INDEX],  # Corrected: Number of docks available
                has_kiosk(station)
            ]


# Function: get_column_sum
def get_column_sum(index: int, stations: list) -> int:
    """
    Returns the sum of the values at the given index for all stations in the list.
    
    Args:
    index (int): The index of the column to sum.
    stations (list): A list of lists representing multiple stations.
    
    Returns:
    int: The sum of the values in the specified column.
    """
    return sum(station[index] for station in stations)

# Function: get_stations_with_kiosks
def get_stations_with_kiosks(stations: list) -> list:
    """
    Returns a list of station IDs that have kiosks.
    
    Args:
    stations (list): A list of lists representing multiple stations.
    
    Returns:
    list: A list of station IDs that have kiosks.
    """
    return [station[STATION_ID_INDEX] for station in stations if has_kiosk(station)]

# Helper function to calculate distance between two coordinates
def get_lat_lon_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculate the Haversine distance between two points on the Earth (specified in decimal degrees).
    
    Args:
    lat1, lon1: Latitude and Longitude of point 1.
    lat2, lon2: Latitude and Longitude of point 2.
    
    Returns:
    float: Distance in kilometers.
    """
    R = 6371.0  # Radius of the Earth in kilometers
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = (sin(dlat / 2) ** 2 +
         cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

# Function: get_nearest_station
def get_nearest_station(lat: float, lon: float, stations: list) -> int:
    """
    Returns the station ID of the nearest station to the given coordinates.
    In case of a tie, returns the station ID of the nearest station that appears last in the list.
    
    Args:
    lat (float): Latitude of the current location.
    lon (float): Longitude of the current location.
    stations (list): A list of lists representing multiple stations.
    
    Returns:
    int: The station ID of the nearest station.
    """
    min_distance = float('inf')
    nearest_station_id = -1
    
    for station in stations:
        distance = get_lat_lon_distance(lat, lon, station[LAT_INDEX], station[LON_INDEX])
        if distance <= min_distance:
            min_distance = distance
            nearest_station_id = station[STATION_ID_INDEX]
    
    return nearest_station_id

# Function: rent_bike
def rent_bike(station_id: int, stations: list) -> bool:
    """
    Rent a bike from a station if at least one bike is available.
    Update the bikes available and docks available counts. 
    
    Args:
    station_id (int): The station ID to rent a bike from.
    stations (list): A list of lists representing multiple stations.
    
    Returns:
    bool: True if the bike rental is successful, False otherwise.
    """
    for station in stations:
        if station[STATION_ID_INDEX] == station_id:
            if station[NUM_BIKES_AVAILABLE_INDEX] > 0:
                station[NUM_BIKES_AVAILABLE_INDEX] -= 1
                station[NUM_DOCKS_AVAILABLE_INDEX] += 1
                return True
            else:
                return False

# Function: return_bike
def return_bike(station_id: int, stations: list) -> bool:
    """
    Return a bike to a station if at least one dock is available.
    Update the bikes available and docks available counts. 
    
    Args:
    station_id (int): The station ID to return a bike to.
    stations (list): A list of lists representing multiple stations.
    
    Returns:
    bool: True if the bike return is successful, False otherwise.
    """
    for station in stations:
        if station[STATION_ID_INDEX] == station_id:
            if station[NUM_DOCKS_AVAILABLE_INDEX] > 0:
                station[NUM_BIKES_AVAILABLE_INDEX] += 1
                station[NUM_DOCKS_AVAILABLE_INDEX] -= 1
                return True
    return False  # If the station_id is not found



# Function: upgrade_stations
def upgrade_stations(capacity_threshold: int, bikes_to_add: int, stations: list) -> int:
    """
    Add bikes and docks to stations with capacity less than the given threshold.
    Each added bike comes with a new dock.
    
    Args:
    capacity_threshold (int): The capacity below which stations are upgraded.
    bikes_to_add (int): The number of bikes (and docks) to add to each qualifying station.
    stations (list): A list of lists representing multiple stations.
    
    Returns:
    int: The total number of bikes added.
    """
    total_bikes_added = 0
    
    for station in stations:
        if station[CAPACITY_INDEX] < capacity_threshold:
            station[NUM_BIKES_AVAILABLE_INDEX] += bikes_to_add
            station[CAPACITY_INDEX] += bikes_to_add  # Each bike comes with a dock
            total_bikes_added += bikes_to_add
    
    return total_bikes_added