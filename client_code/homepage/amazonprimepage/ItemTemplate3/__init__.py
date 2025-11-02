from ._anvil_designer import ItemTemplate3Template
from anvil import *

class ItemTemplate3(ItemTemplate3Template):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.set_item(properties.get('item'))

  def set_item(self, item):
    self.item = item
    self.button_2.text = self.item['title']  # Set button text to the title

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('homepage.amazonprimepage.theoffice')

  
    

