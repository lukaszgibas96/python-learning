import sys

def main():

    coordinates = (42.376, -71.115)

    latitude, longitude = coordinates

    # Tuples value unpack method 1
    print(f"Latitude: {coordinates[0]}")
    print(f"Longitude: {coordinates[1]}")


    # Tuples value unpack method 2
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")
    # Check the variable size in memory
    coordinates_tuple = (42.376, -71.115)
    coordinates_list = [42.376, -71.115]
    print(f"{sys.getsizeof(coordinates_tuple)} bytes")
    print(f"{sys.getsizeof(coordinates_list)} bytes")

main()