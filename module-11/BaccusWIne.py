import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Trunks!99',
    database='bacchus'
)

cursor = conn.cursor()

query = """
    SELECT w.wine_id, w.wine_price, w.wine_quantity, d.distributor_name, d.distributor_address_one, d.distributor_city, d.distributor_state, d.distributor_postal
    FROM wine AS w
    JOIN distributor AS d ON w.wine_id = d.wine_id
"""
cursor.execute(query)

wine_report = cursor.fetchall()

for wine in wine_report:
    wine_id, wine_price, wine_quantity, distributor_name, distributor_address, distributor_city, distributor_state, distributor_postal = wine
    print(f"Wine ID: {wine_id}, Price: ${wine_price}, Quantity: {wine_quantity}")
    print(f"Distributor: {distributor_name}")
    print(f"Address: {distributor_address}, {distributor_city}, {distributor_state} {distributor_postal}")
    print()

cursor.close()
conn.close()