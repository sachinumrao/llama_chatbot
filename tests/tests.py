# write code for testing inserts and reads from sqlite3 table

import sqlite3
from contextlib import closing


def test_inserts():
    
    database_name = "./../database/chatbot.db"
    table_name = "llama_chatbot_logs"
    
    test_data = [
        {
            "id": 1,
            "timestamp": 100,
            "query": "test_query",
            "response": "test_response1"
        },
        {
            "id": 2,
            "timestamp": 200,
            "query": "test_query",
            "response": "test_response2"
        }
    ]
    
    database_name = "./database/chatbot.db"
    table_name = "llama_chatbot_logs"
    
    insert_query = f"INSERT INTO {table_name} VALUES (:id, :timestamp, :query, :response)"
    
    # create db connection
    with closing(sqlite3.connect(database_name)) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(insert_query, test_data)
    
    print("Logging table record inserts successful...")
    
    
def test_reads():
    database_name = "./../database/chatbot.db"
    table_name = "llama_chatbot_logs"
    
    read_query = ""
    pass


def test_deletes():
    database_name = "./../database/chatbot.db"
    table_name = "llama_chatbot_logs"
    
    delete_query = ""
    
    pass


if __name__ == "__main__":
    print("Validating insert ops...")
    test_inserts()
    
    print("Valdiating read ops...")
    test_reads()
    
    print("Validating delete ops...")
    test_deletes()