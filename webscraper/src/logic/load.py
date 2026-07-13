from sqlalchemy import URL, create_engine

from ..data import get_create_temp_table_query, get_filter_existing_meat_query
from ..domain import MeatProduct


class DataLoader:

    def __init__(self, connection_string: URL):
        self.engine = create_engine(connection_string, pool_reset_on_return=None)
    
    def load(self, products: list[MeatProduct]):
        try:
            # An insert query of only
            
            mapping = []
            insert_query = """
            INSERT INTO Stage_Meats (DateCode, Date, SuperMarket, Title, Capitalized_Title, Normal_Price, Current_Price, Discount, Weight)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            temp_table = get_create_temp_table_query()
            insert_filter = get_filter_existing_meat_query()
            for meat in products:
                mapping.append(meat.get_tuple())
                
            # Start transaction
            with self.engine.begin() as conn:
                # Create temp table
                conn.exec_driver_sql(temp_table)
                for record in mapping:
                    conn.exec_driver_sql(insert_query, record)
                # Perform JOIN with existing table
                conn.exec_driver_sql(insert_filter)
                conn.exec_driver_sql("DISCARD TEMP")
                # # Close transaction
                conn.commit()
        except Exception as e:
            raise e
            