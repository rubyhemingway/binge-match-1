from ._anvil_designer import Form1Template
from anvil import *
class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # netflix button code
    self.button_1.text = "Netflix"
    self.button_1.background = "Black"
    self.button_1.foreground = "Red"
    
 



  
