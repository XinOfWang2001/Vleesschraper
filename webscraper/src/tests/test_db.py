import unittest as ut
from datetime import datetime
from sqlalchemy import URL, create_engine, text

from src.domain import MeatProduct
from src.logic import DataLoader

class TestDBConnection(ut.TestCase):
    
    # def test_retrieval(self):
    #     connection_string_collect= URL.create(
    #         drivername="postgresql+psycopg2",
    #         username="hero",
    #         password="localpassword",
    #         host="127.0.0.1",
    #         port=51000,
    #         database="hero"
    #         )
    #     engine = create_engine(connection_string_collect)
        
    #     with engine.connect() as conn:
    #         result = conn.execute(text('SELECT * FROM Meatproduct LIMIT 50'))
    #         rows = result.fetchall()  # Fetches all rows into a Python list
    
    #         # Check if the number of fetched rows matches your expectation
    #         self.assertEqual(50, len(rows))
    
    def test_insertion_3_new_entities(self):
        connection_string_collect= URL.create(
            drivername="postgresql+psycopg2",
            username="test",
            password="test_password",
            host="127.0.0.1",
            port=51000,
            database="test"
            )
        engine = create_engine(connection_string_collect)
        sql = ""
        with open("src/data/db/create_meat_table.sql") as file:
            sql = file.read()
        # Create tables
        with engine.connect() as conn:
            conn.execute(text(sql))
            conn.commit()

        entity1 = MeatProduct(date_time=datetime(2001, 1, 1, 13, 45), supermarket="AH", full_title="test1", capitilized_title="TEST1", normal_price=3.0, current_price=3.0, weight=200)
        entity2 = MeatProduct(date_time=datetime(2001, 1, 1, 13, 45), supermarket="AH", full_title="test2", capitilized_title="TEST2", normal_price=3.0, current_price=3.0, weight=200)
        entity3 = MeatProduct(date_time=datetime(2001, 1, 1, 13, 45), supermarket="AH", full_title="test3", capitilized_title="TEST3", normal_price=3.0, current_price=3.0, weight=200)
        entity4 = MeatProduct(date_time=datetime(2001, 1, 2, 13, 45), supermarket="AH", full_title="test3", capitilized_title="TEST3", normal_price=3.0, current_price=3.0, weight=200)
        bulk = [entity1, entity2, entity3,entity4]
        loader = DataLoader(connection_string_collect)
        # Act
        loader.load(bulk)