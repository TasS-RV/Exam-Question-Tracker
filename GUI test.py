import tkinter as tk
from tkinter import messagebox
from tkinter import Toplevel



    

def perform_operation():

  def terminate_all():
    check_window.destroy()
    window.destroy()



  # Get the user input from the text box
  user_input = text_box.get()

  # Apply the operation to the user input
  result = int(user_input) * 2

  # Display the result in a pop-up
  #messagebox.showinfo("Result",f"The result is {result}. Do you want to continue?")
  #check_window = tk.Tk()
  
  check_window = Toplevel()

  outcome = tk.Label(check_window, text = f"The result is {result}. Do you want to continue?")
  outcome.pack()
  button1 = tk.Button(check_window, text="Yes", command=check_window.destroy)
  button1.pack()
  button2 = tk.Button(check_window, text="No", command=terminate_all)
  button2.pack()
  check_window.mainloop()

# Create the main window
window = tk.Tk()

messagebox.showinfo("How to use Program","This is used to keep track of completed papers and questions from Tripos.\nEnter in the format of P1-18-Q3, which represents Question 3 of 2018 Paper 1.\nTo check if a full paper is complete, omit the '-Q3'.")

# Add a label to prompt the user for input
label = tk.Label(window, text="Please input details of paper and question:")
label.pack(side = "top")

# Add a text box for user input
text_box = tk.Entry(window)
text_box.pack()

parentwin = window
# Add a button to trigger the operation
button = tk.Button(window, text="Calculate", command=perform_operation)
button.pack(side = "bottom")

# Run the main loop
window.mainloop()