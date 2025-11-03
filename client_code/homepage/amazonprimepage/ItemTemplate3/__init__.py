# imported from anvil.
from ._anvil_designer import ItemTemplate3Template
from anvil import *

class ItemTemplate3(ItemTemplate3Template):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.set_item(properties.get('item'))

  # imported from anvil, the first line here is imported from anvil, based on the code written in the corresponding page.
  # these 'templates' are made to house the code required for the repeating panel to display the movie/tv show titles.
  # this template is created just like a normal form, however it needs to be embedded in the form it is linked to in order for it to work.
  def set_item(self, item):
    self.item = item
    self.button_2.text = self.item['title']  # Set button text to the title

  # imported from anvil.
  # SOURCE: (Ryan, 2025, 'Using Layouts to Create a Multi-Page App')
  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('homepage.amazonprimepage.theoffice')

  
    

