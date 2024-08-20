#!/usr/bin/python

# caesar cipher package for helena
# author : inukashi


#argument parsing
"""
print(sys.argv[0])
print(sys.argv[1])

opts, args = getopt.getopt(sys.argv[1:], "f:m:", ['filename','message'])

for opt, arg in opts:
    if opt == '-f':
        filename = arg

    if opt == '-m':
        message = arg
"""


#arguments
'''
-iF = input file
-iT = input text
-oF = output file
-oT = output text
-k = key
-e = encrypt
-d = decrypt
-b = bruteforce
'''
# NOTE: incorporate range into -b or just do -r

#imports
import sys
import getopt
import getpass      #to get username

banner = r'''
   ______                           _______       __             
  / ____/___ ____  _________ ______/ ____(_)___  / /_  ___  _____
 / /   / __ `/ _ \/ ___/ __ `/ ___/ /   / / __ \/ __ \/ _ \/ ___/
/ /___/ /_/ /  __(__  ) /_/ / /  / /___/ / /_/ / / / /  __/ /    
\____/\__,_/\___/____/\__,_/_/   \____/_/ .___/_/ /_/\___/_/     
                                       /_/                       
                                                            
'''

# argument variables
cipherfile = None
ciphertext = None
plainfile = None
#plaintext = None
key = None
encryption = None
decryption = None
bruteforce = None

# symbols that can't be processed through the caesar cipher
symbols = ['\n', '\t', ' ', '.', '?', '!', ',', '/', '\\', '<', '>', '|',
           '[', ']', '{', '}', '@', '#', '$', '%', '^', '&', '*', '(', ')',
           '-', '_', '=', '+', '`', '~', ':', ';', '"', "'", '0', '1', '2', '3',
           '4', '5', '6', '7', '8', '9']

# generate path
path = f"{getpass.getuser()}@helena $ "

# encrypt text
def encrpyt_caesar(plain_content, encryption_key):   #encryption_key is the shift
    # output variable
    output = ""
    output_text = ""

    #encryption process
    for character in plain_content:
        if character in symbols:
            output += character
        elif character.isupper():
            output += chr((ord(character) + encryption_key - 65) % 26 + 65)
        else:
            output += chr((ord(character) + encryption_key - 97) % 26 + 97)

    # NOTE: match lengths of ciphertext to see if any extra characters exist
    # remove extra character
    text_length = len(output)
    for num in range(0, text_length):
        if num != text_length - 1:
            output_text += output[num]

    #output content
    if cipherfile == None:
        print(output_text)
    else:
        with open(cipherfile, 'w') as f:
            f.write(output_text)

#parse all arguments
def parser():
    opts, args = getopt.getopt(sys.argv[1:], "iF:iT:o:k:e:d:b:", ['inputFile','inputText', 'outputFile','key','encrypt','decrypt','bruteforce'])

    for opt, arg in opts:
        # inputflags
        if opt == "-iF" or  opt == "--inputFile":
            cipherfile = arg
        if opt == "-iT" or opt == "--inputText":
            ciphertext = arg
        #output flags
        if opt == "-o" or opt == "--outputFile":
            plainfile = arg
        # if opt == "-oT" or opt =="--outputText":
        #     plaintext = arg
        # ciphering flags
        if opt == "-k" or opt == "--key":
            key = int(arg)
        # TODO: make em kwargs
        if opt == "-e" or opt == "--encypt":
            encryption = True
        if opt == "-d" or opt == "--decrypt":
            decryption = True
        if opt == "-b" or opt == "--bruteforce":
            bruteforce = True

    return (cipherfile, ciphertext, plainfile, key, encryption, decryption, bruteforce)

# cli 
def cli(argument_check):
    #display banner
    print(f"{banner}\n\n")

    # check for arguments
    arguments = parser()
    if argument_check == True:
        # check for file input
        if arguments[0] != None:
            readfile = open(arguments[0]).read()
            # encrypt file option
            if arguments[4] == True:
                encrpyt_caesar(readfile, arguments[3])
            # TODO: incorporate other cipher options here
        else:
            if arguments[4] == True:
                encrpyt_caesar(arguments[1], arguments[3])
    else:
        # display options
        print("Options:\n\teF) Encrpty File\n\teT - Encrypt Text\n\tdF - Decrypt File\n\tdT - Decrypt Text\n\tbF - Bruteforce File\n\tbT - Bruteforce Text\n")
        option = input(f'{path}[~] Option : ')

        # option to encrypt file
        if option == 'eF':
            plainfile_input = input(f'{path}[~] Enter File Name : ')
            shift_key = input(f'{path}[~] Enter Encrpytion Key : ')
            encrpyt_caesar(plainfile_input, shift_key)


# main function for caesar cipher
def caesar_main():
    #checks for arguments
    try:
        sys.argv[1]
    except IndexError:
        arguments_exist = False
    else:
        arguments_exist = True
    cli(arguments_exist)


if __name__ == '__main__':
    caesar_main()
