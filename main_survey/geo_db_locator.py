import sqlite3
from . import geodecoder
import time
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "dati.sqlite")

def anagrafe_milano_piu_vicina(address):
    """
    Find the nearest registry office (anagrafe) in Milan based on address.

    Args:
        address (str): The address to search from

    Returns:
        str: Formatted string with registry office information
    """
    municipio = "1"
    indirizzo_municipio = "Via Larga, 12 - 20122 - Milano"
    tel_municipio = "020202"

    ricerca = geodecoder.municipio_from_indirizzo(address)

    with sqlite3.connect(db_path) as db_connection:
        cursor = db_connection.execute("SELECT titolo, lat, long, indirizzo, tel FROM anagrafe_milano")
        for anagrafe in cursor:
            print(anagrafe)
            if anagrafe[0] == ricerca:
                municipio = anagrafe[0]
                indirizzo_municipio = anagrafe[3]
                # tel is not in the result, using default
                break

    stringa = "Ufficio anagrafe del Municipio {}, {}, telefono: {}\n".format(municipio, indirizzo_municipio, tel_municipio)
    print(stringa)
    return stringa



def valori_bollati_milano_piu_vicini(address):
    """
    Find the nearest stamp tax office (Lottomatica) in Milan.

    Args:
        address (tuple): Coordinates (latitude, longitude)

    Returns:
        str: Formatted string with office information
    """
    distanza_min = None
    lottomatica_selezionata = "Lottomatica"
    indirizzo_lottomatica = "Milano"
    tel_lottomatica = "N/A"

    with sqlite3.connect(db_path) as db_connection:
        cursor = db_connection.execute("SELECT nome, lat, long, via, civico, telefono FROM valoribollati_milano")

        for lottomatica in cursor:
            lott_corrente = lottomatica[1], lottomatica[2]
            distanza = geodecoder.meters_from_two_addresses(address, lott_corrente)
            if distanza_min is None or distanza < distanza_min:
                distanza_min = distanza
                lottomatica_selezionata = lottomatica[0]
                indirizzo_lottomatica = str(lottomatica[3]) + ", " + str(lottomatica[4])
                tel_lottomatica = lottomatica[5]

    stringa = "Puoi acquistare la marca da bollo presso {}, in {}, telefono: {}\n".format(
        lottomatica_selezionata, indirizzo_lottomatica, tel_lottomatica
    )
    print(stringa)
    return stringa



def idoneita_abitativa_vicina_milano(address):
    """
    Find the nearest housing suitability office in Milan.

    Args:
        address (str): The address to search from

    Returns:
        str: Formatted string with office information
    """
    servizio_ufficio = "Unità Servizi - Ufficio Idoneità Abitativa"
    num_ufficio = "1"
    indirizzo_ufficio = "via Marconi, 2 - 20123 - Milano"
    aperture_ufficio = "da lunedì al venerdì dalle 9:30 alle 12:00, il martedì anche dalle 14:30 alle 15:30"
    tel_ufficio = "0288458124"

    ricerca = geodecoder.municipio_from_indirizzo(address)

    with sqlite3.connect(db_path) as db_connection:
        cursor = db_connection.execute("SELECT municipio, indirizzo, servizio, giorni_e_ore, tel FROM idoneitaabitativa_milano")
        for ufficio in cursor:
            if ufficio[0] == ricerca:
                num_ufficio = ufficio[0]
                indirizzo_ufficio = ufficio[1]
                servizio_ufficio = ufficio[2]
                aperture_ufficio = ufficio[3]
                tel_ufficio = ufficio[4]
                break

    stringa = "{}, Municipio {}, {}, aperto {}, telefono: {}\n".format(
        servizio_ufficio, num_ufficio, indirizzo_ufficio, aperture_ufficio, tel_ufficio
    )
    print(stringa)
    return stringa


def info_ambasciata(paese):
    """
    Get embassy information for a given country.

    Args:
        paese (str): Country name

    Returns:
        list: Embassy information
    """
    with sqlite3.connect(db_path) as db_connection:
        cursor = db_connection.execute(
            "SELECT sede, indirizzo, telefonisedi, faxsedi, sitoweb, email FROM ambasciate WHERE paese = ?",
            (paese.upper(),)
        )
        first_row = cursor.fetchone()
        if first_row:
            output = list(first_row)
            for elem in cursor:
                output.append(elem)
            print(output)
            return output
        return []



def info_consolato(paese):
    """
    Get consulate information for a given country.

    Args:
        paese (str): Country name

    Returns:
        list: Consulate information
    """
    with sqlite3.connect(db_path) as db_connection:
        cursor = db_connection.execute(
            "SELECT sede, indirizzo, telefonisedi, faxsedi, sitoweb, email FROM consolati WHERE paese = ?",
            (paese.upper(),)
        )
        first_row = cursor.fetchone()
        if first_row:
            output = list(first_row)
            for elem in cursor:
                output.append(elem)
            print(output)
            return output
        return []


def sindacati_e_patronati(address, via):
    """
    Find nearest union/patronage office.

    Args:
        address (str): Full address
        via (str): Street name

    Returns:
        str: Formatted string with office information
    """
    singole_parole_di_via = via.split()
    nome_via = singole_parole_di_via[-1] if singole_parole_di_via else ""

    nome_ufficio = "INCA"
    indirizzo_ufficio = "Corso di Porta Vittoria, 43 - 20122 - Milano"
    tel_ufficio = "0255025309"
    temp_addr = None

    cap_da_indirizzo = geodecoder.cap_from_address(address)

    with sqlite3.connect(db_path) as db_connection:
        cursor = db_connection.execute("SELECT ufficio, indirizzo, telefono, cap FROM sindacatipatronati")

        for sindacato_temp in cursor:
            if nome_via in sindacato_temp[1]:
                # Found office on same street
                temp_addr = sindacato_temp[1]
                nome_ufficio = sindacato_temp[0]
                indirizzo_ufficio = sindacato_temp[1]
                tel_ufficio = sindacato_temp[2]
                break
            elif sindacato_temp[3] == cap_da_indirizzo and temp_addr is None:
                # Found office in same postal code area
                temp_addr = sindacato_temp[1]
                nome_ufficio = sindacato_temp[0]
                indirizzo_ufficio = sindacato_temp[1]
                tel_ufficio = sindacato_temp[2]

    stringa = "\n{},\nindirizzo: {},\ntelefono: {}\n".format(nome_ufficio, indirizzo_ufficio, tel_ufficio)
    print(stringa)
    return stringa






if __name__ == '__main__':
    main()
