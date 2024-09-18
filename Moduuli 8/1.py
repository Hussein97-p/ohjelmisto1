import mysql.connector

# إعداد الاتصال بقاعدة البيانات
conn = mysql.connector.connect(
    host="localhost",
    user="hussein",
    password="kesko11@@",
    database="flight_game",
    charset="utf8mb4",
    collation="utf8mb4_general_ci"
)

try:
    if conn.is_connected():
        print("Connected to the database.")
        icao_code = input("Please enter the ICAO code of the airport: ").strip()
        cursor = conn.cursor()

        query = "SELECT name, location FROM airport WHERE ident = %s"
        cursor.execute(query, (icao_code,))
        result = cursor.fetchone()

        if result:
            name, location = result
            print(f"Airport Name: {name}")
            print(f"Location: {location}")
        else:
            print("No airport found with the given ICAO code.")

finally:
    # إغلاق الاتصال
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("Connection closed.")
 