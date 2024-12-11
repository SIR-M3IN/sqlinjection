from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):
    def __init__(self, **properties):
        self.init_components(**properties)

    def Login_Btn_click(self, **event_args):
        username = self.name_box.text
        password = self.pw_box.text
        
        try:
            result = anvil.server.call('login', username, password)
            if result['success']:
                alert(f"Willkommen {username}!")
            else:
                alert(f"Login fehlgeschlagen: {result['message']}")
        except Exception as e:
            alert(f"Ein Fehler ist aufgetreten: {str(e)}")

    def balance_button_click(self, **event_args):
        account_no = self.account_no_box.text
        
        try:
            result = anvil.server.call('get_balance', int(account_no))
            if result['success']:
                balance = result['balance']
                alert(f"Ihr Kontostand beträgt: {balance} EUR")
            else:
                alert(f"Fehler: {result['message']}")
        except Exception as e:
            alert(f"Ein Fehler ist aufgetreten: {str(e)}")
