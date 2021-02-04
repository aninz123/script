import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root1234"
)
mycursor = mydb.cursor()
#### check database 
mycursor.execute("SHOW DATABASES")
schemas=[]
for x in mycursor:
  print(x[0])
  schemas.append(x[0])

print("-"*80)
### create database 
if not "thun" in schemas:
    print("don't have ")
    create_db_name="thun"
    print(f"CREATE DATABASE {create_db_name}")
    mycursor.execute(f"CREATE DATABASE {create_db_name};")
else:
    print("have")
print("-"*80)
#### check database 
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x[0])

##  connect database 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root1234",
  database="thun"
)
print("-"*80)
# Use schema 
mycursor = mydb.cursor(buffered=True)
# show table 
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x[0])
print("-"*80)
### sql create table
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")



#### insert 
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 27")
mycursor.execute(sql, val)
mydb.commit()

#### qeury 
### fetchall all 
print("-"*80)
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

### fetchall one 
print("-"*80)
mycursor.execute("SELECT name FROM customers")
myresult = mycursor.fetchone()
print(myresult)
myresult = mycursor.fetchone()
print(myresult)

## update 
print("-"*80)
print("update")
sql = "UPDATE customers SET name = 'nine' WHERE name = 'John'"
mycursor.execute(sql)
mydb.commit()

### fetchall all 
print("-"*80)
mycursor.execute("SELECT * FROM customers")
myresult=['asdasd']
myresult = mycursor.fetchall()
for x in myresult:
  print(x)