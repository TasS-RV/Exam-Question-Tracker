import tkinter as tk
from tkinter import messagebox
from tkinter import Toplevel
import re, os
from time import sleep


def write_into_reserve(input_info, checkstate = "Q"):
    for direc, subdirec, files in os.walk("{}/Completed/".format(os.getcwd())):
        if checkstate == "P":
            paper, remainder = input_info.split('-') #Filenames as per paper
        elif checkstate == "Q":
            paper, year, question = input_info.split('-')
            remainder = year+"-"+question

        if f"{paper}.txt" not in files:
            #Anytime a questions from a paper not previously attempted is sunmitted, it must generate the file first
            with open(f"./Completed/{paper}.txt", 'w') as file_writer:
                file_writer.write(f"{remainder}\n")
        
        elif f"{paper}.txt" in files: 
            #If questions from this paper were previously attempted - 'append' mode, to prevent record of previous questions beig overwritten
            with open(f"./Completed/{paper}.txt", 'a') as file_writer:
                file_writer.write(f"{remainder}\n")
    
    confirmation_window = Toplevel()
    lab = tk.Label(confirmation_window, text = "Question Banks updated!")
    lab.pack()
    confirmation_window.after(1000, confirmation_window.destroy)
    confirmation_window.mainloop()



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


def write_files():
    submit_in = text_box2.get()
    try: 
        paper, year, question = submit_in.split('-')
        format = re.compile("P[1-9]-\d{4}-Q[1-9]") #Checks Papername-Year-Question format
        checkstate = "Q"
    except ValueError: #If no question is specified, user intends to check completion of full paper
        try:
            paper, year = submit_in.split('-')
            format = re.compile("P[1-9]-\d{4}") #Checks Papername-Year format only, later checks if the year is correct by making sure it is 4 digits long 
            checkstate = "P"
        except Exception:
            messagebox.showwarning("File Format Error", "Your input format might be incorrect - this can cause errors when searching for the question in the reserve. Try retyping it in the required format.")
            
    #If matching format captured in the Regular expression, passes on into function to submit into textfiles of each paper topic
    if format.match(submit_in) != None and len(year) == 4: #Will last another 8000 years!
        write_into_reserve(submit_in, checkstate)    
    else:
        messagebox.showerror("File Format Error","Check the 'year' entered is 4 digits long, and remainder of input is in the correct format.")
    


# Create the main window
window = tk.Tk()

#Instructions for use
messagebox.showinfo("How to use","This is used to keep track of completed papers and questions from Tripos.\nEnter in the format of P1-2018-Q3, which represents Question 3 of 2018 Paper 1.\nTo check if a full paper is complete, omit the '-Q3'.\n\nApply the same formatting when submitting questions to be written into the reserve, and it will update text files accordingly.")
sleep(0.5)

#1st section for checking the contents of the record of all completed questions - to prevent repeats
label = tk.Label(window, text="Please input details of paper and question:")
label.pack(side = "top")

# Add a text box for user input
text_box = tk.Entry(window)
text_box.pack()

# Add a button to trigger the file checking
button = tk.Button(window, text="Check", command=read_files)
button.pack()


#2nd section for submitting input files to add to record of completed questions
label = tk.Label(window, text="Please input details of paper and question:")
label.pack(side = "top")

text_box2 = tk.Entry(window)
text_box2.pack()

button2 = tk.Button(window, text="Submit", command=write_files)
button2.pack(side = "bottom")

# Run the main loop
window.mainloop()
