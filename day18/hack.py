# import random
# import string

# characters = string.ascii_lowercase

# password = 'z'

# for char in range(5):
#     password += random.choice(characters)

# hack = ''
# i = 0

# while hack != password:
#     for a in characters:
#         hack += a
#         if hack == password:
#             break
#         for b in characters:
#             hack += b
#             if hack == password:
#                 break
#             for c in characters:
#                 hack += c
#                 if hack == password:
#                     break
#                 for d in characters:
#                     hack += d
#                     if hack == password:
#                         break
#                     for e in characters:
#                         hack += e
#                         if hack == password:
#                             break
#                         for f in characters:
#                             hack += e
#                             if hack == password:
#                                 break
#                             hack = hack[:-1]
#                         if hack == password:
#                             break
#                         hack = hack[:-1]   
#                     if hack == password:
#                         break                 
#                     hack = hack[:-1]  
#                 if hack == password:
#                     break
#                 hack = hack[:-1]  
#             if hack == password:
#                 break         
#             hack = hack[:-1]   
#         if hack == password:
#             break   
#         hack = hack[:-1]
# print(i, hack)


def hack(password):  
    import string
    characters = string.ascii_letters
    hack = ''
    
    def removletter():
        nonlocal hack
        if len(hack) > 0:
            if hack == password:
                return hack
            hack = hack[:-1]
            removletter()
        return hack
    
    def addletter():
        nonlocal hack
        if hack == password:
            return hack
        elif len(hack) == len(password):
            removletter()
        if len(hack) <= len(password):
            for _ in characters:
                hack += _
                if hack == password:
                    return hack
                addletter()            
        return hack
    
     
    while hack!= password:
        addletter()
        
    
    return hack  

print(hack('aaa'))
