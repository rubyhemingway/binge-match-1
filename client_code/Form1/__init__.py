from ._anvil_designer import Form1Template
from anvil import *


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
def outlined_button_1_click(self, **event_args):
  """This method is called when the button is clicked"""
  self.search_bar.focus()
  pass

def search_bar_pressed_enter(self, **event_args):
  """This method is called when the user presses Enter in this text box"""
  query = self.search_bar.text.strip().lower()
  responses = {
    "happy": {
      "title": "Brooklyn Nine-Nine",
      "poster": "https://upload.wikimedia.org/wikipedia/en/8/8a/Brooklyn_Nine-Nine_season_1_DVD_cover.jpg"
    },
    "sad": {
      "title": "13 Reasons Why",
      "poster": "https://upload.wikimedia.org/wikipedia/en/7/79/13_Reasons_Why_season_1.jpg"
    },
    "exciting": {
      "title": "Wednesday & Bridgerton",
      "poster": "https://upload.wikimedia.org/wikipedia/en/7/7e/Wednesday_Netflix_poster.jpg"
    }
  }
  #Google Colab in-class acitivities helped majorly with this portion
  result = responses.get(query)
  if result:
    self.output_label.text = result["title"]
    self.poster_image.source = result["poster"]
  else:
    self.output_label.text = f"No recommendation for '{query}'"
    self.poster_image.source = None