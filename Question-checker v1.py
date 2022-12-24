from time import sleep

print("""This is used to keep track of completed papers and questions from Tripos.
Enter in the format of P1-18-Q3, which represents Question 3 of 2018 Paper 1.
To check if a full paper is complete, omit the '-Q3'.""")
ans = True
while ans == False:    
    user_in = input("\n Please input details of paper and question:")
    try: 
        paper, year, question = user_in.split('-')
        checkstate = "Q"
    except ValueError: #If no question is specified, user intends to check completion of full paper
        paper, year = user_in.split('-')
        checkstate = "P"
    
    with open(f"./Completed/{paper}.txt", 'r') as record:
        completion_state = False #Toggles for run checking 1 paper, or 1 question from a paper

        if checkstate == "P":
            for line in record.readlines():

                if (year in line) and len(year) == len(line.strip()): #Prevents mistaken pick-uof papers with single, some questions complete
                    print("\nYou have completed {1} {0}.".format(paper, year)) 
                    completion_state = True

            if completion_state == False: #After iterating through entire set
                    print("\n{1} {0} is incomplete. Better crack on with Tropos questions buddy.".format(paper, year))
        
        elif checkstate == "Q":            
            for line in record.readlines():
                if "{0}-{1}".format(year, question) in line:
                    print("\nYou have completed {1} {0}, question {2}.".format(paper, year, question))
                    completion_state = True #Same as above, toggled if it finds the question in the list
                
            if completion_state == False: 
                    print("\nThis question has not been completed")
        
        else:
            print("Invalid input. Program is unsure of details to check. Rerunning...")
            sleep(1) #Generating artifical delay for fun
        
        rerun = input("Check another paper/ question? Y/N")
        if rerun == "Y":
            ans = True
        else: #Explicit Y required, otherwise terminates
            ans = False 
            print("Thanks for using this service!")
            raise SystemExit
import re
import os

def write_into_reserve(input_info, checkstate = "Q"):
    for direc, subdirec, files in os.walk("{}/Completed/".format(os.getcwd())):
        if checkstate == "P":
            paper, remainder = submit_in.split('-') #Filenames as per paper
        elif checkstate == "Q":
            paper, year, question = submit_in.split('-')
            remainder = year+"-"+question

        if f"{paper}.txt" not in files:
            #Anytime a questions from a paper not previously attempted is sunmitted, it must generate the file first
            with open(f"./Completed/{paper}.txt", 'w') as file_writer:
                file_writer.write(f"{remainder}\n")
        
        elif f"{paper}.txt" in files: 
            #If questions from this paper were previously attempted - 'append' mode, to prevent record of previous questions beig overwritten
            with open(f"./Completed/{paper}.txt", 'a') as file_writer:
                file_writer.write(f"{remainder}\n")
        

                

n = False
while n:
    submit_in = input("Which question/ paper have you completed?")
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
            print("Your input format might be incorrect - this can cause errors when searching for the question in the reserve. Try retyping it in the required format.")

    #If matching format captured in the Regular expression, passes on into function to submit into textfiles of each paper topic
    if format.match(submit_in) != None and len(year) == 4: #Will last another 8000 years!
        write_into_reserve(submit_in, checkstate)    
    else:
        print("Check the 'year' entered is 4 digits long, and remainder of input is in the correct format.")
    
    n = False

with open("./Completed/P13.txt", 'r') as filereader:
    pass
