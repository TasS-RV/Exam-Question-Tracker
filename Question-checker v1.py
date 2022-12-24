from time import sleep

print("""This is used to keep track of completed papers and questions from Tripos.
Enter in the format of P1-18-Q3, which represents Question 3 of 2018 Paper 1.
To check if a full paper is complete, omit the '-Q3'.""")
ans = True
while ans == True:    
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
