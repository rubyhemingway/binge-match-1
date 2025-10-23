from ._anvil_designer import ItemTemplate2Template
from anvil import *

# to make items appear in the repeating panel, that are title names they needed to be coded in a different template
# i had to use copilot to figure this part out, but once i got it it was pretty intuiative.
class ItemTemplate2(ItemTemplate2Template):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.button_1.text = self.item['title']

# defining the item
  def set_item(self, item):
    self.item = item

# this is the code for the buttons which appear in the panel when the user presses enter.
# clicking on the title names will take the user to a review page of that title.
# same open form tutorial from anvil.works used.
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('netflixpage.happyfeet')
   
