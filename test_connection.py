import psycopg2
from psycopg2 import connect

# declare the connection string specifying
# the host name database name
# use name and password


# use connect function to establish the connection
conn = psycopg2.connect(database="my_db", user="my_user", password="qwerty", host="localhost", port="5438")

cursor = conn.cursor()

sql = '''CREATE TABLE EMPLOYER (
                employer_id SERIAL PRIMARY KEY,
                employer_name VARCHAR(255) NOT NULL,
                employer_estd INT,
                employer_location VARCHAR(255),
                employer_type VARCHAR(255)
)'''

cursor.execute(sql)
print("Table created successfully.........")
conn.commit()


cursor.close()
