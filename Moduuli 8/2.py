import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="hussein",
    password="kesko11@@",
    database="flight_game",
    charset="utf8mb4",
    collation="utf8mb4_general_ci"
)

cursor = conn.cursor()

country_code = input("Enter the country code (Forexample>> -FI): ").upper()

query = """
    SELECT type, COUNT(*) AS count
    FROM airport
    WHERE iso_country = %s
    GROUP BY type;
"""

cursor.execute(query, (country_code,))

results = cursor.fetchall()

if results:
    print(f"Airports in {country_code}:")
    for row in results:
        print(f"{row[0]}: {row[1]} airports")
else:
    print(f"No airports found for country code: {country_code}")

cursor.close()
conn.close()
