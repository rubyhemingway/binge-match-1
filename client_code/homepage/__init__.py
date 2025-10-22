#anvil template
from ._anvil_designer import homepageTemplate
from anvil import *
class homepage(homepageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

# the 'open form' function is made to add pages into the site, to make the screens change.
# I learnt how to do that from a tutorial in anvil.
  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('netflixpage')

  def home_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  



