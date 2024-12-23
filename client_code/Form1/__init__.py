from ._anvil_designer import Form1Template
from .LoggedInPage import LoggedInPage
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

          
class Form1(Form1Template):
    def __init__(self, **properties):
      self.init_components(**properties)
      if anvil.server.call('check_session'):
        open_form(LoggedInPage())
      
    def Login_Btn_click(self, **event_args):
        username = self.name_box.text
        password = self.pw_box.text
        result = anvil.server.call('login', username, password)
        if result['success']:
            open_form(LoggedInPage())
        else:
            alert(result['message'])