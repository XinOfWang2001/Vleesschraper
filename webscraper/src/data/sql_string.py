
def get_filter_existing_meat_query() -> str:
    with open("src/data/db/filter_existing_meat.sql", "r") as file:
        query = file.read()
    return query

def get_create_temp_table_query() -> str:
    with open("src/data/db/create_temp_table.sql", "r") as file:
        query = file.read()
    return query