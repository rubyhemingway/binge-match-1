# auto anvil import for the template
from ._anvil_designer import theofficeTemplate
from anvil import *

class theoffice(theofficeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  # focuses the users mouse to the search bar.
  # functions video on Canvas, was helpful for this part of the code. (reference in master reference list)
  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.theoffice_reviewbox.focus()

  def theoffice_reviewbox_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    user_input = self.theoffice_reviewbox.text.strip()
    self.theoffice_reviewbox.text = ""

  # this is the code for the label which appears under the review box when the user presses enter.
  # this code is for the label to be visible or not.
  # i used what I learnt when creating the search bar to help me write this code.
    # conditionals python video on Canvas was used for this portion. along with anvils prewritten code which pops up when you begin typing.
    if user_input:
      self.theoffice_outputreview.text = user_input
      self.theoffice_outputreview.visible = True
    else:
      self.theoffice_outputreview.text = ""
      self.theoffice_outputreview.visible = False

#takes the user back to the homepage
  # SOURCE: (Ryan, 2025, 'Using Layouts to Create a Multi-Page App')
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('homepage')

  # SOURCE: (Ryan, 2025, 'Using Layouts to Create a Multi-Page App')
  def outlined_button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('netflixpage')

  # SOURCE: (Ryan, 2025, 'Using Layouts to Create a Multi-Page App')
  def outlined_button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('homepage.amazonprimepage')
