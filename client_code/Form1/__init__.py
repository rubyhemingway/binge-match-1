#anvil template
from ._anvil_designer import Form1Template
from anvil import *
class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  #focus to search bar
  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.search_bar.focus()
    pass
  #search bar basic responses
  def search_bar_click(self, **event_args):
    pass

  def search_bar_pressed_enter(self, **event_args):
    query = self.search_bar.text.strip().lower()

  responses = {
    "happy": "Brooklyn Nine-Nine",
    "sad": "13 Reasons Why",
    "exciting": ["Wednesday", "Bridgerton"]

  }
result = responses.get(query, f"No recommendation for '{query}'")
self.output_label.text = result
"""This method is called when the user presses Enter in this text box"""
pass




