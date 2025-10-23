from ._anvil_designer import netflixpageTemplate
from anvil import *

class netflixpage(netflixpageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # answers to the users search
    # products to keyword 'happy'
    self.media_data = [
      {"title": "Happy Feet", "type": "show"},
      {"title": "Happiest Season", "type": "movie"},
      {"title": "Happy Endings", "type": "show"},
      {"title": "Happy Place", "type": "movie"},
    ]
    self.repeating_panel_1.visible = False

  # this is the code for when the user presses enter, making the repeating panel drop down
  def search_bar_pressed_enter(self, **event_args):
    search_term = self.search_bar.text.lower()

# the code which informs the site to show the list of movie titles.
    if len(search_term) > 0:
      matches = [item for item in self.media_data 
                 if search_term in item['title'].lower()]

      # the code which tells the repeating panel what to do.
      # telling the panel to only show if there is a match to what the user is searching.
      self.repeating_panel_1.items = matches
      self.repeating_panel_1.visible = len(matches) > 0
    else:
      self.repeating_panel_1.visible = False

# hides the repeating panel from view when running the site.
# unless the user hits enter in the search bar, then it appears.
  def repeating_panel_1_hide(self, **event_args):
    """This method is called when the repeating panel is removed from the screen"""
    pass

# makes the users mouse focus to the search bar
  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.search_bar.focus()
    pass

# takes the user back to the homepage
# figured out how to code this with an anvil.works tutorial.
  def home_button01_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form ('homepage')

# this button will always bring the user to the netlfix page.
  def outlined_button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('netflixpage')
