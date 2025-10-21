from ._anvil_designer import netflixpageTemplate
from anvil import *

class netflixpage(netflixpageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # answers to the users search
    # products to keyword 'happy'
    self.media_data = [
      {"title": "Brooklyn Nine-Nine", "type": "show"},
      {"title": "Happy Gilmore 2", "type": "movie"},
      {"title": "Happy Feet", "type": "show"},
      {"title": "Kath and Kim", "type": "movie"},
    ]
    self.repeating_panel_1.visible = False

  def search_bar_pressed_enter(self, **event_args):
    search_term = self.search_bar.text.lower()

    if len(search_term) > 0:
      if search_term == 'happy':
        happy_titles = ["Brooklyn Nine-Nine", "Happy Gilmore", "Kath and Kim"]
        matches = [item for item in self.media_data if item["title"] in happy_titles]
    else:
      matches = [item for item in self.media_data if search_term in item["title"].lower()]

      self.repeating_panel_1.items = matches
      self.repeating_panel_1.visible = len(matches) > 0
    else:
       self.repeating_panel_1.visible = False


#hides the repeating panel when the user is not using the search bar
def repeating_panel_1_hide(self, **event_args):
  """This method is called when the repeating panel is removed from the screen"""
  pass

def outlined_button_1_click(self, **event_args):
  """This method is called when the button is clicked"""
  self.search_bar.focus()
  pass

