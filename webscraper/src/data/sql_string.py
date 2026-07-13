
def _read_sql_file(file_path: str) -> str:
    with open(file_path, "r") as file:
        query = file.read()
    return query

def get_filter_existing_meat_query() -> str:
    return _read_sql_file("src/data/db/filter_existing_meat.sql")

def get_create_temp_table_query() -> str:
    return _read_sql_file("src/data/db/create_temp_table.sql")