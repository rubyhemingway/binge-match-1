from ._anvil_designer import Form1Template
from anvil import *
class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def sidebar_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass



  
