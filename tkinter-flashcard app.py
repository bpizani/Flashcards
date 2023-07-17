from tkinter import *
from random import randint

root = Tk()
root.title("Flashcard App!")
root.geometry("400x400")
root.iconbitmap('iambob.ico')
#Create the addition function
def add():
    hide_menu_frame()
    add_frame.pack(fill="both", expand=1)

    #Create 2 random numbers
    global num_1
    global num_2
    num_1 = IntVar()
    num_2 = IntVar()
    num_1.set(randint(0,10))
    num_2.set(randint(0,10))

    #Create function to determine add answer correct
    def add_correct(num1, num2):
        # calculate the actual answer
        correct = num1 + num2

        #correct and incorrect message
        output_answer_correct = StringVar()
        output_answer_incorrect = StringVar()
        output_answer_correct.set("Correct")
        output_answer_incorrect.set("Incorrect")

        if int(add_answer.get()) == correct:
            add_correct_label.config(text=output_answer_correct.get())
        else:
            add_correct_label.config(text=output_answer_incorrect.get())

    #put our random number onto the screen
    add_flash = Label(add_frame, text=str(num_1.get()) + " + " + str(num_2.get()), font=("Arial", 32))
    add_flash.pack(pady=10)

    #Answer Box
    add_answer = Entry(add_frame)
    add_answer.pack(pady=5)

    #Answer Button
    add_button = Button(add_frame, text="Answer", command=lambda: add_correct(num_1.get(), num_2.get()))
    add_button.pack(pady=5)

    #Correct or Incorrect Message
    global add_correct_label
    add_correct_label = Label(add_frame, text="Enter your Answer Above")
    add_correct_label.pack(pady=5)


#Create the subtract function
def subtract():
    hide_menu_frame()
    subtract_frame.pack(fill="both", expand=1)

#Create the multiply function
def multiply():
    hide_menu_frame()
    multiply_frame.pack(fill="both", expand=1)

#Create the divide function
def divide():
    hide_menu_frame()
    divide_frame.pack(fill="both", expand=1)

#Hide Frame Function

def hide_menu_frame():
    add_frame.pack_forget()
    subtract_frame.pack_forget()
    multiply_frame.pack_forget()
    divide_frame.pack_forget()

#Define Main Menu
my_menu = Menu(root)
root.config(menu=my_menu)

#define the Main Menu
math_menu = Menu(root)
my_menu.add_cascade(label="Mathcards", menu=math_menu)
math_menu.add_command(label="Add", command=add)
math_menu.add_command(label="Subtract", command=subtract)
math_menu.add_command(label="Multiply", command=multiply)
math_menu.add_command(label="Divide", command=divide)
math_menu.add_separator()
math_menu.add_command(label="Exit", command=root.quit)

#Create Math Frames
add_frame = Frame(root, width=400, height=400)
subtract_frame = Frame(root, width=400, height=400)
multiply_frame = Frame(root, width=400, height=400)
divide_frame = Frame(root, width=400, height=400)

root.mainloop()
