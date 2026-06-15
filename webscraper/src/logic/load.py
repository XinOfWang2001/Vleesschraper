from ..domain import MeatProduct

from sqlalchemy import URL
from sqlalchemy import create_engine

class DataLoader:

    def __init__(self, connection_string: URL):
        self.engine = create_engine(connection_string)

    def load(self, products: list[MeatProduct]):
        try:
            # An insert query of only
            # Start transaction
            insert_query = """
            INSERT INTO Stage_Meats (DateCode, Title, Capitalized_Title, Normal_Price, Current_Price, Discount)
            VALUES (%s, %s, %s, %s, %s, %s)
            """

            mapping = []
            temp_table = """
            CREATE TEMPORARY TABLE Stage_Meats (
                DateCode bigint,
                Title varchar(255),
                Capitalized_Title varchar(255),
                Normal_Price float,
                Current_Price float,
                Discount int,
                PRIMARY KEY (DateCode, Capitalized_Title)
            )
            """
            insert_filter = """
            INSERT INTO Meatproduct (DateCode, Title, Capitalized_Title, Normal_Price, Current_Price, Discount) 
                SELECT sm.DateCode, sm.Title, sm.Capitalized_Title, sm.Normal_Price, sm.Current_Price, sm.Discount
                FROM Stage_Meats sm
                WHERE NOT EXISTS (
                    SELECT 1 
                    FROM MeatProduct mp 
                    WHERE mp.DateCode = sm.DateCode 
                    AND mp.Capitalized_Title = sm.Capitalized_Title
                );
            """
            for meat in products:
                mapping.append((meat.get_date_code(), meat.full_title, meat.capitilized_title, meat.normal_price, meat.current_price, 0))
            
            with self.engine.begin() as conn:
                # Create temp table
                conn.exec_driver_sql(temp_table)
                for record in mapping:
                    conn.exec_driver_sql(insert_query, record)
                # Perform JOIN with existing table
                conn.exec_driver_sql(insert_filter)
                # # Close transaction
                conn.commit()
        except Exception as e:
            e.with_traceback()
            print("Something went wrong with the insertion")
            