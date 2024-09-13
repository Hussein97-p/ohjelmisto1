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

# إنشاء مؤشر للتفاعل مع قاعدة البيانات
cursor = conn.cursor()

# طلب رمز الدولة من المستخدم
country_code = input("Enter the country code (e.g., FI): ").upper()

# استعلام SQL لجلب عدد المطارات في الدولة حسب النوع
query = """
    SELECT airport_type, COUNT(*) AS count
    FROM airport
    WHERE iso_country = %s
    GROUP BY airport_type;
"""

# تنفيذ الاستعلام
cursor.execute(query, (country_code,))

# الحصول على النتائج
results = cursor.fetchall()

# التحقق من وجود مطارات في الدولة المحددة
if results:
    print(f"Airports in {country_code}:")
    for row in results:
        print(f"{row[0]}: {row[1]} airports")
else:
    print(f"No airports found for country code: {country_code}")

# إغلاق الاتصال بقاعدة البيانات
cursor.close()
conn.close()
