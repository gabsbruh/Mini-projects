#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

# Open the pattern and load to sample_text variable
with open("Input/Letters/starting_letter.txt", 'r') as sample:
    sample_text = sample.read()

# load the list of invitees  
with open("Input/Names/invited_names.txt", 'r') as invitees:
    invited = invitees.readlines()
    
# loop on invitiees and exchange [name] in pattern to a person
for inv in invited:    
    inv = inv.strip() # clears the \n
    personalized = sample_text.replace('[name]', inv)
    with open(f"Output/ReadyToSend/letter_for_{inv}.txt", 'w') as invitation:
        invitation.write(personalized)