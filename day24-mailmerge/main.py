#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open('D:\Documents\Python lessons\AngelaYu\day24\Input\Letters\starting_letter.txt') as letter:
    body = letter.read()
print(body)

with open('D:\Documents\Python lessons\AngelaYu\day24\Input\Names\invited_names.txt') as guests:
    guest = guests.readlines()
print(guest)

guest = [nam.strip() for nam in guest]

for name in guest:
    name_letter = body.replace('[name]', name)
    with open("D:\documents\Python lessons\AngelaYu\day24\Output\ReadyToSend\f'letter_for_{name}.txt", mode='w') as final:
        final.write(name_letter)




# hello = ['  hi  ', '    seuon    ', '   tunde    ',  ' sesam    ']
# new = []
# # for _ in hello:
# #     clean = _.strip()
# #     new.append(clean)
# #     print(1, hello)
# #     print(2, new)


# clean = [_.strip() for _ in  hello]

# print(clean)