from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

level = 1

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.Level_Label.text = "Level: 1"
    # Any code you write here will run before the form opens.

  def Login_Btn_click(self, **event_args):
      # Inhalte der Eingabefelder abrufen
      username = self.name_box.text
      password = self.pw_box.text
  
      # Debugging (optional, falls du die Werte überprüfen möchtest)
      print(f"Username: {username}, Password: {password}")

     
      result,text = callLogin(username, password)
      self.Level_Label.text = f"Level: {level}"
    
      if result['success']:
              alert(text) 
      else:
          print(f"Fehler: {result['message']}")

  def save_checkbox_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    pass

def callLogin(username, password):
  global level
  if level == 1:
    result = anvil.server.call('loginLvl1', username, password)
    text = f"Willkommen, {result['username']}!"
    level += 1
  elif level == 2:
    result = anvil.server.call('loginLvl2', username, password)
    if result['isAdmin']:
      text = f"Willkommen, mr Admin {result['username']}!"
      level += 1
      
    else:
      text = f"Willkommen, {result['username']}, aber du bist kein Admin!"
  elif level == 3:
    result = anvil.server.call('loginLvl3', username, password)
    level += 1
  elif level == 4:
    result = anvil.server.call('loginLvl4', username, password)
    level += 1
  else:
    level = 1
  return result, text