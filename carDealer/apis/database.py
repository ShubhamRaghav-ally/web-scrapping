from getpass import getpass
from mysql.connector import connect, Error
import mysql.connector
# MYSQL_HOST = 3.6.145.79
# MYSQL_DATABASE_NAME = 91wheels
# MYSQL_USERNAME = 91w_staging
# MYSQL_PASSWORD = 91w@8iut
# MYSQL_DIALECT = "mysql"
mydb = mysql.connector.connect(
  host="3.6.145.79",
  user="91w_staging",
  password="91w@8iut",
  database="91wheels"
)
mycursor = mydb.cursor()
# sql = "INSERT INTO `91wheels_guest_user_log` SET `guest_id`=%s, `user_id`=%s, `status`=%s"
# cursor.execute(sql, (guest_id, user_id, status))

# def insert_customer(company_name,address,pincode,website,phone,latitude,longitude,city_name):
def insert_customer(each_row):
    print("each_row insert db ",each_row)

    for index, row in each_row.iterrows():
      print("After First Loop",row.items(),"===================",index)
      sql = "INSERT INTO 91wheels_scrap_dealers SET "
      for col, val in row.items():
          sql += f"`{col}`='{val}', "

      sql = sql.rstrip(", ")
      print("sql ",sql)
      mycursor.execute(sql)

      mydb.commit()
