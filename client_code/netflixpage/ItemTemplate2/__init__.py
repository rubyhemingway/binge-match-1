from ._anvil_designer import ItemTemplate2Template
from anvil import *

class ItemTemplate2(ItemTemplate2Template):
  def __init__(self, **properties):
    self.init_components(**properties)

  def set_item(self, item):
    self.item = item
    self.title_button_1.text = item['title']
