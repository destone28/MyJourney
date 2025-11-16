
from geopy.geocoders import Nominatim
from geopy.distance import geodesic, great_circle
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
import logging

logger = logging.getLogger(__name__)

geolocator = Nominatim(user_agent="webapp")

def from_address_to_coords(address):
    """
    Convert an address to geographic coordinates.

    Args:
        address (str): The address to geocode

    Returns:
        tuple: (latitude, longitude) or "None" if geocoding fails
    """
    try:
        location = geolocator.geocode(address)
        if location:
            return (location.latitude, location.longitude)
        else:
            logger.warning(f"Could not geocode address: {address}")
            return "None"
    except (GeocoderTimedOut, GeocoderServiceError) as e:
        logger.error(f"Geocoding error for address '{address}': {e}")
        return "None"
    except Exception as e:
        logger.error(f"Unexpected error geocoding address '{address}': {e}")
        return "None"

def from_coords_to_address(lat, long):
    location = geolocator.reverse(lat + ", " + long)
    return str(location.address)

def meters_from_two_addresses(a,b):
    return geodesic(a,b).meters

def cap_from_address(indirizzo):
    """
    Extract postal code (CAP) from an address.

    Args:
        indirizzo (str): The address to extract CAP from

    Returns:
        str: Postal code or "20121" (default Milan CAP) if not found
    """
    try:
        location = geolocator.geocode(indirizzo, addressdetails=True)
        if location and 'address' in location.raw:
            postcode = location.raw['address'].get('postcode')
            if postcode:
                return postcode
        logger.warning(f"Could not extract CAP from address: {indirizzo}, using default")
        return "20121"  # Default Milan postal code
    except (GeocoderTimedOut, GeocoderServiceError) as e:
        logger.error(f"Geocoding error for CAP extraction '{indirizzo}': {e}")
        return "20121"
    except (KeyError, AttributeError) as e:
        logger.error(f"Invalid geocoding response for '{indirizzo}': {e}")
        return "20121"
    except Exception as e:
        logger.error(f"Unexpected error extracting CAP from '{indirizzo}': {e}")
        return "20121"

def municipio_from_cap(cap):
    municipio = "1"

    if (cap=="20123" or cap=="20121" or cap=="20145" or cap=="20122" ):
        municipio = "1"
    elif (cap=="20124" or cap=="20125" or cap=="20128" or cap=="20127" ):
        municipio = "2"
    elif (cap=="20131" or cap=="20133" or cap=="20129" or cap=="20134" or cap=="20132" or cap=="20126" ):
        municipio = "3"
    elif (cap=="20137" or cap=="20138" ):
        municipio = "4"
    elif (cap=="20141" or cap=="20142" or cap=="20139" or cap=="20135" or cap=="20136" ):
        municipio = "5"
    elif (cap=="20143" or cap=="20146" or cap=="20144" ):
        municipio = "6"
    elif (cap=="20153" or cap=="20152" or cap=="20151" or cap=="20147" ):
        municipio = "7"
    elif (cap=="20149" or cap=="20156" or cap=="20155" or cap=="20154" or cap=="20148" or cap=="20157" ):
        municipio = "8"
    elif (cap=="20158" or cap=="20161" or cap=="20162" or cap=="20159" ):
        municipio = "9"

    return municipio

def municipio_from_indirizzo(indirizzo):
    return municipio_from_cap(cap_from_address(indirizzo))

def main():

    choice = input("Scegli:\n1 per decodificare un indirizzo in coordinate;\n2 per convertire due coordinate in un indirizzo testuale;\n3 per calcolare la distanza tra due punti:\n4 per il cap:\n5 per il municipio:\n6 per il sindacato:\n")

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

    if (choice=='4'):
        indirizzo = input("Inserisci l'indirizzo: ")
        print(cap_from_address(indirizzo))

    if (choice=='5'):
        indirizzo = input("Inserisci l'indirizzo: ")
        print (municipio_from_indirizzo(indirizzo))

if __name__ == '__main__':
    main()
