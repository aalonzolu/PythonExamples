import MySQLdb

connection = MySQLdb.connect(
                host = 'xx.rds.amazonaws.com',
                user = '',
                passwd = '')  # create the connection

cursor = connection.cursor()     # get the cursor

cursor.execute("SHOW DATABASES")    # execute 'SHOW TABLES' (but data is not returned)
tables = cursor.fetchall()

query = input("Ingrese SQL: (%d para la base de datos)>> ")
#print(query)
print('')
print('')
array_databases = []
for (table_name,) in cursor:
        tmp = table_name.split("_")
        if tmp[0]=="geducar" and tmp[1] != "website":
            #print(table_name)
            tmp_query = query.replace("%d",table_name)
            print(tmp_query)
