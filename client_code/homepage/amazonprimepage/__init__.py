# imported from anvil.
from ._anvil_designer import amazonprimepageTemplate
from anvil import *

# imported from anvil.
class amazonprimepage(amazonprimepageTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    # the data needed so the code understands which titles it needs to make visible.
    # the following code after the title is telling the code to respond to keywords not the title.
    # used the same method applied to the netflix page, however it took more effort and time because figuring out how to make it respond to keywords took so much research.
     # co-pilot was also needed for this portion (tutor is aware).
    self.media_data = [
      {"title": "The Office", "type": "show", "tags": ["funny", "comedy", "sit-com"]},
      {"title": "South Park", "type": "show", "tags": ["funny", "comedy"]},
      {"title": "Clarkson's Farm", "type": "show", "tags": ["funny", "comedy"]},
      {"title": "The Boys", "type": "show", "tags": ["action", "dark"]},
      {"title": "Fleabag", "type": "show", "tags": ["funny", "drama"]},
      {"title": "Top Gear", "type": "show", "tags": ["funny", "cars", "simple"]},
    ]

    # this is the code to hide the repeating panel
    # only made visible when the user presses enter
    self.repeating_panel_1.visible = False

# takes the user to the homepage
  # imported from anvil.
  # SOURCE: (Ryan, 2025, 'Using Layouts to Create a Multi-Page App')
  def button_1_click(self, **event_args):
    """Go back to homepage"""
    open_form('homepage')

# takes the user to the netflix page
  # imported from anvil.
  # SOURCE: (Ryan, 2025, 'Using Layouts to Create a Multi-Page App')
  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('netflixpage')

# reloads the amazon prime page
  # imported from anvil.
  # SOURCE: (Ryan, 2025, 'Using Layouts to Create a Multi-Page App')
  def outlined_button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('amazonprimepage')

#focuses the users mouse to the search bar, showing that they can type in it.
  # imported from anvil.
  def outlined_button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.search_bar_2.focus()
    pass

  # when the user hits enter the repeating panel becomes visible.
  # imported from anvil.
  # functions video on Canvas, was helpful for this part of the code. (reference in master reference list)
  def search_bar_2_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    search_term = self.search_bar_2.text.lower()

    # this means if the length of the input is greater than 0, making the repeating panel become visible.
    # co-pilot was also needed for this portion (tutor is aware), along with some in-class activites.
    # however, once this small portion of code was understood the anvil 'Get Started' module was enough for me to delve deeper with my code.
    # also, the Python (conditionals) video on Canvas was helpful, I just needed to adapt it to anvil. (reference in master reference list)
    if len(search_term) > 0:
      # the code which produces an output based on the tags written in the data code.
      # an example being, 'funny', 'simple', 'sit-com'
      matches = [item for item in self.media_data
                 if item['type'] == 'show' and search_term in item['tags']]
      self.repeating_panel_1.items = matches
      self.repeating_panel_1.visible = len(matches) > 0
    else:
      self.repeating_panel_1.visible = False


 
