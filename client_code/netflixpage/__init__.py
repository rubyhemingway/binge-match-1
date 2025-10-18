from ._anvil_designer import netflixpageTemplate
from anvil import *

class netflixpage(netflixpageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.media_data = [
      {"title": "Happy", "type": "show"},
      {"title": "Happiest Season", "type": "movie"},
      {"title": "Happy Endings", "type": "show"},
      {"title": "Happy Place", "type": "movie"},
      {"title": "The Office", "type": "show"},
      {"title": "Inception", "type": "movie"},
      {"title": "Stranger Things", "type": "show"},
    ]
    self.repeating_panel_1.visible = False

  def search_bar_pressed_enter(self, **event_args):
    search_term = self.search_bar.text.lower()

    if len(search_term) > 0:
      matches = [item for item in self.media_data 
                 if search_term in item['title'].lower()]

      self.repeating_panel_1.items = matches
      self.repeating_panel_1.visible = len(matches) > 0
    else:
      self.repeating_panel_1.visible = False

  def repeating_panel_1_hide(self, **event_args):
    """This method is called when the repeating panel is removed from the screen"""
    pass

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.search_bar.focus()
    pass

