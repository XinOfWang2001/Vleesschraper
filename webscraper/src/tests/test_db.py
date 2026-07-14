import unittest as ut
from datetime import datetime
from sqlalchemy import URL, create_engine, text

from src.domain import MeatProduct
from src.logic import DataLoader
from src.data import get_create_meat_table_query

class TestDBConnection(ut.TestCase):

    def __init__(self, methodName = "runTest"):
        self.connection_string_collect= URL.create(
            drivername="postgresql+psycopg2",
            username="test",
            password="test_password",
            host="127.0.0.1",
            port=51000,
            database="test"
            )
        self.engine = create_engine(self.connection_string_collect)
        super().__init__(methodName)
    
    def test_insertion_3_new_entities(self):
        sql = get_create_meat_table_query()
        # Create tables
        with self.engine.connect() as conn:
            conn.execute(text(sql))
            conn.commit()

        entity1 = MeatProduct(date_time=datetime(2001, 1, 1, 13, 45), supermarket="AH", full_title="test1", capitilized_title="TEST1", normal_price=3.0, current_price=3.0, weight=200)
        entity2 = MeatProduct(date_time=datetime(2001, 1, 1, 13, 45), supermarket="AH", full_title="test2", capitilized_title="TEST2", normal_price=3.0, current_price=3.0, weight=200)
        entity3 = MeatProduct(date_time=datetime(2001, 1, 1, 13, 45), supermarket="AH", full_title="test3", capitilized_title="TEST3", normal_price=3.0, current_price=3.0, weight=200)
        entity4 = MeatProduct(date_time=datetime(2001, 1, 2, 13, 45), supermarket="AH", full_title="test3", capitilized_title="TEST3", normal_price=3.0, current_price=3.0, weight=200)
        bulk = [entity1, entity2, entity3,entity4]
        loader = DataLoader(self.connection_string_collect)
        # Act
        loader.load(bulk)

        # Validate

if __name__ == "main":
    ut.main()