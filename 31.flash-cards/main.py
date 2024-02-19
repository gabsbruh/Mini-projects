import pandas as pd
import random
import tkinter as tk
from RangeSlider import RangeSliderV

########## CONSTANTS ##########
BACKGROUND_COLOR = "#B1DDC6"
CHECKMARK_COLOR = "#416D19"
WRONG_COLOR = "#A94438"
FONT_LANGUAGE = ("Ariel", 30, "italic")
FONT_WORD = ("Ariel", 50, "bold")
FONT_CHANGE = ("Ariel", 15, "bold")
FONT_COUNTER = ("Arial", 30, "bold")
learn_language = 'English' # language user want to learn
know_language = 'Polish' # known language
level = [1, 10] # db are divided from most common words to least.
                # each level is 5k words, 1lvl 5k most common, 10lvl less. defines a section between
TIME_FLIP = 4000 # in ms
right_counter = 0 # counting right anwers
wrong_counter = 0 # counting wrong answers

########## COMMANDS FOR UI ##########
def flip_card():
    global word_learn, word_known
    canvas_card.itemconfig(bg_card, image=front_img)    
    canvas_card.itemconfig(word_canvas_card, text=word_known)
    canvas_card.itemconfig(language_canvas_card, text=know_language)
    
def when_button():
    """Funciton defines what happens after user clicks one of the buttons
    """
    global word_learn, word_known, flipper
    root.after_cancel(flipper)
    word_learn, word_known = find_words()
    canvas_card.itemconfig(bg_card, image=back_img)
    canvas_card.itemconfig(language_canvas_card, text=learn_language)
    canvas_card.itemconfig(word_canvas_card, text=word_learn)
    flipper = root.after(TIME_FLIP, flip_card)
    
def when_button_yes():
    """Funtion to add to the button. Checkmark 'yes' button increments right_counter,
    and turn on when_button funtion.
    """
    global right_counter
    right_counter += 1
    good_answers.config(text=right_counter)
    when_button()

def when_button_no():
    """Funtion to add to the button. Checkmark 'no' button increments wrong_counter,
    and turn on when_button funtion.
    """
    global wrong_counter
    wrong_counter += 1
    bad_answers.config(text=wrong_counter)
    when_button()

def learn_radio_used():
    """function triggers when language to learn has changed.
    """
    global learn_language
    if learn_store.get() == 1:
        learn_language = "English"
    elif learn_store.get() == 2:
        learn_language = "Polish"
    elif learn_store.get() == 3:
        learn_language = "Spanish"

def know_radio_used():
    """function triggers when language which is known has changed.
    """
    global know_language
    if know_store.get() == 1:
        know_language = "Polish"
    elif know_store.get() == 2:
        know_language = "English"
    elif know_store.get() == 3:
        know_language = "Spanish"

def change_min_level(*args):
    """Change minimum of variable 'level'
    """
    global level
    level[0] = int(level_min_sl.get())

def change_max_level(*args):
    """Change maximum of variable 'level'
    """
    global level
    level[1] = int(level_max_sl.get())


########## DB ACCESS ##########
database = pd.read_csv('data\words_db.csv')

def find_words():
    """Function looks for random word and its translation in dataframe

    Args:
        level_min (int, optional): minimum of level of words between(1,10).
                                   Can't be greater than level_max. Defaults to 1.
        level_max (int, optional): maximum level of words between(1,10). Defaults to 10.
    
    Returns:
        Tuple(string, string): Words from database, random words and its translation
    """
    global learn_language, know_language, level
    level_min = level[0]
    level_max = level[1]
    # catching inappropriate input arguments
    if level_min > level_max:
        raise ValueError("Argument 'level_min' can't be greater than 'level_max'")
    if not 1 <= level_min <= 10:
        raise ValueError("Argument 'level_min' needs to be an intiger between 1 and 10.")
    if not 1 <= level_max <= 10:
        raise ValueError("Argument 'level_max' needs to be an intiger between 1 and 10.")
    if learn_language not in database.columns.to_list():
        raise ValueError("Wrong 'learn' language input.")
    if know_language not in database.columns.to_list():
        raise ValueError("Wrong 'know' language input.")
    
    # setup range based on level
    nrow = database.shape[0]
    level_divide = int(nrow/10) # divide database onto 10 levels
    min_word = (level_min-1)*level_divide + 1 # min index of row
    max_word = level_max*level_divide # max index of row
    
    # take random index of number
    index = random.randint(min_word, max_word) 
    return database.loc[index, learn_language], database.loc[index, know_language]


########## UI SETUP ##########
# WINDOW
root = tk.Tk()
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
root.title('Flash Cards')

