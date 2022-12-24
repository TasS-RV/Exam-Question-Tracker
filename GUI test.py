import tkinter as tk
from tkinter import messagebox
from tkinter import Toplevel
from time import sleep

def check_completion(user_in):
    try: 
        paper, year, question = user_in.split('-')
        checkstate = "Q"
    except ValueError: #If no question is specified, user intends to check completion of full paper
        try: 
            paper, year = user_in.split('-')
            checkstate = "P"
        except ValueError:
            messagebox.showerror("Input Error","Invalid input, please retry.")
    #Where it fails both cases, and prompts user to retry input.
    
    with open(f"./Completed/{paper}.txt", 'r') as record:
        completion_state = False #Toggles for run checking 1 paper, or 1 question from a paper

        if checkstate == "P":
            for line in record.readlines():

                if (year in line) and len(year) == len(line.strip()): #Prevents mistaken pick-uof papers with single, some questions complete
                    outcome = "You have completed {1} {0}.".format(paper, year) 
                    completion_state = True

            if completion_state == False: #After iterating through entire set
                    outcome = "{1} {0} is incomplete. Better crack on with Tripos questions buddy.".format(paper, year)
        
        elif checkstate == "Q":            
            for line in record.readlines():
                if "{0}-{1}".format(year, question) in line:
                    outcome = "You have completed {1} {0}, question {2}.".format(paper, year, question)
                    completion_state = True #Same as above, toggled if it finds the question in the list
                
            if completion_state == False: 
                    outcome = "This question has not been completed."
        
        else:
            outcome = "Invalid input. Program is unsure of details to check. Click 'Yes' and rerun."
            sleep(1) #Generating artifical delay for fun
    return outcome        


def read_files():
  
  #Terminates top level and base window if user is done checking completed questions.
  def terminate_all():
    check_window.destroy()
    window.destroy()


  # Get the user input from the text box
  user_input = text_box.get()
  outcome = check_completion(user_input)
  # Outcome after checking current researve of questions
  
  #Window overlay to return outcome of check
  check_window = Toplevel()

  out_label = tk.Label(check_window, text = "{}\n Check another paper or question?".format(outcome))
  out_label.pack()
  button1 = tk.Button(check_window, text="Yes", command=check_window.destroy)
  button1.pack()
  button2 = tk.Button(check_window, text="No", command=terminate_all)
  button2.pack()
  check_window.mainloop()


# Create the main window
window = tk.Tk()

#Instructions for use
messagebox.showinfo("How to use","This is used to keep track of completed papers and questions from Tripos.\nEnter in the format of P1-2018-Q3, which represents Question 3 of 2018 Paper 1.\nTo check if a full paper is complete, omit the '-Q3'.\n\nApply the same formatting when submitting questions to be written into the reserve, and it will update text files accordingly.")
sleep(1.5)

# Add a label to prompt the user for input
label = tk.Label(window, text="Please input details of paper and question:")
label.pack(side = "top")

# Add a text box for user input
text_box = tk.Entry(window)
text_box.pack()

parentwin = window
# Add a button to trigger the operation
button = tk.Button(window, text="Check", command=read_files)
button.pack(side = "bottom")

# Run the main loop
window.mainloop()
