import mysql.connector as sqltor
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

mycon = sqltor.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD, database=DB_NAME)
if mycon.is_connected():
    print("Successfully connected to MySQL")

cursor = mycon.cursor()
