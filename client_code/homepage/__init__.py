#anvil template
from ._anvil_designer import homepageTemplate
from anvil import *
class homepage(homepageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
   
  #search bar basic responses
  #microsoft copilot helped with the formatting of this portion, along with in-class code conundrums done in Google Colab
  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('netflixpage')
    pass

