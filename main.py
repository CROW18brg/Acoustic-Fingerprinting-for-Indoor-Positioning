import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="hd5gcUpDk",
 database="mydatabase"
)

mycursor = mydb.cursor()

#mycursor.execute("create table sala (id int AUTO_INCREMENT,f1 VARCHAR(255),PRIMARY KEY(id)); ")
#mycursor.execute("show columns FROM sala")

#mycursor.execute("CREATE TABLE quarto (name VARCHAR(255), f1 VARCHAR(255)),f2")
#
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("musica4", "asa5adada6878787a7")
a=0
#mycursor.execute(sql, val)

#mydb.commit()
#
# print(mycursor.rowcount, "record inserted.")

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)