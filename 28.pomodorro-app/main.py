import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
STRONG_GREEN = "#789461"
RED = "#FF8080"
LIGHT_GREEN = "#CDFADB"
BLUE = "#7FC7D9"
YELLOW = "#F6FDC3"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = '✔'
timer = None
reps = 0
modulo_encounter = 1 # helps hadling with checkmarks reset
# ---------------------------- TIMER RESET ------------------------------- # 

# function to reset counter, for reset button
def on_reset():
    """ function callable on widget. Function resetting all variables which were changing
        during program was running to strating value.
    """
    # reps set back to 0
    global reps
    reps = 0
    
    # modulo_encounter back to 1
    global modulo_encounter
    modulo_encounter = 1
    
    # header restoration
    header.config(text="Timer")
    header.config(fg=RED)    
    
    # checkmarks cleared from the screen
    checkmark_text.config(text='')
    
    # canvas text config
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00 : 00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# function to start counter, for start button
def on_start():
    """ function callable on widget. Depending on wheter global reps variable 
        are odd or even, it starts counter for longer / shorter interval (work / break).
        When reps reaches 8, it starts a long break interval.
    """
    global reps
    reps += 1 # repetitions
    
    # conversion to seconds
    work_in_sec = WORK_MIN * 60
    short_in_sec = SHORT_BREAK_MIN * 60
    long_in_sec = LONG_BREAK_MIN * 60
  
    if reps % 8 == 0: # case when it comes to long break
        header.config(text="Long Break")
        header.config(fg=BLUE)
        track_time(long_in_sec)
        
    elif reps % 2 == 1: # time for work
        header.config(text="Work")  
        header.config(fg=RED)      
        track_time(work_in_sec)   
        
    elif reps % 2 == 0: # short time for a break between working intervals
        header.config(text="Break")
        header.config(fg=STRONG_GREEN)
        track_time(short_in_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# tracking time on canvas 
def track_time(count):
    # convert to a "00:00" format
    def conversion(count):
        minutes = int(count / 60) # holds value of remaining minutes
        seconds = int(count % 60) # holds value of remaining seconds
        return (f"{minutes:02d} : {seconds:02d}") # value to print
    
    canvas.itemconfig(timer_text, text=conversion(count)) # changes the text inside tomato
    if count > 0:
        global timer
        # count is -1 lower on each call of the function
        timer = window.after(1000, track_time, count-1) 
        
    # call new interval
    else:
        global modulo_encounter
        on_start()
        if reps % 2 == 0:
            checkmark_text.config(text=checkmark_text.cget("text") + CHECKMARK) 
        if reps == modulo_encounter*8 + 1:
            checkmark_text.config(text='')
            modulo_encounter += 1

# ---------------------------- UI SETUP ------------------------------- #

# main window config
window = tk.Tk()
window.title('Pomodorro')
window.config(padx=20, pady=10, bg=LIGHT_GREEN)

# import image with canvas widget
canvas = tk.Canvas(width=200, height=223, bg=LIGHT_GREEN, highlightthickness=0)
photo_image = tk.PhotoImage(file="tomato.png") # import image as an photoimage object
canvas.create_image(100, 112, image=photo_image) # create image with given position and

# photoimage object
canvas.grid(column=2, row=2) # specify layout of tomato and timer

# create text with timer in the centre of canvas's image
timer_text = canvas.create_text(102, 132, text="00 : 00", font=("Arial", 30, "bold"), fill='white')
    
# button to start counting
start = tk.Button(text='START', command=on_start, fg=RED, bg=YELLOW, 
                  font=("Arial", 12, "bold"), width=12, border=0, 
                  highlightthickness=0, padx=10, pady=10)
start.grid(column=1, row=3)

# button to start counting
reset = tk.Button(text='RESET', command=on_reset, fg=RED, bg=YELLOW, 
                  font=("Arial", 12, "bold"), width=12, border=0, 
                  highlightthickness=0, padx=10, pady=10)
reset.grid(column=3, row=3)

# text above the tomato
header = tk.Label(text='Timer', fg=RED, bg=LIGHT_GREEN, 
                  font=("Arial", 30, "bold"), pady=10)
header.grid(column=2, row=1)

# checkmarks to track completed intervals
checkmark_text = tk.Label(text='', bg=LIGHT_GREEN,
                          fg=STRONG_GREEN, font=("Arial", 20, "bold"))
checkmark_text.grid(column=2, row=4)

# mainloop of the window
window.mainloop()
