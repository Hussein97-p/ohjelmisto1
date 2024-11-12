from flask import Flask, jsonify, abort
import mysql.connector

app = Flask(__name__)

# Database connection setup
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="flight_game",
        charset="utf8mb4",
        collation="utf8mb4_general_ci"
    )

@app.route('/AIRPORT/<icao>', methods=['GET'])
def get_airport(icao):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Query to retrieve airport data by ICAO code
    query = "SELECT ident AS ICAO, name AS Name, municipality AS Municipality FROM airport WHERE ident = %s"
    cursor.execute(query, (icao.upper(),))
    result = cursor.fetchone()

    # Close the database connection
    cursor.close()
    conn.close()
    
    # Return result if found, otherwise return 404
    if result:
        return jsonify(result)
    else:
        abort(404, description="The airport is not available")

# Instructions for the user
print("========================================")
print("========================================")
print("To retrieve airport information, enter the URL in the following format:")
print("http://127.0.0.1:3000/AIRPORT/<ICAO_CODE>")
print("Replace <ICAO_CODE> with the ICAO code of the airport you are searching for.")
print("Example:")
print("http://127.0.0.1:3000/AIRPORT/EFHK")
print("========================================")

# Run the application
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=3000)
