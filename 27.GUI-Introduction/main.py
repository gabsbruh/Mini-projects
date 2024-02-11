from tkinter import *

def calculate(var, mode):
    """main conversion function

    Args:
        var (float): variable to be converted
        mode (boolean): type of conversion(miles to km is True, inverted False)

    Returns:
        float: converted variable to another unit
    """
    if mode == True:
        return round(1.60934*var, 3)
    elif mode == False:
        return round(var/1.60934, 3)
    
def main():

    # initializing
    window = Tk()
    window.title('Miles to km converter')
    window.minsize(400,100)

    # input to calculate
    input_ = Entry(width=10, font=('arial', 12))
    input_.grid(column=2, row=1)
    
    #labels
    label1 = Label(text='Kilometers: ', width=20)
    label2 = Label(text='Miles: ', width=20)
    label1.grid(column=1, row=1)
    label2.grid(column=1, row=2)
    
    # switch logic
    def toggle():
        if switch.config('text')[-1] == 'km to miles':
            switch.config(text='miles to km')
            label1.grid(column=1, row=1) # changes text next to input
            label2.grid(column=1, row=2)
        else:
            switch.config(text='km to miles')    
            label1.grid(column=1, row=2)
            label2.grid(column=1, row=1)
    
    switch = Button(window, text='km to miles', width=12, command=toggle)
    switch.grid(column=3, row=2, padx=30)
    
    # output config
    output_ = Text(window, width=12, height=1, font=('arial', 12))
    output_.grid(column=2, row=2)
    output_.focus() # can click on text and toggle between string
    output_["state"] = 'disabled' # unable writing to the output
    
    def calculate_wrap():
        """Wrapper to the calculate() function which initializes it, gather arguments
        for it. Additionally it configurates the output to display the output. This wrapper
        can be passed to the Button init so existence of this fun is significant.
        """
        var = float(input_.get())
        mode = True if switch.config('text')[-1] == 'km to miles' else False
        output = calculate(var, mode)
        output_["state"] = 'normal' # turn on writing to the output
        output_.delete('1.0', 'end') # delete previous content of text box
        output_.insert('1.0', str(output))  
        output_["state"] = 'disabled'
    
    # button which activates converter
    calc = Button(window, text="CALCULATE", width=15, command=calculate_wrap)
    calc.grid(column=3, row=3, pady=30)
    
    # remain loop of app
    window.mainloop()


if __name__ == '__main__':
    main()