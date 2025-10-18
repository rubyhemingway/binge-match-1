from ._anvil_designer import ItemTemplate2Template
from anvil import *


class ItemTemplate2(ItemTemplate2Template):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.title_label.text = self.item['title']

    # Any code you write here will run before the form opens.
