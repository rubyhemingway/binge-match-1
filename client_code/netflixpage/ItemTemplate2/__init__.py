from ._anvil_designer import ItemTemplate2Template
from anvil import *

class ItemTemplate2(ItemTemplate2Template):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.button_1.text = self.item['title']

  def set_item(self, item):
    self.item = item

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
   
