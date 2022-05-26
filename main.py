from tkinter import *
from functools import partial  # To prevent unwanted windows
 # import random


class Converter:
  def __init__(self, parent):

    # Formatting variables:

    # Main Screen GUI:
    self.main_frame = Frame(width = 600, height = 600, bg = "maroon", 
                            pady = 10)
    self.main_frame.grid()

    # Home Screen Heading:
    self.home_scrn_label = Label(self.main_frame, text = "Blackjack",
                                font = ("Italic", "16", "bold"),
                                bg = "gold", padx = 10, pady = 10)
    self.home_scrn_label.grid(row = 0, column = 0)

    # Single Player button:
    self.sngle_button = Button(self.main_frame, text = "Single Player",
                              padx = 10, pady = 10)
    self.sngle_button.grid(row = 1)

    # Multiplayer Button:
    self.multi_buttons = Button(self.main_frame, text = "MultiPlayer",
                                padx = 10, pady = 10)
    self.multi_buttons.grid(row = 2)



# main routine:
if __name__ == "__main__":
  root = Tk()
  root.title("Blackjack Home Screen")
  something = Converter(root)
  root.mainloop()