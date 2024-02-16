import tkinter as tk
from tkinter import messagebox
import random

# ---------------------------- CONSTANTS ------------------------------- #
FONT = ("Courier", 10, "normal")
DEFAULT_EMAIL = 'mostcommon@email.com'

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pwd():
    """ Attachable to a button. Generate new password for user consist of random letters, numbers
    and special characters. 12 - 24 chars.
    """
    def pwd_generator():
        password_entry_prob = []   
        for char in range(1, random.randint(2, 22)): # leave 2 min. places for number and special character
            password_entry_prob.append(random.choice(letters))
        for char in range(1, random.randint(2, 23-len(password_entry_prob))):
            password_entry_prob.append(random.choice(numbers))    
        for char in range(1, random.randint(2, 24-len(password_entry_prob))):
            password_entry_prob.append(random.choice(symbols)) 
        return password_entry_prob  
    
    # lists of all characters avaiable
    # alphabet letters, lower and upper case
    letters = ranged_letters = [chr(letter) for letter in range(ord('a'),ord('z') + 1)] + [
                                chr(letter) for letter in range(ord('A'),ord('Z') + 1)] 
    numbers = [str(i) for i in range(0,10)]
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    # choose random chars from lists. password is up to 24 chars
    generated_password = pwd_generator()
    while len(generated_password) <= 12:
        generated_password = pwd_generator()
    
    # making the password chars order mixed (abandon the order letters, sumbols, numbers)
    random.shuffle(generated_password)
    
    # concatenates the whole list of chars in password
    password_entry.delete('0', tk.END)
    password_entry.insert('0', "".join(generated_password))

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
        is_ok = messagebox.askokcancel(title='Data validation', 
                                       message=f"""
    Data below:\n
Website:    {web_getter}\n
Username: {email_getter}\n
Password:  {password_getter}\n
    Will be saved to a data file. Proceed?
""")
        
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

password_entry = tk.Entry(width=35)
password_entry.grid(column=1, row=3, columnspan=2)

######### BUTTONS #########
generate = tk.Button(text="Generate", command=generate_pwd)
generate.grid(column=3, row=3)

add = tk.Button(text='Add', command=add_pwd, width=33, border=3)
add.grid(column=1, row=5, columnspan=2, pady=20)

# main loop of program
window.mainloop()