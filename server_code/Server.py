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
def loginLvl1(username, password):
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    query = f"SELECT username FROM Users WHERE username = '{username}' AND password = '{password}'"
    print("SQL Query:", query)
    cursor.execute(query)
    result = cursor.fetchone()

    connection.close()

    if result != None:
        [username] = result
        return {"success": True, "username": username}
    else:
        return {"success": False, "message": "Invalid username or password."}

@anvil.server.callable
def loginLvl2(username, password):
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    query = f"SELECT username, isAdmin FROM Users WHERE username = '{username}' AND password = '{password}'"
    print("SQL Query:", query)
    cursor.execute(query)
    result = cursor.fetchone()

    connection.close()

    if result != None:
        [username, is_admin] = result
        return {"success": True, "username": username, "isAdmin": bool(is_admin)}
    else:
        return {"success": False, "message": "Invalid username or password."}

@anvil.server.callable
def loginLvl3(username, password):
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    query = f"SELECT username, isAdmin FROM Users WHERE username = '{username}' AND password = '{password}'"
    print("SQL Query:", query)
    cursor.execute(query)
    result = cursor.fetchone()

    connection.close()

    if result != None:
        [username, is_admin] = result
        return {"success": True, "username": username, "isAdmin": bool(is_admin)}
    else:
        return {"success": False, "message": "Invalid username or password."}

@anvil.server.callable
def loginLvl4(username, password):
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    query = f"SELECT username, isAdmin FROM Users WHERE username = '{username}' AND password = '{password}'"
    print("SQL Query:", query)
    cursor.execute(query)
    result = cursor.fetchone()

    connection.close()

    if result != None:
        [username, is_admin] = result
        return {"success": True, "username": username, "isAdmin": bool(is_admin)}
    else:
        return {"success": False, "message": "Invalid username or password."}