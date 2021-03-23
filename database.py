import mysql.connector


# conn = mysql.connector.connect(host='127.0.0.1', user='root', password='hujisanroku2')
# cursor = conn.cursor()
#
# cursor.execute('CREATE DATABASE test_mysql_database')
#
# cursor.close()
# conn.close()

conn = mysql.connector.connect(host='127.0.0.1', database='mydb')
cursor = conn.cursor()
cursor.execute(
	'CREATE TABLE persons('
	'id int NOT NULL AUTO_INCREMENT,'
	'name varchat(14) NOT NULL,'
	'PRIMARY KEY(id)')

conn.commit()
cursor.close()
conn.close()