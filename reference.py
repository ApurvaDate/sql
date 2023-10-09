#code for reference


############################# test.py ####################################

import mysql.connector

mydb = mysql.connector.connect( 

    host = "localhost", 
    user = "root",
    password = "***************",
    database = "sql_course"
    )

print(mydb)

#initialize cursor 
mycursor = mydb.cursor()

#create database
# mycursor.execute("CREATE DATABASE sql_course")

#show databases
mycursor.execute("SHOW DATABASES")

for db in mycursor:
    print(db)

#to create table in our database

# mycursor.execute("CREATE TABLE students (name VARCHAR(20), age INTEGER(10))")

for tb in mycursor:
    print(tb)




######################## test_connection.py ################################


import mysql.connector


#to setup a database and test the connection
mydb = mysql.connector.connect(
    
    host = "localhost",
    user = 'root',
    password = "*******************",
    database = 'testdb'
)
print(mydb)

#initialize database and table

#cursor is the object that entirely communicates with the server and through that we create the database

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE testdb") #to create a database use sql command in the execute

mycursor.execute("SHOW DATABASES")

for db in mycursor:
    print(db)   #to print the databases

#to create a table we need to specify which database mysql must be using
# mycursor.execute("CREATE TABLE employee (name VARCHAR (50) , email VARCHAR(50))")

mycursor.execute("SHOW TABLES")

for tb in mycursor:
    print(tb)

# ########## how to insert data in our tables

# sqlFormula = "INSERT INTO employee (name, email) VALUES (%s, %s)"  #%s are used as placeholders where data can be stored
# # user1 = ("a1", "a1@gamil.com") for one user
# # emp = [
# #         ("A1", "a1@gamil.com"),
# #        ("b1", "b1@gamil.com"),
# #        ("c1", "c1@gamil.com"),
# #        ]
# # # mycursor.execute(sqlFormula, user1)  #for single record
# # mycursor.executemany(sqlFormula, emp)

# # mydb.commit()  #migrates to ruby makes sure change is seen in the database

# ############## select and get data ##############

# mycursor.execute("SELECT * FROM employee")

# myresult = mycursor.fetchall() # fetch all the rows from last execution

# #by using fetchone we get only one entry

# for row in myresult:
#     print(row)

# #Query conditions with WHERE and Wildcards

# sql = "SELECT * FROM employee WHERE email = 'a1@gamil.com'"
# mycursor.execute(sql)

# my_result = mycursor.fetchall()

# for result in my_result:
#     print("---------",result)
#     print(result[0])


# # ########we can use wildcard as well 
# # sql = "SELECT * FROM employee WHERE email LIKE '%@gamil.com'"
# # mycursor.execute(sql)

# # my_result = mycursor.fetchall()

# # for result in my_result:
# #     print("---------",result)
#     # print(result[0])
# #we can use %s and pass a tuple as well


# ########## update and limit values in mysql database

# #get the name and change the email

# sql2 = "UPDATE  employee SET email = 'a1@gmail.com' WHERE  name = 'a1'"
# mycursor.execute(sql2)

# my_result1 = mycursor.fetchall()
# mydb.commit()
# for result1 in my_result1:
#     print("((((((()))))))",result1)






################################### db_create.py #####################

import mysql.connector

mydb_create = mysql.connector.connect(
    
        host = "localhost",
        user = 'root',
        password = "*****************"
        )
cursor = mydb_create.cursor()
print(cursor)
# cursor.execute("CREATE DATABASE flask_testing")
# cursor.execute("SHOW DATABASES")
# for db in cursor:
#     print(db)


#################### add_data.py #################


import mysql.connector

mydb = mysql.connector.connect( 

    host = "localhost", 
    user = "root",
    password = "******************",
    database = "sql_course"
    )

mycursor = mydb.cursor()

#create a formula

sqlFormula = "INSERT INTO students (name, age) VALUES  (%s, %s)"

# student1 = ("Rachel", 22)

# mycursor.execute(sqlFormula, student1)

mydb.commit()

#to add multiple entries in our database


students = [('avi', 17),
            ('Jacob', 17),
            ('amanda',32),
            ('Bob',29)
                    ]
mycursor.executemany(sqlFormula, students)
mydb.commit()




############################## select_get_data.py #######################

import mysql.connector

mydb = mysql.connector.connect( 

    host = "localhost", 
    user = "root",
    password = "*******************",
    database = "sql_course"
    )

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM  students")

myresult = mycursor.fetchall() #will fetch all the data from last executed statement

for row in myresult:
    print(row)

mycursor.execute("SELECT age FROM  students")

myresult = mycursor.fetchall() #will fetch all the data from last executed statement

for row in myresult:
    print(row)



############################ WHERE & WILDCARDS ##########################

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "#MYSQL12345**97",
    database = 'sql_course'
)

mycursor = mydb.cursor()

sql = "SELECT * FROM students WHERE age = 17 "

mycursor.execute(sql)

myresult = mycursor.fetchall()

for result in myresult:
    print(result)


#wildcards : if we want to find out that starts with something, ends with something or have that particular phrase, 
# we can use the wildcards which includes the start, end of a given letter of a phrase.

sql = "SELECT * FROM students WHERE name LIKE 'Ra%'"
mycursor.execute(sql)

myresult = mycursor.fetchall()

for result in myresult:
    print(result)

#e.g
sql = "SELECT * FROM students WHERE name = %s"

mycursor.execute(sql,("Rach",))

myresult = mycursor.fetchall()

for result in myresult:
    print("---------",result)




##################### update and limit query ########################


import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "******************",
    database = 'sql_course'
)

mycursor = mydb.cursor()

#updating the queries

#get the name of BOB and set the age

sql = "UPDATE students SET age = 13 WHERE name = 'BOB'"

mycursor.execute(sql)
mydb.commit()

#limiting the results

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM students LIMIT 5")
myresult = mycursor.fetchall()
for result in myresult:
    print(result)   #here we get first five values 
mydb.commit()

print("-----------------")
mycursor.execute("SELECT * FROM students LIMIT 5 OFFSET 2 ")
myresult = mycursor.fetchall()
for result in myresult:
    print(result)   #here we get first five values starting after 2nd value 
mydb.commit()



