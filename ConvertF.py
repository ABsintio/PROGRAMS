''' Convert File 
    We create a file with many number into it.
    Our goal is to convert that number from base 10 to 2, with a 
    function called conv_bin(x), where x in succesfully the 
    number in the file (positive and negative). The range of the 
    number goes from -128 to 127, otherwise the function's not able
    to convert'''

import re
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
 
