from ._anvil_designer import theofficeTemplate
from anvil import *

class theoffice(theofficeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('homepage')

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('netflixpage')

  def outlined_button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('homepage.amazonprimepage')

  # allows the user to write a review which gets posted on the site so other users can see it.
  def reviewbox_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    user_input = self.review_boxtheoffice.text.strip()
    self.review_boxtheoffice.text = ""

    # this is the code for the label which appears under the review box when the user presses enter.
    # this code is for the label to be visible or not.
    # i used what I learnt when creating the search bar to help me write this code.
    # this is the same code needed for the 'happy feet' page.
    if user_input:
      self.outputlabel_2.text = user_input
      self.outputlabel_2.visible = True
    else:
      self.outputlabel_2.text = ""
      self.outputlabel_2.visible = False

  def outlined_button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.review_boxtheoffice.focus()
