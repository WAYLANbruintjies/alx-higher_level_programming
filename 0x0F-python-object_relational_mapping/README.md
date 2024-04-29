* 0x0F. Python - Object-relational mapping
(Python /OOP /SQL /MySQL /ORM /SQLAlchemy)

Learning Objectives
At the end of this project, expected learning outcomes will be to explain to anyone, without the help of Google:

Why Python programming is awesome
How to connect to a MySQL database from a Python script
How to SELECT rows in a MySQL table from a Python script
How to INSERT rows in a MySQL table from a Python script
What ORM means
How to map a Python Class to a MySQL table
How to create a Python Virtual Environment

1) In the first part, the module MySQLdb will be used to connect to a MySQL database and execute your SQL queries.
2) In the second part, the module SQLAlchemy is used which is an Object Relational Mapper (ORM).

The biggest difference between the 2 is: no more SQL queries! The purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. Also code won’t be “storage type” dependent, making it easier to change your storage without re-writing your entire project.
