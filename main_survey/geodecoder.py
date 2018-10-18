
from geopy.geocoders import Nominatim
from geopy.distance import geodesic, great_circle

geolocator = Nominatim(user_agent="webapp")

def from_address_to_coords(address):
    location = geolocator.geocode(address)
    if (location):
        a = (location.latitude, location.longitude)
        return a
    else:
        return ("None")

def from_coords_to_address(lat, long):
    location = geolocator.reverse(lat + ", " + long)
    return str(location.address)

def meters_from_two_addresses(a,b):
    return geodesic(a,b).meters

def main():

    choice = input("Scegli:\n1 per decodificare un indirizzo in coordinate;\n2 per convertire due coordinate in un indirizzo testuale;\n3 per calcolare la distanza tra due punti:\n")

    if (choice=='1'):
        indirizzo = input("Inserisci l'indirizzo: ")
        print(from_address_to_coords(indirizzo))

    if (choice=='2'):
        latitude = input("\nLatitudine: ")
        longitude = input("\nLongitudine: ")
        print(from_coords_to_address(latitude,longitude))

    if (choice=='3'):
        latitudeA = input("\nLatitudine primo punto: ")
        longitudeA = input("\nLongitudine primo punto: ")
        a = (latitudeA, longitudeA)
        latitudeB = input("\nLatitudine secondo punto: ")
        longitudeB = input("\nLongitudine secondo punto: ")
        b = (latitudeB, longitudeB)
        print("\nTra il primo e il secondo punto c'è una distanza di %.2f metri" %meters_from_two_addresses(a,b))


if __name__ == '__main__':
    main()
