import psycopg2

from authors import Author_nov

conn = psycopg2.connect(
    dbname="brgeicfqg8kyazonirom",
    user="ulwgoripw8ejfilgoi5u",
    password="yIus83C46Zx1VgDBZ5UjzY04BQrST3",
    host="brgeicfqg8kyazonirom-postgresql.services.clever-cloud.com",
    port=50013
)
# we have to create a cursor=conn.cursor() to communicate with the DB
cursor = conn.cursor()
print(cursor)
cursor.execute('SELECT* FROM authors')
autori = cursor.fetchall()
print(autori)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
cursor.execute('SELECT* FROM authors order by author_id DESC')
prvy_author = cursor.fetchone()
print(prvy_author)
author1 = Author_nov(4, "juan perez", "je to dobry author")
print(author1)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''''
Create an instance of the class
author1 = ID_Author(1, "John Doe", "John Doe is a famous author.")
print(author1)
author2 = ID_Author(4, "Ruben Dario", "Azul Modernism")
print(author2)
'''
