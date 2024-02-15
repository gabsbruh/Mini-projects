import tkinter as tk
from tkinter import messagebox
import random

# ---------------------------- CONSTANTS ------------------------------- #
FONT = ("Courier", 10, "normal")
DEFAULT_EMAIL = 'mostcommon@email.com'

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pwd():
    """ Attachable to a button. Generate new password for user consist of random letters, numbers
    and special characters. 8 - 32 chars.
    """
    pass

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pwd():
    """Function attachable to the button. Designed for saving password to a file with all pasword which program is holding
    """
    web_getter = website_entry.get()
    email_getter = email_entry.get()
    password_getter = password_entry.get()
    
    # validate if textboxes are not empty
    if len(web_getter) == 0 or len(email_getter) == 0 or len(password_getter) == 0:
        messagebox.showinfo(title="Blank rows", message="Don't leave textboxes empty!")
    
    else:  
        # concatenate data got to one row and make sure is it ok
        output = "  |  ".join([web_getter, email_getter, password_getter])
        
        # let the user validate entry in the pop-up
        is_ok = messagebox.askokcancel(title='data file', 
                            message=f'Text below:\n{output}\nwill be saved to a data file. Proceed?')
        if is_ok:    
            # save data to file
            with open('data.txt', 'a') as data:
                data.write(output + '\n')

# ---------------------------- UI SETUP ------------------------------- #

# main window
window = tk.Tk()
window.config(padx=20, pady=20)
window.title("Password Manager")

# canvas widget to hold the logo
canvas = tk.Canvas(width=200, height=200)
logo = tk.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo) # first two vairables stands for place for the image
canvas.grid(column=1, row=0)

######### LABELS #########
website = tk.Label(text='Website: ', font=FONT)
website.grid(column=0, row=1)

username = tk.Label(text="Email/Username: ", font=FONT)
username.grid(column=0, row=2)

password = tk.Label(text='Password: ', font=FONT)
password.grid(column=0, row=3)

######### INPUTS #########
website_entry = tk.Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website.focus()

email_entry = tk.Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert('0', DEFAULT_EMAIL) # default email to write

password_entry = tk.Entry(width=21)
password_entry.grid(column=1, row=3)

######### BUTTONS #########
generate = tk.Button(text="Generate Password", command=generate_pwd)
generate.grid(column=2, row=3)

add = tk.Button(text='Add', command=add_pwd, width=36)
add.grid(column=1, row=4, columnspan=2)

# main loop of program
window.mainloop()