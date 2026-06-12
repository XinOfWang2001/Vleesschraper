from ..domain import MeatProduct


class DataLoader:

    def __init__(self, connection_string: str):
        pass

    def load(self, products: list[MeatProduct]):
        try:
            # An insert query of only
            query = """
            INSERT INTO oltp_meat WITH (?, ?, ?, ?, ?)
            """
            while(len(products) > 0):
                meat = products.pop()
                insert_query = f"({meat.date_time}, {meat.full_title}, {meat.capitilized_title}, {meat.current_price}, {meat.supermarket})"
                query += insert_query
            # execute query
            query
        except:
            print("Something went wrong with the insertion")