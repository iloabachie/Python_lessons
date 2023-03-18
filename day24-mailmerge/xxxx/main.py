#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open('starting_letter.txt') as letter:
    body = letter.read()
print(body)


with open('invited_names.txt') as guests:
    guest = guests.readlines()
print(1, guest)

guest = [nam.strip() for nam in guest]
print(2, guest)

for name in guest:
    name_letter = body.replace('[name]', name)
    print(name_letter)
    with open(f'letter_for_{name}.txt', mode='w') as final:
        final.write(name_letter)


