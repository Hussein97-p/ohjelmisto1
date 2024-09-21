import mysql.connector
from geopy.distance import geodesic

conn = mysql.connector.connect(
    host="localhost",
    user="hussein",
    password="kesko11@@",
    database="flight_game",
    charset="utf8mb4",
    collation="utf8mb4_general_ci"
)

cursor = conn.cursor()

def get_coordinates(icao_code):
    query = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    cursor.execute(query, (icao_code,))
    result = cursor.fetchone()
    return result

def calculate_distance(icao1, icao2):
    coord1 = get_coordinates(icao1)
    coord2 = get_coordinates(icao2)

    if coord1 and coord2:
        distance = geodesic(coord1, coord2).kilometers
        return distance
    else:
        return None

def main():
    icao1 = input("Enter the ICAO code for the first airport: ").strip().upper()
    icao2 = input("Enter the ICAO code for the second airport: ").strip().upper()

    distance = calculate_distance(icao1, icao2)

    if distance is not None:
        print(f"The distance between {icao1} and {icao2} is {distance:.2f} kilometers.")
    else:
        print("No information found for one or both of the airports.")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
