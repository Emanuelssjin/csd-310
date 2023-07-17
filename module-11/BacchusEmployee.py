import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Trunks!99",
    database="bacchus"
)

cursor = db.cursor()

query = """
    SELECT
        CONCAT(e.employee_firstName, ' ', e.employee_lastName) AS employee_name,
        wh.work_day,
        wh.clock_in,
        wh.clock_out
    FROM
        employee e
    INNER JOIN
        work_hours wh ON e.employee_id = wh.employee_id
"""

cursor.execute(query)

results = cursor.fetchall()

print("Employee Work Hours Report")
print("-------------------------------------------------")
print("Employee Name | Work Day     | Clock-In | Clock-Out")
print("-------------------------------------------------")

for row in results:
    employee_name, work_day, clock_in, clock_out = row
    print(f"{employee_name:14} | {work_day} | {clock_in} | {clock_out}")

db.close()
