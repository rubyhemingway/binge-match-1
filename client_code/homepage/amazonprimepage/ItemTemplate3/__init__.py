from ._anvil_designer import ItemTemplate3Template
from anvil import *

class ItemTemplate3(ItemTemplate3Template):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.set_item(properties.get('item'))

  def set_item(self, item):
    self.item = item
    self.button_2.text = self.item['title']  # Set button text to the title

  def button_2_click(self, **event_args):
    """Open a form based on the title"""
    # this ensures the output of the titles will match any forms created after the fact which link to the repeating panel.
    title = self.item['title'].lower().replace(" ", "").replace("'", "")
    form_name = f"amazonprimepage.{title}"
    try:
      open_form(form_name)
    except Exception:
      alert(f"No form found for '{self.item['title']}'")

