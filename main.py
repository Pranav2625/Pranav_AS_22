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
                                bg = "gold", padx = 200, pady = 10)
    self.home_scrn_label.grid(row = 0)

    # Single Player button:
    self.sngle_button = Button(self.main_frame, text = "Single Player",
                              padx = 10, pady = 10)
    self.sngle_button.grid(row = 1)

    # Multiplayer Button:
    self.multi_buttons = Button(self.main_frame, text = "MultiPlayer",
                                padx = 10, pady = 10)
    self.multi_buttons.grid(row = 2)

    # # Multiplayer Drop-down:
    def two_or_three():
      if variable.get() == "2 Players":
        two_play()
      if variable.get() == "3 Players":
        three_play()
    variable = StringVar(root)
    variable.set("Multiplayer")
    self.mult_drop = OptionMenu(root, variable, "2 Players", "3 Players")
    self.mult_drop.grid(row = 2)

    self.confirm_mult = Button(root, text = "Confirm", command = two_or_three)
    self.confirm_mult.grid(row = 3)

    def two_play():
      print("two players")

    def three_play():
      print("Three players")



# main routine:
if __name__ == "__main__":
  root = Tk()
  root.title("Blackjack Home Screen")
  something = Converter(root)
  root.mainloop()