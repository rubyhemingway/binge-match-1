# imported from anvil.
from ._anvil_designer import netflixpageTemplate
from anvil import *

# imported from anvil.
class netflixpage(netflixpageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # this is the data for the repeating panel.
    # if I was able to get access to API's for streaming platforms the information would go here.
    # to initially understand what I was looking at Co-Pilot (as mentioned during tutorial) was helpful in getting me started for my search bar.
    # approved use by tutor to understand my code.
    self.media_data = [
      {"title": "Happy Feet", "type": "show"},
      {"title": "Happiest Season", "type": "movie"},
      {"title": "Happy Endings", "type": "show"},
      {"title": "Happy Place", "type": "movie"},
    ]
    self.repeating_panel_1.visible = False

  # this is the code for when the user presses enter, making the repeating panel drop down.
  # by using anvils 'prewritten' code function when writing in the code, I
  def search_bar_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    search_term = self.search_bar.text.lower()

    # the code which informs the site to show the list of movie titles.
    # co-pilot was also needed for this portion (tutor is aware), along with some in-class activites.
    # however, once this small portion of code was understood the anvil 'Get Started' module was enough for me to delve deeper with my code.
    # also, the Python (conditionals) video on Canvas was helpful, I just needed to adapt it to anvil.
    if len(search_term) > 0:
      matches = [item for item in self.media_data 
                 if search_term in item['title'].lower()]

      # the code which tells the repeating panel what to do.
      # telling the panel to only show if there is a match to what the user is searching.
      self.repeating_panel_1.items = matches
      self.repeating_panel_1.visible = len(matches) > 0
    else:
      self.repeating_panel_1.visible = False

  # highlights the search bar for the user.
  # imported from anvil.
  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.search_bar.focus()

  # hides the repeating panel from view when running the site.
  # unless the user hits enter in the search bar, then it appears.
  # imported from anvil.
  def repeating_panel_1_hide(self, **event_args):
    """This method is called when the repeating panel is removed from the screen"""
    pass

  # takes the user back to the homepage.
  # imported from anvil.
  # SOURCE: (Ryan, 2025, 'Using Layouts to Create a Multi-Page App')
  def home_button01_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form ('homepage')

  # reloads the netflix page.
  # imported from anvil.
  # SOURCE: (Ryan, 2025, 'Using Layouts to Create a Multi-Page App')
  def outlined_button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('netflixpage')





