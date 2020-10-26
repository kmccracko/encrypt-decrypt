import random
import sys

alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,?!@#$%^&*':;()1234567890-=+<>-_/[]"
addfactor = 15
additionals = 10

def encryption(alphabet,addfactor,additionals):
    message = input("Mesage:\n\n")
    
    alphabetnums = range(0,27)
    encryptout = []

    # ENCRYPTION

    for letter in message:
        indexnum = alphabet.index(letter) # translate the letter to respective number
        indexnum += addfactor # add a bit to the number
        encryptout = encryptout + [indexnum] # add the number to the output list
        for num in range(0,additionals): # add in "additionals" amount of fake nums
            encryptout = encryptout + [random.choice(alphabetnums)+addfactor]

    encryptout = encryptout + [addfactor]
    encryptout = encryptout + [additionals+addfactor] # these add the addfactor and additionals
                                            # values to the end so the decryptor can
                                            # use them in reversing the process


    # output is made into an easy to copy/paste "string"
    #   (because input wouldn't recognize a list with "[ , ]" to be a list,
    #   instead it would just read it as a string. so we prepare for that here

    print('\n\nEncryption:\n\n', *encryptout, sep='-')
    
def decryption(alphabet):
    encrypted = input("Enter encrypted text\n\n")

    # --------------------------------------------------------------------
    #   DECRYPTION

    encrypted = encrypted.replace('-','',1) # removes first dash
    encryptout = encrypted.split("-")       # separates into list by dashes
    # print(encryptout)

    decryptout = []

    addfactor = int(encryptout[-2])
    additionals = int(encryptout[-1])-addfactor

    del(encryptout[-1])
    del(encryptout[-1]) # these get rid of the additionals and addfactor keys

    # print("\nafter removing additionals and addfactor:")
    # print(encryptout)

    encryptlength = len(encryptout)

    messagelocation = []
    for num in range(0,encryptlength,additionals+1):# additionals is how many values to skip 
        messagelocation = messagelocation + [num]   #    identify the indexes of 
                                                    # each relevant value 
                                                    # (ignoring additionals)

    # print("\nThis is the message locations:")
    # print(messagelocation)

    newlist = []
    for x in messagelocation:           # uses location indexes to take relevant values
        realnum = encryptout[x]         # and put them into a new list
        newlist = newlist + [realnum]
    # print("\nThese are the important numbers")
    # print(newlist)

    for num in newlist:
        num = int(num) - addfactor      # subtracts number added to each value to get real
        decryptout += [alphabet[num]]   # value, then translates using alphabet and adds to output
    decryptout = "".join(decryptout)  # this outputs without list format

    print("\n\nDecrpytion:\n\n",decryptout)


loop = True
while loop:
    mode = input('\nAre you [e]ncrypting or [d]ecrypting?\n')

    if mode == 'e':
        addfactor = int(input('Addfactor: Choose a number between 100 and 1000: '))
        additionals = int(input('Additionals: Choose a number between 2 and 20: '))
        encryption(alphabet,addfactor,additionals)
    elif mode == 'd':
        decryption(alphabet)
    else:
        print('\tYou must type only "e" or "d"')