# CANVAS
word_learn, word_known = find_words() # find first words which initializes the text on canvas
# card config
canvas_card = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = tk.PhotoImage(file='images/card_front.png')
back_img = tk.PhotoImage(file='images/card_back.png')
bg_card = canvas_card.create_image(400, 263, image=back_img)
language_canvas_card = canvas_card.create_text(400, 150, text=learn_language, font=FONT_LANGUAGE)
word_canvas_card = canvas_card.create_text(400, 263, text=word_learn, font=FONT_WORD)
canvas_card.grid(column=1, row=2, columnspan=8, rowspan=2)

# initialize lfipper which tracks button clicks
flipper = root.after(TIME_FLIP, flip_card)

# BUTTONS
# no button
no_img = tk.PhotoImage(file='images/wrong.png')
no = tk.Button(image=no_img, command=when_button_no, highlightthickness=0)
no.grid(column=2, row=4, columnspan=2)

# skip button
skip_img = tk.PhotoImage(file='images/skip.png')
skip_img = skip_img.subsample(5,5)
skip = tk.Button(image=skip_img, command=when_button, highlightthickness=0,
                 bg=BACKGROUND_COLOR)
skip.grid(column=4, row=4, columnspan=2)

# yes button
yes_img = tk.PhotoImage(file="images/right.png")
yes = tk.Button(image=yes_img, command=when_button_yes, highlightthickness=0)
yes.grid(column=6, row=4, columnspan=2)

# RADIOBUTTONS
english_img = tk.PhotoImage(file="images/united.png")
english_img = english_img.subsample(3,3)
polish_img = tk.PhotoImage(file="images/poland.png")
polish_img = polish_img.subsample(3,3)
spanish_img = tk.PhotoImage(file="images/spain.png")
spanish_img = spanish_img.subsample(3,3)

# learn radiobuttons
learn_store = tk.IntVar()

english_rb_learn = tk.Radiobutton(image=english_img, bg=BACKGROUND_COLOR, 
                                  variable=learn_store, value=1, command=learn_radio_used)
english_rb_learn.grid(column=2, row=1)
polish_rb_learn = tk.Radiobutton(image=polish_img, bg=BACKGROUND_COLOR, 
                                  variable=learn_store, value=2, command=learn_radio_used)
polish_rb_learn.grid(column=3, row=1)
spanish_rb_learn = tk.Radiobutton(image=spanish_img, bg=BACKGROUND_COLOR, 
                                  variable=learn_store, value=3, command=learn_radio_used)
spanish_rb_learn.grid(column=4, row=1)

# know radiobuttons
know_store = tk.IntVar()
english_rb_know = tk.Radiobutton(image=english_img, bg=BACKGROUND_COLOR, 
                                  variable=know_store, value=2, command=know_radio_used)
english_rb_know.grid(column=6, row=1)
polish_rb_know = tk.Radiobutton(image=polish_img, bg=BACKGROUND_COLOR, 
                                  variable=know_store, value=1, command=know_radio_used)
polish_rb_know.grid(column=7, row=1)
spanish_rb_know = tk.Radiobutton(image=spanish_img, bg=BACKGROUND_COLOR, 
                                  variable=know_store, value=3, command=know_radio_used)
spanish_rb_know.grid(column=8, row=1)

# LABELS
# change leanguage labels
learn_label = tk.Label(text='Learn: ', font=FONT_CHANGE, bg=BACKGROUND_COLOR)
learn_label.grid(column=1, row=1)
learn_label = tk.Label(text='Know: ', font=FONT_CHANGE, bg=BACKGROUND_COLOR)
learn_label.grid(column=5, row=1)

# change level labels
level_label = tk.Label(text='Level: ', font=FONT_CHANGE, bg=BACKGROUND_COLOR)
level_label.grid(column=9, row=2)

# counter for good and bad
good_answers = tk.Label(text='0', font=FONT_COUNTER,
                         bg=BACKGROUND_COLOR, fg=CHECKMARK_COLOR)
good_answers.grid(column=8, row=4)

bad_answers = tk.Label(text='0', font=FONT_COUNTER,
                         bg=BACKGROUND_COLOR, fg=WRONG_COLOR)
bad_answers.grid(column=1, row=4)

# RANGE SLIDER
level_min_sl = tk.IntVar(value=1)
level_max_sl = tk.IntVar(value=4)
slider = RangeSliderV(root, [level_min_sl, level_max_sl], min_val=1, max_val=10,
                      bgColor=BACKGROUND_COLOR, font_family='Ariel', padY=12,
                      digit_precision='.0f') 
slider.grid(column=9, row=3)

# trace values of slider
level_min_sl.trace('w', change_min_level)
level_max_sl.trace('w', change_max_level)


# mainloop
tk.mainloop()