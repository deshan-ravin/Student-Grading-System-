'''# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
   # Any code taken from other sources is referenced within my code solution.
   # Student ID:[IIT:- 20221472],[UoW:- w1956167]
   # Date: 15/11/2022'''

creditpass=0
defer=0
fail=0
dictionary={}  #define dictionary
repeat='y'                    #define repeat variable for outer loop
def input_process(mark_type):     #input_process user defined function
            while True:
                try:                   #ValueError handling exception
                    creditlevel_1=int(input('Enter your total '+mark_type+ ' credits :'))
                    if creditlevel_1 not in range(0,140,20):
                        print('Out of range.')
                        continue
                    else:
                        break
                except ValueError:
                        print('Integer Required')
            return creditlevel_1

while repeat=='y':            #main outer loop

    while True:        #validity checking loop for ID
        try:                        #ValueError handling exception
            stu_id =int(input('Enter your student ID:w'))     #user input for id
            if len(str(stu_id))!=7:
                print('Invalid ID Number!! \n')
                continue
                    
        except ValueError:
            print('Integer Required \n')
        else:
            break
     
    creditpass=input_process('PASS')     #input_process funtion calling
 
    defer=input_process('DEFER')

    fail=input_process('FAIL')
     
    total=creditpass+defer+fail

            
    print()                
    total=creditpass+defer+fail    #users credit input total
    if total != 120:
        print("Total incorrect.")            #total check
            

    def credit_level_check(creditlevel_2):
        print(creditlevel_2)
        file_string= creditlevel_2+'- '+str(creditpass)+','+str(defer)+','+str(fail)  #convert int inputs to strings and file saving
        dictionary[stu_id]=(str (file_string)+" " )       #dictionary values append
                
    if total==120:
            
        if creditpass==120 and defer==0 and fail==0:                      #progress credit check
            credit_level_check('progress')
                
        elif(creditpass==100 and defer==20 and fail==0) or (creditpass==100 and defer==0 and fail==20):   #moduletrailer credit check
            credit_level_check('Module trailer')
                
        elif  fail>=80:                             #Exclude credit check
            credit_level_check('Exclude')                
                
        else:                                       #moduleretriever credit check
            credit_level_check('Module retriever')
        print()
            
    else:
        print()

         
    print('Would you like to enter another set of data?')                #user choice
    repeat=input("Enter 'y' for yes or 'q' to quit and view results:")   #user input as per repeat or end
    print()
    
    while True:                    #invalid user input check loop
        if repeat=='y':
            break              #loop break for correct input
        elif repeat=='q':
            break              #loop break for correct input
        else:
            print('Invalid Input')
            repeat=input("Enter 'y' for yes or 'q' to quit and view results:")      #for invalid input, re-entry of user input for repetition or ending
            print()
            
    if repeat=='q':
        break

print('xx '*25)
print()

print('Part 4')
print()
for element in dictionary.keys():             #loop for displaying keys and values
    print('w'+str(element),':',dictionary[element])
print()

print('xx '*25)
