import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import sqlite3


DATABASE_FILE = data_files["database.db"]

def get_db_connection():
    return sqlite3.connect(DATABASE_FILE)

@anvil.server.callable
def login(username, password):
    db = sqlite3.connect(DATABASE_FILE)
    cursor = db.cursor()
    try:
        query = f"SELECT AccountNo, isAdmin FROM Users WHERE username='{username}' AND password='{password}'"
        result = cursor.execute(query).fetchone()
        if result:
            anvil.server.session['is_logged_in'] = True
            anvil.server.session['account_no'] = result[0]
            return {'success': True, 'AccountNo': result[0], 'isAdmin': bool(result[1])}
        else:
            return {'success': False, 'message': 'Benutzer oder Passwort falsch.'}
    except Exception as e:
        return {'success': False, 'message': str(e)}
    finally:
        db.close()
      
@anvil.server.callable
def check_session():
    return anvil.server.session.get('is_logged_in', False)

@anvil.server.callable
def logout():
    if 'is_logged_in' in anvil.server.session:
        del anvil.server.session['is_logged_in']
    if 'account_no' in anvil.server.session:
        del anvil.server.session['account_no']
    return {'success': True}


@anvil.server.callable
def get_balance(account_no):
    db = sqlite3.connect(DATABASE_FILE)
    cursor = db.cursor()
    try:
        query = f"SELECT balance FROM Balances WHERE AccountNo={account_no}"
        result = cursor.execute(query).fetchone()
        if result:
            return {'success': True, 'balance': result[0]}
        else:
            return {'success': False, 'message': 'Kein Kontostand gefunden.'}
    except Exception as e:
        return {'success': False, 'message': str(e)}
    finally:
        db.close()
