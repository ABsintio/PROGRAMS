''' Convert File 
    We create a file with many number into it.
    Our goal is to convert that number from base 10 to 2, with a 
    function called conv_bin(x), where x in succesfully the 
    number in the file (positive and negative). The range of the 
    number goes from -128 to 127, otherwise the function's not able
    to convert'''

import re
#BConversion is not a repository of standard library is a script created by me
#It's in that repository of github 
from BConversion import conv_bin

#First define a function that take for arguments Fin, Fout
#Fin is the file where we'll find the number 
#Fout is the file where we'll save the converted number
def fileConverter(Fin, Fout):
    
    #Create and load the file
    File_In = open(Fin, 'x')
    #inizialized a variable str
    string = '0'
    while not string == '':
      string = input('Insert the number: ')
      #Write the number into the File_In with a print function
      print(string, end='\n', file=File_In, flush=False)
    #Close the file to save it
    File_In.close()
    #Reopen the file to apply the conversion
    File_In = open(Fin)
    resultlist = listConversion(File_In)
    #Save the result file 
    saveFile(Fout, resultlist)

#Function to convert the number in the file
def listConversion(File):
    #Inizialized a list
    resultlist = []
    for number in File:
        if not number.startswith('-'):
            #m become an integer when the regex take all the string
            #numbers in the number, and form the integer number in m
            m = re.match('\d+', number)
        else:
            #Like before but take also the minus to 
            #indicate that the number is negative
            m = re.match('(-)\d+', number)
        if m:
            resultlist.append(conv_bin(int(m.group(0))))
    return resultlist

#Function to save the file with the number converted
def saveFile(Fout, numbers):
    File_Out = open(Fout, 'x')
    for element in numbers:
        print(element, end='\n', file=File_Out, flush=True)
        
