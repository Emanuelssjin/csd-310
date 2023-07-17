import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="bacchus_user",
    password="winery",
    database="bacchus"
)

cursor = db.cursor()

query = """
    SELECT
        s.supplier_name,
        s.supplier_contact_firstName,
        s.supplier_contact_lastName,
        s.supplier_phone,
        s.supplier_email,
        GROUP_CONCAT(sp.supply_name SEPARATOR ', ') AS supplies,
        d.delivery_date,
        d.expected_date
    FROM
        supplier s
    INNER JOIN
        supply sp ON s.supplier_id = sp.supplier_id
    LEFT JOIN
        delivery d ON s.supplier_id = d.supplier_id
    GROUP BY
        s.supplier_id,
        d.delivery_date,
        d.expected_date
"""

cursor.execute(query)

results = cursor.fetchall()

print("Supplier Information Report")
print("-----------------------------------------------------------------------------")
print("Supplier Name | Contact Name   | Phone         | Email                | Supplies       | Delivery Date | Expected Date")
print("-----------------------------------------------------------------------------")

for row in results:
    supplier_name, contact_firstName, contact_lastName, phone, email, supplies, delivery_date, expected_date = row
    print(f"{supplier_name:13} | {contact_firstName} {contact_lastName:12} | {phone:14} | {email:20} | {supplies:15} | {delivery_date} | {expected_date}")

db.close()
