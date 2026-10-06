import MySQLdb

db = MySQLdb.connect(
    host = 'localhost',
    user = 'root',
    password = 'YOUR_PASSWORD',
    db = 'DATABASE_NAME'
)

c = db.cursor()

# Insert
'''c.execute("insert into users values('Santhosh', 'santhosh@gmail.com', 20)")
db.commit()
print("Inserted successfully.")'''

# Update
c.execute("update users set age=22 where u_name='Santhosh'")
db.commit()
print("Updated successfully.")