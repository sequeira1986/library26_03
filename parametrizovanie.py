import psycopg2

conn = psycopg2.connect(
    dbname="brgeicfqg8kyazonirom",
    user="ulwgoripw8ejfilgoi5u",
    password="yIus83C46Zx1VgDBZ5UjzY04BQrST3",
    host="brgeicfqg8kyazonirom-postgresql.services.clever-cloud.com",
    port=50013
)
cursor = conn.cursor()


name = 'Octavio Paz'
bio = 'the best mexican writer'

cursor.execute(""" 
INSERT INTO authors (name, bio)
VALUES (%s,%s)
""", (name, bio))

conn.commit()

print("Novy author bol pridane.")
cursor.close()



