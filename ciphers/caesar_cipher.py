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
# NOTE: incorporate range into -b or -r
'''

file.py CIPHER[-e,-d,-b] KEY[-k] INPUT[-iF,-iT] OUTPUT[-oF, -oT]

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
key = None
input_file = None
input_text = None
output_file = None
output_text = None

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
            output += chr((ord(character) + int(encryption_key) - 65) % 26 + 65)
        else:
            output += chr((ord(character) + int(encryption_key) - 97) % 26 + 97)

    # NOTE: match lengths of input_text to see if any extra characters exist
    # remove extra character
    text_length = len(output)
    for num in range(0, text_length):
        if num != text_length - 1:
            output_text += output[num]

    #output content
    if input_file == None:
        print(output_text)
    else:
        with open(input_file, 'w') as f:
            f.write(output_text)

#parse all arguments
def parser():
    opts, args = getopt.getopt(sys.argv[2:], "k:iF:iT:oF:oT", ['key','inputFile','inputText', 'outputFile','outputText'])

    for opt, arg in opts:
        # inputflags
        if opt == "-iF" or opt == "--inputFile":
            input_file = arg
        if opt == "-iT" or opt == "--inputText":
            input_text = arg
        #output flags
        if opt == "-oF" or opt == "--outputFile":
            output_file = arg
        if opt == "-oT" or opt == "--outputText":
            output_text = arg
        # ciphering flags
        if opt == "-k" or opt == "--key":
            key = int(arg)

    return (key, input_file, input_text, output_file, output_text)

# cli 
def cli(argument_check):
    #display banner
    print(f"{banner}\n\n")

    # check for arguments
    # TODO: check if args are empty
    if argument_check == True:
        arguments = parser()
        ciphering_process = sys.argv[1]
        if ciphering_process == '-e':
            encrpyt_caesar()
        if ciphering_process == '-d':
            pass  # decrypt caesar
        if ciphering_process == '-b':
            pass  # bruteforce caesar
        # check for file input
        # if arguments[0] != None:
        #     readfile = open(arguments[0]).read()
        #     # encrypt file option
        #     if arguments[4] == True:
        #         encrpyt_caesar(readfile, arguments[3])
        #     # TODO: incorporate other cipher options here
        # else:
        #     if arguments[4] == True:
        #         encrpyt_caesar(arguments[1], arguments[3])
    else:
        # display options
        print("Options:\n\teF - Encrpty File\n\teT - Encrypt Text\n\tdF - Decrypt File\n\tdT - Decrypt Text\n\tbF - Bruteforce File\n\tbT - Bruteforce Text\n")
        option = input(f'{path}[~] Option : ')

        # option to encrypt file
        if option == 'eF':
            output_file_input = input(f'{path}[~] Enter File Name : ')
            shift_key = input(f'{path}[~] Enter Encrpytion Key : ')
            encrpyt_caesar(output_file_input, shift_key)


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
