from ._anvil_designer import happyfeetTemplate
from anvil import *

# anvil given template which is required in order for code written to run properly.
class happyfeet(happyfeetTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

  # takes user back to netflix page.
  # anvil tutorial used for this code.
  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('netflixpage')

  # takes the user back to the homepage of the site.
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('homepage')

  # focuses the users mouse to the text box to write a review on the movie.
  def outlined_button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.reviewbox_1.focus()

# allows the user to write a review which gets posted on the site so other users can see it.
  def reviewbox_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    user_input = self.reviewbox_1.text.strip()
    self.reviewbox_1.text = ""

# this is the code for the label which appears under the review box when the user presses enter.
# this code is for the label to be visible or not.
# i used what I learnt when creating the search bar to help me write this code.
    if user_input:
      self.output_label.text = user_input
      self.output_label.visible = True
    else:
      self.output_label.text = ""
      self.output_label.visible = False

