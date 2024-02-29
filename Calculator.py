import tkinter as tk

calculation=""

def add_to_evaluate(sym):
    global calculation
    calculation+=sym
    text.delete(1.0,'end')
    text.insert(1.0,calculation)
    

def evaluate_calculation():
    global calculation
    try:
        text.delete(1.0,'end')
        calculation=str(eval(calculation))
        text.insert(1.0,calculation)
    except:
        text.delete(1.0,'end')
        calculation=''
        text.insert(1.0,'Error')
def clear_field():
    global calculation
    calculation=''
    text.delete(1.0,'end')

def create_round_button(canvas, x, y, radius, text, command, **kwargs):
    # Extracting color from kwargs if provided, otherwise defaulting to black
    color = kwargs.get('color', 'black')
    
    # Create the oval button with the specified color
    button = canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color, outline="#2a2a2a")
    text_id=canvas.create_text(x, y, text=text,font=("Arial", 20))
    if command.__code__.co_argcount == 0:  # Check if command doesn't accept any arguments
        canvas.tag_bind(button, "<Button-1>", lambda event: command())
        canvas.tag_bind(text_id, "<Button-1>", lambda event: command())
    else:  # If command accepts an argument
        canvas.tag_bind(button, "<Button-1>", lambda event: command(text))
        canvas.tag_bind(text_id, "<Button-1>", lambda event: command(text))

root = tk.Tk()
root.title("Calculator")
root.geometry("285x360")
root.resizable(False,False)

text=tk.Text(root,height=2,width=45,font=("Arial",20))
text.pack()

canvas = tk.Canvas(root, width=285, height=360)
canvas.pack()


create_round_button(canvas, 38, 30, 25, "C", clear_field,color="#5b5b5b")
create_round_button(canvas, 108, 30, 25, "(", add_to_evaluate,color="#5b5b5b")
create_round_button(canvas, 178, 30, 25, ")", add_to_evaluate,color="#5b5b5b")
create_round_button(canvas, 248, 30, 25, "/", add_to_evaluate,color = "#f2a33c")
create_round_button(canvas, 38, 90, 25, "7", add_to_evaluate,color="#5b5b5b")
create_round_button(canvas, 108, 90, 25, "8", add_to_evaluate,color="#5b5b5b")
create_round_button(canvas, 178, 90, 25, "9", add_to_evaluate,color="#5b5b5b")
create_round_button(canvas, 248, 90, 25, "*", add_to_evaluate,color = "#f2a33c")
create_round_button(canvas, 38, 150, 25, "4", add_to_evaluate,color="#5b5b5b")
create_round_button(canvas, 108, 150, 25, "5", add_to_evaluate,color="#5b5b5b")
create_round_button(canvas, 178, 150, 25, "6", add_to_evaluate,color="#5b5b5b")
create_round_button(canvas, 248, 150, 25, "−", add_to_evaluate,color = "#f2a33c")
create_round_button(canvas, 38, 210, 25, "1", add_to_evaluate,color="#5b5b5b")
create_round_button(canvas, 108, 210, 25, "2", add_to_evaluate,color="#5b5b5b")
create_round_button(canvas, 178, 210, 25, "3", add_to_evaluate,color="#5b5b5b")
create_round_button(canvas, 248, 210, 25, "+", add_to_evaluate,color = "#f2a33c")
create_round_button(canvas, 38, 270, 25, "00", add_to_evaluate,color="#5b5b5b")
create_round_button(canvas, 108, 270, 25, "0", add_to_evaluate,color="#5b5b5b")
create_round_button(canvas, 178, 270, 25, ".", add_to_evaluate,color="#5b5b5b")
create_round_button(canvas, 248, 270, 25, "=", evaluate_calculation,color = "#f2a33c")

root.mainloop()
