import pandas as pd
import sqlalchemy
host="localhost",
user="root",
password="root1234"
host='localhost'
port_db='3306'
database="thun"

engine = sqlalchemy.create_engine('mysql+mysqldb://root:root1234@localhost:3306/thun')


df = pd.read_csv('sumary.csv')

print(df)
df.to_sql('customers',con=engine,index=False,if_exists='replace')