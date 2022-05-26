from tkinter import *
from functools import partial  # To prevent unwanted windows
 # import random


class Converter:
  def __init__(self, parent):

    # Formatting variables:

    # Main Screen GUI:
    self.main_frame = Frame(width = 500, height = 500, bg = "maroon", 
                            pady = 10)
    self.main_frame.grid()




# main routine:
if __name__ == "__main__":
  root = Tk()
  root.title("Blackjack Home Screen")
  something = Converter(root)
  root.mainloop()