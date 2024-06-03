import sqlite3


def main():
    # define table schema
    
    column_dtypes = {
        "id": "INTEGER",
        "timestamp": "INTEGER",
        "query": "TEXT",
        "response": "TEXT"
    }
    
    table_name = "llama_chatbot_logs"
    table_creation_query = f"CREATE TABLE {table_name} ("
    for field, dtype in column_dtypes.items():
        table_creation_query += f" {field} {dtype},"
    
    table_creation_query = table_creation_query.rstrip(",")
    table_creation_query += ")"
    
    print("Table creation query:")
    print(table_creation_query)
    
    # create table in database
    database_name = "./database/chatbot.db"
    db = sqlite3.connect(database_name)
    cursor = db.cursor()
    
    # run table creation query
    cursor.execute(table_creation_query)
    print("Logging table initialized successfully...")
    
    # close db connections
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()