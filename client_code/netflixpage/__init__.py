from ._anvil_designer import netflixpageTemplate
from anvil import *

class netflixpage(netflixpageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def search_bar_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

def recommendations(self, **event_args):
  self.recommendations = {
    "happy": ["Brooklyn Nine-Nine", "Ted Lasso", "Parks and Rec"],
    "sad": ["BoJack Horseman", "13 Reasons Why", "This Is Us"],
    "excited": ["Stranger Things", "Money Heist", "Wednesday"],
    "romantic": ["Bridgerton", "Outlander", "Heartstopper"]
  }

