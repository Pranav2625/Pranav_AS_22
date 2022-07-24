from tkinter import *
from functools import partial

root = Tk()
root.title("Home")

home_frame = Frame(root, width=600, height=600, bg="maroon")
home_frame.grid()

home_header = Label(home_frame, text="Blackjack", font=("Times 16 bold"),
                    bg="gold", padx=270, pady=10, justify=CENTER)
home_header.place(x=-10, y=0)



def Single_Username():
    sngle_usrnme_win = Toplevel(root)

    sngle_but.config(state=DISABLED)

    def close_sngle_usrnme():  # If either the back button or window is closed
        sngle_but.config(state=NORMAL)  # revert the single player button back to normal
        sngle_usrnme_win.destroy()
    sngle_usrnme_win.protocol("WM_DELETE_WINDOW", partial(close_sngle_usrnme))

    sngle_usrnme_frame = Frame(sngle_usrnme_win, width=600, height=600, bg="maroon")
    sngle_usrnme_frame.grid()

    sngle_usrnme_header = Label(sngle_usrnme_frame, text="Enter in a username", font="arial 14 bold", justify=CENTER,
                              width=40, bg="orange", wrap=250)
    sngle_usrnme_header.grid(row=0)

    def prnt_sngle_usrnme():  # Carries out defintion if confirm is pushed
        sngle_username = sngle_usrnme_entry_box.get()  # Stores the input text from the entry field in this variable as string
        print("Hello", sngle_username)  # and prints it out

    sngle_usrnme_entry_box = Entry(sngle_usrnme_frame, width=20, font="arial 14")  # Creates the entry box
    sngle_usrnme_entry_box.grid(row=2, pady=10)

    sngle_usrnme_confirm = Button(sngle_usrnme_frame, text="Confirm", bg="gold", font="arial 10 bold",
                                  # Creates
                                  command=prnt_sngle_usrnme)  # confirm button
    sngle_usrnme_confirm.grid(row=4, pady=10)

    sngle_usrnme_back = Button(sngle_usrnme_frame, text="Back", width=10, bg="orange",  # Creates back button
                               font="arial 10 bold", command=partial(close_sngle_usrnme))
    sngle_usrnme_back.grid(row=6, pady=10)

sngle_but = Button(home_frame, text="Single-player", font="arial 10 bold", bd=1, command=Single_Username)
sngle_but.place(x=250, y=150)



def Double_Username():
    dble_usrnme_win = Toplevel(root)

    dble_but.config(state=DISABLED)

    def close_dble_usrnme():  # If either the back button or window is closed
        dble_but.config(state=NORMAL)  # revert the single player button back to normal
        dble_usrnme_win.destroy()
    dble_usrnme_win.protocol("WM_DELETE_WINDOW", partial(close_dble_usrnme))

    dble_usrnme_frame = Frame(dble_usrnme_win, width=600, height=600, bg="maroon")
    dble_usrnme_frame.grid()

    dble_usrnme_header = Label(dble_usrnme_frame, text="Enter in two usernames", font="Times 14 bold",
                               justify=CENTER, bg="gold", padx=270, pady=10)
    dble_usrnme_header.place(x=-40, y=0)

    def prnt_dble_usrnme():  # When confirmed is pushed...
        dble_username1 = dble_usrnme_entry_box1.get()  # Store the usr input in
        dble_username2 = dble_usrnme_entry_box2.get()  # these two variables
        print("Hello", dble_username1, "&", dble_username2)  # and print this statement in the terminal

    dble_usrnme_entry_box1 = Entry(dble_usrnme_frame, width=20, font="arial 12")  # Make two
    dble_usrnme_entry_box1.place(x=230, y=100)  # entry
    dble_usrnme_entry_box2 = Entry(dble_usrnme_frame, width=20, font="arial 12")  # boxes
    dble_usrnme_entry_box2.place(x=230, y=150)

    dble_usrnme_confirm = Button(dble_usrnme_frame, text="Confirm", bg="gold",  # Confirm button for
                                      font="arial 10 bold", command=prnt_dble_usrnme)  # username input
    dble_usrnme_confirm.place(x=265, y=200)

    dble_usrnme_back = Button(dble_usrnme_frame, text="Back", bg="orange",  # Creates back button
                               font="arial 10 bold", command=partial(close_dble_usrnme))
    dble_usrnme_back.place(x=270, y=230)


dble_but = Button(home_frame, text="Two Players", font="arial 10 bold", bd=1, command=Double_Username)
dble_but.place(x=252, y=200)



def Triple_Username():
    trpe_usrnme_win = Toplevel(root)

    trpe_but.config(state=DISABLED)

    def close_trpe_usrnme():
        trpe_but.config(state=NORMAL)
        trpe_usrnme_win.destroy()

    trpe_usrnme_win.protocol("WM_DELETE_WINDOW", partial(close_trpe_usrnme))

    trpe_usrnme_frame = Frame(trpe_usrnme_win, width=600, height=600, bg="maroon")
    trpe_usrnme_frame.grid()

    trpe_usrnme_header = Label(trpe_usrnme_frame, text="Enter in three usernames", font="Times 14 bold",
                               bg="gold", padx=270, pady=10)
    trpe_usrnme_header.place(x=-50, y=0)

    def prnt_trp_usrnme():  # When the inputs are confirmed using buttons
        trp_username1 = trp_usrnme_entry_box1.get()  # store these inputs as string variables
        trp_username2 = trp_usrnme_entry_box2.get()
        trp_username3 = trp_usrnme_entry_box3.get()
        print("Hello", trp_username1, ",", trp_username2, ", &", trp_username3)  # Print them in a statement

    trp_usrnme_entry_box1 = Entry(trpe_usrnme_frame, width=20, font="arial 12")  # Entry boxes for the window
    trp_usrnme_entry_box1.place(x=230, y=100)
    trp_usrnme_entry_box2 = Entry(trpe_usrnme_frame, width=20, font="arial 12")
    trp_usrnme_entry_box2.place(x=230, y=150)
    trp_usrnme_entry_box3 = Entry(trpe_usrnme_frame, width=20, font="arial 12")
    trp_usrnme_entry_box3.place(x=230, y=200)

    trpe_usrnme_confirm = Button(trpe_usrnme_frame, text="Confirm", bg="gold",  # Confirm button
                                     font="arial 10 bold", command=prnt_trp_usrnme)
    trpe_usrnme_confirm.place(x=265, y=250)

    trpe_usrnme_back = Button(trpe_usrnme_frame, text="Back", bg="orange",  # Back button
                                  font="arial 10 bold",
                                  command=partial(close_trpe_usrnme))
    trpe_usrnme_back.place(x=270, y=280)

trpe_but = Button(home_frame, text="Three Players", font="arial 10 bold", bd=1, command=Triple_Username)
trpe_but.place(x=248, y=250)

root.mainloop()