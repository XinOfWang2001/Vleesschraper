from ..domain import MeatProduct

from sqlalchemy import URL, create_engine, event

class DataLoader:

    def __init__(self, connection_string: URL):
        self.engine = create_engine(connection_string, pool_reset_on_return=None)
    
    # TODO: Clean up tables.
    def load(self, products: list[MeatProduct]):
        try:
            # An insert query of only
            # Start transaction
            mapping = []
            insert_query = """
            INSERT INTO Stage_Meats (DateCode, SuperMarket, Title, Capitalized_Title, Normal_Price, Current_Price, Discount, Weight)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            temp_table = """
            CREATE TEMPORARY TABLE Stage_Meats (
            DateCode bigint,
            SuperMarket varchar(100),
            Title varchar(255),
            Capitalized_Title varchar(255),
            Normal_Price float,
            Current_Price float,
            Discount int,
            Weight int,
            PRIMARY KEY (DateCode, Capitalized_Title)
            )
            """
            insert_filter = """
            INSERT INTO Meatproduct (DateCode, SuperMarket, Title, Capitalized_Title, Normal_Price, Current_Price, Discount, Weight) 
                SELECT sm.DateCode, sm.SuperMarket, sm.Title, sm.Capitalized_Title, sm.Normal_Price, sm.Current_Price, sm.Discount, sm.Weight
                FROM Stage_Meats sm
                WHERE NOT EXISTS (
                    SELECT 1 
                    FROM MeatProduct mp 
                    WHERE mp.DateCode = sm.DateCode 
                    AND mp.Capitalized_Title = sm.Capitalized_Title
                );
            """
            for meat in products:
                mapping.append(meat.get_tuple())
            
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
            