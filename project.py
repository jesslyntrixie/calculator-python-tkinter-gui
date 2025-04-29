from tkinter import Tk, Entry, Button, StringVar

# Global variables
root = None
equation = None
entry_value = ''

def initialize_tkinter():
    global root, equation
    root = Tk()
    equation = StringVar()

def show(value):
    global entry_value
    entry_value += str(value)  # Convert value to string and append to entry_value
    equation.set(entry_value)
    
def clear():
    global entry_value
    entry_value = ''
    equation.set(entry_value)
    
def solve():
    global entry_value
    try:
        processed_value = entry_value.replace('%', '/100')
        processed_value = processed_value.replace('x', '*')
        result = eval(processed_value)  # Evaluate the expression in entry_value
        equation.set(result)
    except Exception as e:
        equation.set("Error")
        
def backspace():
    global entry_value
    
    #print("Backspace pressed") 
    #print(str(entry_value))
    entry_value = entry_value[:-1]
    print(entry_value)
    equation.set(entry_value)
    

def main():
    global root, equation
    
    # Initialize the main window
    initialize_tkinter()
    root.title("Calculator")
    root.geometry('308x527+0+0')
    root.config(bg='#8794BF')
    root.resizable(False, False)
    
    equation = StringVar()
    
    # Create Entry widget
    entry = Entry(root, width=20, bg='#3E3E5E', fg = 'white', font=('Arial Bold', 28), textvariable=equation)
    entry.place(x=24, y=20, width=260, height=73)

    # Buttons configuration
    buttons = [
        '(', ')', '%', '/',
        '7', '8', '9', 'x',
        '4', '5', '6', '-',
        '1', '2', '3', '+',
        '+/-', '0', '.', '='
    ]

    # Adjust button sizes and padding
    button_width = 65
    button_height = 65
    x_padding = 0
    y_padding = 0
    x0 = 24
    y0 = 170  # Start buttons below the input bar

    row = 0
    col = 0

    Button(root, text='C', width=5, height=2, font=('Arial', 18), command=clear,
                bg='#D1CFE2', activebackground='#B1AECB').place(
                x=154, y=105, width=button_width, height=button_height
            )
    Button(root, text = 'Bksp', width = 5, height = 2, font = ('Arial', 18),
                bg='#D1CFE2', activebackground='#B1AECB', 
                command=backspace).place(
                x=219, y=105, width=button_width, height=button_height
            )    
                
    for button in buttons:
        if button == '=':
            Button(root, text=button, width=5, height=2, font=('Arial', 18), command=solve,
                bg='#E27396', activebackground='#C25678').place(
                x=x0, y=y0, width=button_width, height=button_height
            )
        elif button == '+/-':
            Button(root, text=button, width=5, height=2, font=('Arial', 18),
                bg='#E27396', activebackground='#C25678', 
                command=lambda b='-': show(b)).place(
                x=x0, y=y0, width=button_width, height=button_height
            )
            
                
        elif button in ['+', '-', 'x', '/', '.', '(', ')', '%']:
            Button(root, text=button, width=5, height=2, font=('Arial', 18),
                bg='#E27396', activebackground='#C25678', 
                command=lambda b=button: show(b)).place(
                x=x0, y=y0, width=button_width, height=button_height
            )
        

        else:
            Button(root, text=button, width=5, height=2, font=('Arial', 18),
                command=lambda b=button: show(b),
                bg = '#FBFBFB', activebackground= '#E0E0E0'
                ).place(
                x=x0, y=y0, width=button_width, height=button_height
            )

        col += 1
        x0 += button_width + x_padding  # Add padding between buttons
        if col > 3:
            col = 0
            row += 1
            x0 = 24
            y0 += button_height + y_padding  # Add padding between rows

    
    # Run the main loop
    root.mainloop()
    
    
if __name__ == "__main__":
    main()   
    
    
