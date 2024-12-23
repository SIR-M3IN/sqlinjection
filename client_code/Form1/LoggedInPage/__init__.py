from ._anvil_designer import LoggedInPageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class LoggedInPage(LoggedInPageTemplate):
    def __init__(self, account_no=None, **properties):
        self.init_components(**properties)
        self.account_no = account_no

    def form_show(self, **event_args):
        try:
            url_args = get_url_hash()
            if 'AccountNo' in url_args:
                injected_account_no = url_args['AccountNo']
                result = anvil.server.call('get_balance', injected_account_no)
                if result['success']:
                    self.balance_label.text = f"Ihr Kontostand: {result['balance']} EUR"
                else:
                    self.balance_label.text = f"Fehler: {result['message']}"
        except Exception as e:
            self.balance_label.text = f"Ein Fehler ist aufgetreten: {str(e)}"

    def logoutBtn_click(self, **event_args):
        result = anvil.server.call('logout')
        if result['success']:
            self.refresh_data_bindings()
