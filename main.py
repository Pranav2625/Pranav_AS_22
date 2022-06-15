from tkinter import *
from functools import partial  # To prevent unwanted windows
 # import random


class Main_screen:
  def __init__(self, parent):

    # Formatting variables:

    # Main Screen GUI:
    self.main_frame = Frame(width = 600, height = 600, bg = "maroon",  # Both these lines are the features of 
                            pady = 10)                                 # the main window frame
    self.main_frame.grid()

    # Home Screen Heading:
    self.home_scrn_label = Label(self.main_frame, text = "Blackjack",    # Makes the title heading for the window
                                font = ("Italic", "16", "bold"),         # using a specfic font
                                bg = "gold", padx = 200, pady = 10)      # and a label colour
    self.home_scrn_label.grid(row = 0)                                   # and applies it to the interface's grid

    # Single Player button:
    self.sngle_button = Button(self.main_frame, text = "Single Player",  # Creates a button for
                              padx = 10, pady = 10, command = self.single_username)                      # Single player mode
    self.sngle_button.grid(row = 1, pady = 10)                                      # and puts it onto the grid

    # # Multiplayer Drop-down:
    def two_or_three():
      if variable.get() == "2 Players":                      # If 2 players selected
        two_play()                                           # goto two_play()
      if variable.get() == "3 Players":                      # If 3 players selected
        three_play()                                         # goto three_play()
    variable = StringVar(root)
    variable.set("Multiplayer")
    self.mult_drop = OptionMenu(self.main_frame, variable, "2 Players", "3 Players")     # Create the menu and it's options
    self.mult_drop.grid(row = 2, pady = 5)                                                         # and put it on the grid

    self.confirm_mult = Button(self.main_frame, text = "Confirm", command = two_or_three)  # Create the confirm button
    self.confirm_mult.grid(row = 3, pady = 2)                                                        

    def two_play():
      print("two players")

    def three_play():
      print("Three players")

  def single_username(self):
    get_sngle_usernme = Single_Username(self)
    get_sngle_usernme.sngle_usernme_text.configure(text = "Enter in a username")

class Single_Username:
  def __init__(self, partner):

    partner.sngle_button.config(state = DISABLED) # Disables the confirm button when 
                                                 # while this window is open
    
    self.sngle_usrnme_win = Toplevel() # Sets up the window

    self.sngle_usrnme_win.protocol("WM_DELETE_WINDOW", partial(self.close_sngle_usr, partner)) # Releases confirm button 
                                                                                               # when window closed
    
    self.sngle_usr_frame = Frame(self.sngle_usrnme_win, width = 600, height = 600, bg = "maroon")  # Makes the frame for this window
    self.sngle_usr_frame.grid()

    self.sngle_usernme_text = Label(self.sngle_usr_frame, text = "", font = "arial 14 bold", justify = CENTER, 
                                    width = 40, bg = "orange", wrap = 250)
    self.sngle_usernme_text.grid(row = 0)

    def prnt_sngle_usr():
      sngle_username = self.sngle_usr_entry_box.get()
      print("Hello", sngle_username)
    
    self.sngle_usr_entry_box = Entry(self.sngle_usr_frame, width = 20, font = "arial 14")
    self.sngle_usr_entry_box.grid(row = 2, pady = 10)

    self.sngle_usr_confirm = Button(self.sngle_usr_frame, text = "Confirm", bg = "gold", font = "arial 10 bold",
                                   command = prnt_sngle_usr)
    self.sngle_usr_confirm.grid(row = 4, pady = 10)
    
    self.sngle_usr_back = Button(self.sngle_usr_frame, text = "Back", width = 10, bg = "orange", 
                                 font = "arial 10 bold", command = partial(self.close_sngle_usr, partner))
    self.sngle_usr_back.grid(row = 6, pady = 10)

  def close_sngle_usr(self, partner):
    partner.sngle_button.config(state = NORMAL)
    self.sngle_usrnme_win.destroy()



    
# main routine:
if __name__ == "__main__":
  root = Tk()
  root.title("Blackjack Home Screen")  # Name of the windows
  something = Main_screen(root)
  root.mainloop()