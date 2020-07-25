from sqlalchemy import create_engine
import pandas as pd

SQLALCHEMY_DATABASE_URL = "sqlite:///./localities.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# used to insert data from portugal.csv to the database table I've created 
# data = pd.DataFrame(pd.read_csv('portugal.csv', skiprows = 1))
# data.to_sql('portugal', con=engine, if_exists='replace', index=True)

# verifying if data was inserted
for row in engine.execute('''
               SELECT * FROM portugal 
               ''').fetchfirst():
    print(row)
    