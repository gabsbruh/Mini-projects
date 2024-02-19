import pandas as pd
import tkinter as tk
import random

########## COMMANDS FOR UI ##########
def when_wrong():
    word_learn, word_known = find_words()
    # change the text on flash cards
    front_card.itemconfig(word_front_card, text=word_known) 
    

def when_right():
    word_learn, word_known = find_words()
    # change the text on flash cards
    front_card.itemconfig(word_front_card, text=word_known) 


########## CONSTANTS ##########
BACKGROUND_COLOR = "#B1DDC6"
FONT_LANGUAGE = ("Ariel", 30, "italic")
FONT_WORD = ("Ariel", 50, "bold")
LEARN_LANGUAGE = 'English' # language user want to learn
KNOW_LANGUAGE = 'Polish' # known language
level = [1, 10] # db are divided from most common words to least.
                # each level is 5k words, 1lvl 5k most common, 10lvl less. defines a section between


########## DB ACCESS ##########
database = pd.read_csv('data\words_db.csv')

def find_words(learn='English', know='Polish', level_min=1, level_max=4):
    """Function looks for random word and its translation in dataframe

    Args:
        learn (str, optional): language to learn. Defaults to 'English'.
        know (str, optional): language which user's know. Defaults to 'Polish'.
        level_min (int, optional): minimum of level of words between(1,10).
                                   Can't be greater than level_max. Defaults to 1.
        level_max (int, optional): maximum level of words between(1,10). Defaults to 10.
    
    Returns:
        Tuple(string, string): Words from database, random words and its translation
    """
    # catching inappropriate input arguments
    if level_min > level_max:
        raise ValueError("Argument 'level_min' can't be greater than 'level_max'")
    if not 1 <= level_min <= 10:
        raise ValueError("Argument 'level_min' needs to be an intiger between 1 and 10.")
    if not 1 <= level_max <= 10:
        raise ValueError("Argument 'level_max' needs to be an intiger between 1 and 10.")
    if learn not in database.columns.to_list():
        raise ValueError("Wrong 'learn' language input.")
    if know not in database.columns.to_list():
        raise ValueError("Wrong 'know' language input.")
    
    # setup range based on level
    nrow = database.shape[0]
    level_divide = int(nrow/10) # divide database onto 10 levels
    min_word = (level_min-1)*level_divide + 1 # min index of row
    max_word = level_max*level_divide # max index of row
    
    # take random index of number
    index = random.randint(min_word, max_word) 
    return database.loc[index, learn], database.loc[index, know]


########## UI SETUP ##########
# WINDOW
window = tk.Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title('Flash Cards')

# CANVAS
# front card config
front_card = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = tk.PhotoImage(file='images/card_front.png')
front_card.create_image(400, 263, image=front_img)
language_front_card = front_card.create_text(400, 150, text="Polish", font=FONT_LANGUAGE)
word_front_card = front_card.create_text(400, 263, text="word", font=FONT_WORD)
front_card.grid(column=1, row=1, columnspan=2)


# BUTTONS
# no button
no_img = tk.PhotoImage(file='images/wrong.png')
no = tk.Button(image=no_img, command=when_wrong, highlightthickness=0)
no.grid(column=1, row=2)

# yes button
yes_img = tk.PhotoImage(file="images/right.png")
yes = tk.Button(image=yes_img, command=when_right, highlightthickness=0)
yes.grid(column=2, row=2)

# mainloop
tk.mainloop()