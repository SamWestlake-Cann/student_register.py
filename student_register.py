"""
Ask user for number of students to register
Loop for that amount of times asking for student ID
(Dots after ID for student signature)
open and write to file reg_form.txt    
"""

# Defining num as open string
num = ""

# Asking for required num of loops
num_stud = input("How many students would you like to register today? ")

# Adding num_stud to num
num += num_stud

# Open/create new fil with title Student ID Numbers:
with open('reg_form.txt', 'w') as f:
        f.write("Student ID Numbers:\n")

# Loop asking ID numbers for the amount of students registered 
# Change Str to Int  
for i in range(int(num)):
    stud_num = input("Please type your student ID number: ")
    # Append file reg_form with stud_num with dotted line for signature
    with open('reg_form.txt', 'a') as f:
        f.write(stud_num+'....................\n')

# Close file
f.close()

# Let user know ID's have been saved in reg_form    
print("Thankyou, all student ID's have been saved to txt file reg_form")