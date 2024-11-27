import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import sqlite3

DATABASE_FILE = data_files["database.db"]


# def login(username, password):
#   try:
#       connection = sqlite3.connect(DATABASE_FILE)
#       cursor = connection.cursor()
      
#       query = "SELECT username, isAdmin FROM Users WHERE username = ? AND password = ?"
#       cursor.execute(query, (username, password))
      
#       result = cursor.fetchone()
      
#       if result:
#         username, is_admin = result
#         print("Admin")
#         return {"success": True, "username": username, "isAdmin": bool(is_admin)}
#       else:
#         print("No Admin")
#         return {"success": False, "message": "Invalid username or password."}
  
#   except Exception as e:
#     return {"success": False, "message": f"An error occurred: {str(e)}"}
  
#   finally:
#     connection.close()
@anvil.server.callable
def login(username, password):
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    # UNSICHER: SQL-Abfrage mit direkter String-Konkatenation
    query = f"SELECT username FROM Users WHERE username = '{username}' AND password = '{password}'"
    print("SQL Query:", query) 
    cursor.execute(query)
    result = cursor.fetchone()

    connection.close()

    if result:
        return {"success": True, "username": result[0]}
    else:
        return {"success": False, "message": "Invalid username or password."}
