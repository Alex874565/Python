#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


lettermodelpath = "Mail Merge Project Start/Input/Letters/starting_letter.txt"
namespath = "Mail Merge Project Start/Input/Names/invited_names.txt"
letterfolderpath = "Mail Merge Project Start/Output/ReadyToSend"


with open(lettermodelpath, "r") as letterfile:
    lettermodel = letterfile.read()
    with open(namespath, "r") as namesfile:
        names = namesfile.readlines()
        for name in names:
            name = name.strip()
            with open(f"{letterfolderpath}/Letter_for_{name}.txt", "w") as letter:
                letteraux = lettermodel
                letteraux = lettermodel.replace("[name]", name)
                letter.write(f"{letteraux}")
