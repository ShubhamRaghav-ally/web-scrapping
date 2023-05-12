import pandas as pd
import mysql.connector
from roughShete import each_row as df2
# establish MySQL connection
mydb = mysql.connector.connect(
  host="3.6.145.79",
  user="91w_staging",
  password="91w@8iut",
  database="91wheels"
)
# define query to fetch data from table
query = "SELECT city_id, city_name,city_alias FROM 91wheels_location_cities"

# fetch data from table and store in a dataframe
df1 = pd.read_sql(query, mydb)
# df1['city_name'] = df1['city_name'] + df1['city_alias']
# print("ALIAS========>",df1['city_alias'])
df3 = pd.merge(df1, df2, on=['city_name'], how='inner')
# close MySQL connection
mydb.close()

# display the dataframe
print("df33333333333333=============>",df3[['city_name', 'city_id']])
