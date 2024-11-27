from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def Login_Btn_click(self, **event_args):
      # Inhalte der Eingabefelder abrufen
      username = self.name_box.text
      password = self.pw_box.text
  
      # Debugging (optional, falls du die Werte überprüfen möchtest)
      print(f"Username: {username}, Password: {password}")
  
      # Aufrufen der Login-Funktion auf dem Server
      result = anvil.server.call('login', username, password)
  
      # Ergebnis verarbeiten
      if result['success']:
          if result['isAdmin']:
              alert(f"Willkommen, Admin {result['username']}!")
          else:
              alert(f"Willkommen, {result['username']}!")
      else:
          print(f"Fehler: {result['message']}")

  def save_checkbox_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    pass
