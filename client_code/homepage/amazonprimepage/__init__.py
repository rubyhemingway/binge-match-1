from ._anvil_designer import amazonprimepageTemplate
from anvil import *

class amazonprimepage(amazonprimepageTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    # the data needed so the code understands which titles it needs to make visible.
    # the following code after the title is telling the code to respond to keywords not the title.
    # used the same method applied to the netflix page, however it took more effort and time because figuring out how to make it respond to keywords took so much research.
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
  def button_1_click(self, **event_args):
    """Go back to homepage"""
    open_form('homepage')

# takes the user to the netflix page
  def outlined_button_1_click(self, **event_args):
    """Go to Netflix page"""
    open_form('netflixpage')

# reloads the amazon prime page
  def outlined_button_2_click(self, **event_args):
    """Reload Amazon Prime page"""
    open_form('amazonprimepage')

  def outlined_button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.search_bar_2.focus()
    pass

  def search_bar_2_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    """Triggered when user presses Enter in the search bar"""
    search_term = self.search_bar_2.text.lower()

    if len(search_term) > 0:
      # Filter for shows that include the search term in their tags
      matches = [item for item in self.media_data
                 if item['type'] == 'show' and search_term in item['tags']]
      self.repeating_panel_1.items = matches
      self.repeating_panel_1.visible = len(matches) > 0
    else:
      self.repeating_panel_1.visible = False


 
